#!/usr/bin/env python3
"""Fetch Bilibili subtitles for study/research use.

Strategy:
1. Read public video metadata and subtitle metadata.
2. If BILIBILI_SESSDATA is available, send it for AI subtitle tracks.
3. Download subtitle JSON when a track URL is exposed.
4. Fall back to yt-dlp if installed.

This script does not bypass paywalls or access controls.
"""

from __future__ import annotations
import argparse
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/147 Safari/537.36"
API = "https://api.bilibili.com"


def bvid_of(s: str) -> str:
    m = re.search(r"(BV[a-zA-Z0-9]{10})", s)
    if not m:
        raise SystemExit(f"cannot find BVID in: {s}")
    return m.group(1)


def get_json(url: str, referer: str | None = None, sessdata: str | None = None):
    headers = {"User-Agent": UA}
    if referer:
        headers["Referer"] = referer
    if sessdata:
        headers["Cookie"] = f"SESSDATA={sessdata}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def save_track(url: str, out: pathlib.Path, referer: str, sessdata: str | None):
    if url.startswith("//"):
        url = "https:" + url
    payload = get_json(url, referer=referer, sessdata=sessdata)
    body = payload.get("body") or []
    out.write_text("\n".join(str(x.get("content", "")) for x in body), encoding="utf-8")
    out.with_suffix(".json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return len(body)


def public_api(bvid: str, outdir: pathlib.Path, sessdata: str | None):
    referer = f"https://www.bilibili.com/video/{bvid}/"
    view = get_json(
        f"{API}/x/web-interface/view?" + urllib.parse.urlencode({"bvid": bvid}),
        referer=referer,
        sessdata=sessdata,
    )
    if view.get("code") != 0:
        raise RuntimeError(f"view API failed: {view}")
    data = view["data"]
    pages = data.get("pages") or [{"cid": data.get("cid"), "page": 1, "part": data.get("title")}]
    summary = {"bvid": bvid, "title": data.get("title"), "aid": data.get("aid"), "pages": []}

    for p in pages:
        cid = p.get("cid")
        page_no = p.get("page")
        part = p.get("part")
        meta_url = f"{API}/x/player/wbi/v2?" + urllib.parse.urlencode({"bvid": bvid, "cid": cid})
        meta = get_json(meta_url, referer=referer, sessdata=sessdata)
        tracks = ((meta.get("data") or {}).get("subtitle") or {}).get("subtitles") or []
        row = {
            "page": page_no,
            "cid": cid,
            "part": part,
            "tracks": [{"lan": t.get("lan"), "lan_doc": t.get("lan_doc")} for t in tracks],
        }
        chosen = None
        for t in tracks:
            lan = str(t.get("lan") or "")
            if lan.startswith("ai-") or lan in {"zh-CN", "zh-Hans", "zh"}:
                chosen = t
                if lan == "ai-zh":
                    break
        if chosen and chosen.get("subtitle_url"):
            stem = outdir / f"P{int(page_no):02d}"
            count = save_track(chosen["subtitle_url"], stem.with_suffix(".txt"), referer, sessdata)
            row["saved"] = str(stem.with_suffix(".txt"))
            row["subtitle_count"] = count
            row["language"] = chosen.get("lan")
        summary["pages"].append(row)

    (outdir / "metadata.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def yt_dlp_fallback(source: str, outdir: pathlib.Path):
    cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs", "ai-zh,zh-CN,zh-Hans,zh.*",
        "--sub-format", "srt/vtt/best",
        "-o", str(outdir / "yt-%(playlist_index|)s-%(title)s.%(ext)s"),
        source,
    ]
    proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (outdir / "yt-dlp.log").write_text(proc.stdout, encoding="utf-8")
    return proc.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--out", default="bilibili-output")
    args = ap.parse_args()
    outdir = pathlib.Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    bvid = bvid_of(args.source)
    sess = os.getenv("BILIBILI_SESSDATA") or None

    errors = []
    try:
        summary = public_api(bvid, outdir, sess)
        saved = [p for p in summary["pages"] if p.get("saved")]
        print(f"public/api path: {len(saved)}/{len(summary['pages'])} pages saved")
        if saved:
            return 0
    except Exception as e:
        errors.append(f"api: {type(e).__name__}: {e}")

    try:
        rc = yt_dlp_fallback(args.source, outdir)
        print(f"yt-dlp exit={rc}")
        if rc == 0 and (any(outdir.glob("*.srt")) or any(outdir.glob("*.vtt"))):
            return 0
    except Exception as e:
        errors.append(f"yt-dlp: {type(e).__name__}: {e}")

    (outdir / "errors.txt").write_text("\n".join(errors), encoding="utf-8")
    print("\n".join(errors), file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
