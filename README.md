# Bilibili 字幕读取工具

统一入口：

```bash
python tools/bilibili_reader/fetch_subtitles.py BV1xxxxxxxx --out /tmp/bilibili-output
```

工具会先读取完整分P元数据与 B站字幕轨，再按需回退到 `yt-dlp`。`metadata.json` 记录总P数、CID、标题、时长、逐P字幕状态、字幕来源和完整性；只有全部分P均成功读取时，公开 API 路径才返回成功。

若 AI 字幕只对登录用户可见，可显式启用一次性扫码登录：

```bash
python -m pip install 'qrcode[pil]'
python tools/bilibili_reader/fetch_subtitles.py BV1xxxxxxxx --out /tmp/bilibili-output --qr-login
```

扫码登录的 Cookie 只保存在当前进程内存中，不写入输出目录或 Git。二维码图片写入系统临时目录，登录成功、超时或失败后自动删除。

也可复用本机已登录的 Chrome / Edge 会话：

```bash
python -m pip install browser-cookie3
python tools/bilibili_reader/fetch_subtitles.py BV1xxxxxxxx --out /tmp/bilibili-output --cookies-from-browser edge
```

该模式只读取 `.bilibili.com` Cookie，并仅在当前进程内存中构造请求头；Cookie 值不会打印或写入文件。

长任务若需避免 macOS 密钥链反复授权，可通过 `--cookies-file` 读取一个权限受限的临时 Netscape Cookie 文件。该文件必须位于系统临时目录，并在任务结束后立即删除；禁止放入仓库、下载目录或长期缓存。

也可继续使用既有环境变量 `BILIBILI_SESSDATA`。禁止把该变量、Cookie、二维码或浏览器配置提交到仓库。

## 408 真题基线

本分支专门维护 **计算机 408 统考真题**，当前覆盖 **2009—2023 年**。

目前已完成：

- **数据结构：193 题**
- **计算机组成原理：196 题**

两门均提供 **按年份**、**按知识点**、**刷题进度** 与 **机器可读 JSONL** 入口。

## 数据结构

- [总索引](./数据结构/索引.md)
- [全部真题索引](./数据结构/全部真题索引.md)
- [按知识点](./数据结构/按知识点/README.md)
- [刷题进度](./数据结构/刷题进度.md)
- `数据结构/年份/`：2009—2023 每年单独定位
- `数据结构/questions.jsonl`：机器可读索引

范围：

- 2009 年单项选择题：1～10
- 2010—2023 年单项选择题：1～11
- 综合应用题按实际学科归属逐年判断

## 计算机组成原理

- [总索引](./计算机组成原理/索引.md)
- [全部真题索引](./计算机组成原理/全部真题索引.md)
- [按知识点](./计算机组成原理/按知识点/README.md)
- [刷题进度](./计算机组成原理/刷题进度.md)
- `计算机组成原理/年份/`：2009—2023 每年单独定位
- `计算机组成原理/questions.jsonl`：机器可读索引

范围：

- 2009 年单项选择题：11～22
- 2010—2023 年单项选择题：12～22
- 综合应用题按实际学科归属逐年判断，共 30 题

按知识点分为：

1. 计算机系统概述
2. 数据的表示与运算
3. 存储系统
4. 指令系统
5. 中央处理器
6. 总线
7. 输入输出系统

## 当前整理原则

1. 知识点文件只写 **年份-题号 + 题型 + 题干摘要/核心考点**，默认不写答案，便于真正刷题。
2. 需要做某一题时，再回到原始 408 真题读取完整题面、选项、公式、代码和图。
3. 图形、公式、代码或文字转写出现异常时，以原卷为准，不依据摘要猜题。
4. 年份索引用于整套刷题；知识点索引用于专项训练；JSONL 用于覆盖率和错题状态的自动统计。
