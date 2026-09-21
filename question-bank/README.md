# question-bank

操作系统真题 / 练习题结构化记录目录。

## 当前状态

已参考仓库中其他科目的题库组织方式：

- 概率统计、线性代数：保留原 PDF / 页码索引，强调来源可追溯；
- 计算机网络：采用 `questions.jsonl` + 按年份 / 按知识点双索引；
- 408 真题分支：保留按年份检索入口。

操作系统分支采用上述方式的组合，并把**按知识点刷题**设为主入口。

当前已从已上传 BOK25 操作系统 PDF 中核对、去重并正式入库 **10 道带明确年份的题目**。

> 这 10 道仅代表“当前上传讲义中明确出现的历年题”，不代表完整 408 操作系统真题总量。

## 文件

- `questions.jsonl`：一题一行的机器可检索主库
- `by-topic.md`：按知识点总索引，刷题主入口
- `by-year.md`：按年份交叉索引
- `by-topic/02-synchronization.md`：进程同步与互斥
- `by-topic/03-memory-management.md`：内存管理
- `by-topic/04-file-system.md`：文件系统
- `source-question-index.md`：来源 PDF / 页码 / 去重记录
- `wrong-questions.md`：错题记录
- `retest.md`：复测记录

## 单题字段

- `id`
- `year`
- `type`
- `topic`
- `subtopic`
- `source_file`
- `source_page`
- `stem`
- `options`
- `answer`
- `verification_status`
- `review_status`

## 入库规则

1. 题面必须能追溯到明确 PDF 与页码。
2. 课件连续多页演示同一道题时，只保留首次完整题面，后续解析页不重复计数。
3. 带年份的真题与普通教学例题分开；普通例题不自动计入历年真题覆盖率。
4. 题目按“知识点主分类 + 年份副索引”组织。
5. 刷题时先隐藏答案；用户作答后再核对 `answer` / 原解析。
6. 新资料到达后增量抽取，不重建旧题 ID。

## 刷题原则

- 题面完整，不拆成只剩机械计算的最后一步。
- 用户先做，再判断具体错误位置。
- 地址转换、调度、PV、死锁、文件分配、磁盘调度等保留完整中间过程。
- 识别不清时回查原 PDF 页面，不猜题。
- 重复错误进入 `wrong-questions.md` 并安排同型复测。
