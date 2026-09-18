# 三本线代题册归档

## 目标

把三本题册中的全部题目按原 PDF 源页识别并归档，保留：

- 题册编号。
- PDF 页码。
- 页标题 / 题源标签。
- 完整题面。
- 选项（如有）。
- 答案。
- 原解析或关键解法。
- 识别 / 核对状态。
- 刷题状态。

## 源页规模

| 题册 | 页数 |
|---|---:|
| 纯真题必做版 | 346 |
| 真题 + 重点题 | 385 |
| 好习题集版 | 563 |
| 合计 | 1294 |

## 当前识别状态

- 1294 个源页均已建立文本层页标题索引。
- 页面主体大量为图像；完整题面与数学公式需要逐页视觉核对。
- 机器 OCR 仅作草稿，不把未核对的公式作为最终题面。
- 之后每完成一批视觉核对，就将完整题面写入本目录并更新覆盖状态。

## 页索引

- `book-1-pure-real-exams-page-index.txt`
- `book-2-real-and-key-page-index.txt`
- `book-3-exercises-page-index.txt`

## 归档格式

后续完整题目按章节分文件，例如：

- `01-determinants.md`
- `02-matrices.md`
- `03-vectors.md`
- `04-linear-systems.md`
- `05-eigenvalues.md`
- `06-quadratic-forms.md`

每题至少记录：

`[book/page/source-label/status]`

其中 status：

- `indexed`：仅页标题已建立。
- `ocr-draft`：机器 OCR 草稿。
- `verified`：已对原页视觉核对。
- `solved`：学习者已刷。
