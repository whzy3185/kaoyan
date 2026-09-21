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
import http.cookiejar
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/147 Safari/537.36"
API = "https://api.bilibili.com"


def bvid_of(s: str) -> str:
    m = re.search(r"(BV[a-zA-Z0-9]{10})", s)
    if not m:
        raise SystemExit(f"cannot find BVID in: {s}")
    return m.group(1)


def get_json(
    url: str,
    referer: str | None = None,
    cookie: str | None = None,
    opener: urllib.request.OpenerDirector | None = None,
):
    headers = {"User-Agent": UA}
    if referer:
        headers["Referer"] = referer
    if cookie:
        headers["Cookie"] = cookie
    req = urllib.request.Request(url, headers=headers)
    open_url = opener.open if opener else urllib.request.urlopen
    with open_url(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def save_track(url: str, out: pathlib.Path, referer: str, cookie: str | None):
    if url.startswith("//"):
        url = "https:" + url
    payload = get_json(url, referer=referer, cookie=cookie)
    body = payload.get("body") or []
    out.write_text("\n".join(str(x.get("content", "")) for x in body), encoding="utf-8")
    out.with_suffix(".json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return len(body)


def public_api(bvid: str, outdir: pathlib.Path, cookie: str | None):
    referer = f"https://www.bilibili.com/video/{bvid}/"
    view = get_json(
        f"{API}/x/web-interface/view?" + urllib.parse.urlencode({"bvid": bvid}),
        referer=referer,
        cookie=cookie,
    )
    if view.get("code") != 0:
        raise RuntimeError(f"view API failed: {view}")
    data = view["data"]
    pages = data.get("pages") or [{"cid": data.get("cid"), "page": 1, "part": data.get("title")}]
    summary = {
        "bvid": bvid,
        "title": data.get("title"),
        "aid": data.get("aid"),
        "total_pages": len(pages),
        "pages": [],
    }

    for p in pages:
        cid = p.get("cid")
        page_no = p.get("page")
        part = p.get("part")
        duration = p.get("duration")
        meta_url = f"{API}/x/player/wbi/v2?" + urllib.parse.urlencode({"bvid": bvid, "cid": cid})
        meta = get_json(meta_url, referer=referer, cookie=cookie)
        tracks = ((meta.get("data") or {}).get("subtitle") or {}).get("subtitles") or []
        row = {
            "page": page_no,
            "cid": cid,
            "part": part,
            "duration_seconds": duration,
            "tracks": [{"lan": t.get("lan"), "lan_doc": t.get("lan_doc")} for t in tracks],
            "subtitle_status": "unavailable",
            "subtitle_source": None,
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
            try:
                count = save_track(chosen["subtitle_url"], stem.with_suffix(".txt"), referer, cookie)
                row["saved"] = str(stem.with_suffix(".txt"))
                row["subtitle_count"] = count
                row["language"] = chosen.get("lan")
                row["subtitle_status"] = "downloaded"
                row["subtitle_source"] = (
                    "bilibili_ai" if str(chosen.get("lan") or "").startswith("ai-") else "bilibili"
                )
            except Exception as e:
                row["subtitle_status"] = "error"
                row["subtitle_error"] = f"{type(e).__name__}: {e}"
        summary["pages"].append(row)

    summary["successful_pages"] = sum(p.get("subtitle_status") == "downloaded" for p in summary["pages"])
    summary["complete"] = summary["successful_pages"] == summary["total_pages"]
    (outdir / "metadata.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def yt_dlp_fallback(source: str, outdir: pathlib.Path):
    if re.fullmatch(r"BV[a-zA-Z0-9]{10}", source):
        source = f"https://www.bilibili.com/video/{source}/"
    executable = shutil.which("yt-dlp")
    if executable:
        cmd = [executable]
    else:
        try:
            __import__("yt_dlp")
        except ImportError as e:
            raise FileNotFoundError("yt-dlp is not installed") from e
        cmd = [sys.executable, "-m", "yt_dlp"]
    cmd += [
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


def qr_login(timeout_seconds: int = 180) -> str:
    try:
        import qrcode
    except ImportError as e:
        raise RuntimeError("QR login requires: python -m pip install 'qrcode[pil]'") from e

    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    referer = "https://passport.bilibili.com/login"
    generated = get_json(
        "https://passport.bilibili.com/x/passport-login/web/qrcode/generate",
        referer=referer,
        opener=opener,
    )
    data = generated.get("data") or {}
    login_url = data.get("url")
    qrcode_key = data.get("qrcode_key")
    if not login_url or not qrcode_key:
        raise RuntimeError(f"QR generation failed: {generated}")

    fd, qr_name = tempfile.mkstemp(prefix="bilibili-login-", suffix=".png")
    os.close(fd)
    qr_path = pathlib.Path(qr_name)
    qrcode.make(login_url).save(qr_path)
    print(f"QR_IMAGE={qr_path}", flush=True)
    print("Scan the QR code with the Bilibili mobile app.", flush=True)

    deadline = time.monotonic() + timeout_seconds
    poll_url = "https://passport.bilibili.com/x/passport-login/web/qrcode/poll?" + urllib.parse.urlencode(
        {"qrcode_key": qrcode_key}
    )
    try:
        while time.monotonic() < deadline:
            payload = get_json(poll_url, referer=referer, opener=opener)
            poll_data = payload.get("data") or {}
            code = poll_data.get("code")
            if code == 0:
                if not list(jar) and poll_data.get("url"):
                    opener.open(urllib.request.Request(poll_data["url"], headers={"User-Agent": UA}), timeout=30)
                cookie = "; ".join(f"{item.name}={item.value}" for item in jar)
                if "SESSDATA=" not in cookie:
                    raise RuntimeError("QR login succeeded but no SESSDATA cookie was received")
                print("QR login succeeded; credentials remain in memory only.", flush=True)
                return cookie
            if code == 86038:
                raise RuntimeError("QR code expired")
            time.sleep(2)
        raise RuntimeError("QR login timed out")
    finally:
        qr_path.unlink(missing_ok=True)


def browser_cookie_header(browser: str) -> str:
    try:
        import browser_cookie3
    except ImportError as e:
        raise RuntimeError("Browser cookie access requires: python -m pip install browser-cookie3") from e

    loaders = {
        "chrome": browser_cookie3.chrome,
        "edge": browser_cookie3.edge,
    }
    jar = loaders[browser](domain_name=".bilibili.com")
    cookies = [item for item in jar if "bilibili.com" in item.domain]
    cookie = "; ".join(f"{item.name}={item.value}" for item in cookies)
    if "SESSDATA=" not in cookie:
        raise RuntimeError(f"No logged-in Bilibili SESSDATA cookie found in {browser}")
    print(f"Loaded Bilibili login cookies from {browser}; values remain in memory only.", flush=True)
    return cookie


def cookie_file_header(path: pathlib.Path) -> str:
    jar = http.cookiejar.MozillaCookieJar(str(path))
    jar.load(ignore_discard=True, ignore_expires=True)
    cookies = [item for item in jar if "bilibili.com" in item.domain]
    cookie = "; ".join(f"{item.name}={item.value}" for item in cookies)
    if "SESSDATA=" not in cookie:
        raise RuntimeError(f"No logged-in Bilibili SESSDATA cookie found in {path}")
    print("Loaded Bilibili login cookies from a temporary cookie file; values were not printed.", flush=True)
    return cookie


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--out", default="bilibili-output")
    ap.add_argument("--cookies-file", type=pathlib.Path, help="Temporary Netscape cookie file; never commit it")
    ap.add_argument("--cookies-from-browser", choices=("chrome", "edge"))
    ap.add_argument("--qr-login", action="store_true", help="Use one-time QR login; credentials stay in memory")
    ap.add_argument("--qr-timeout", type=int, default=180)
    args = ap.parse_args()
    outdir = pathlib.Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    bvid = bvid_of(args.source)
    sess = os.getenv("BILIBILI_SESSDATA") or None
    cookie = f"SESSDATA={sess}" if sess else None
    if args.cookies_file:
        cookie = cookie_file_header(args.cookies_file)
    if args.cookies_from_browser:
        cookie = browser_cookie_header(args.cookies_from_browser)
    if args.qr_login:
        cookie = qr_login(args.qr_timeout)

    errors = []
    try:
        summary = public_api(bvid, outdir, cookie)
        saved = [p for p in summary["pages"] if p.get("saved")]
        print(f"public/api path: {len(saved)}/{len(summary['pages'])} pages saved")
        if summary.get("complete"):
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
