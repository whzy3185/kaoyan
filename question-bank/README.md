# 真题与练习题库

本目录用于计算机网络真题/练习题的结构化归档和刷题状态维护。

## 建议结构

- `questions.jsonl`：一题一行，机器可检索
- `by-year/`：按年份整理
- `by-topic/`：按知识点整理
- `wrong-questions.md`：用户错题与复测记录

## 单题字段

- `id`
- `year`
- `question_no`
- `type`
- `topic`
- `subtopic`
- `source_file`
- `source_page`
- `stem`
- `options`
- `answer`
- `analysis`
- `user_answer`
- `result`
- `error_tags`
- `review_status`
- `last_reviewed_at`

## 刷题原则

- 题面必须完整，不把题拆到只剩最后一步机械运算。
- 第一次做题先不给答案。
- 用户作答后精确指出错误位置，再讲原因。
- 题目本身识别不清时回查PDF原页，不猜测。
- 真题和教材练习分开标记，避免混淆。
