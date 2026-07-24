---
spec_id: DBRAP-PROTOTYPE-TASKS-0.1
source_scope: Paper-3-EOA-research-workflow
status: DEFINED_NOT_RUN
task_count: 4
source_documents_bound: false
tasks_executed: false
---

# Prototype Task Definition v0.1（原型任务定义 v0.1）

## 1. Scope（范围）

本文件定义未来实验使用的四项真实科研工作流任务类别。任务语境来自 Paper 3 的 Evidence Object Architecture（EOA，证据对象架构）研究工作流，但当前 `source_documents: []`，没有 Paper 3 来源或数据绑定到 Context，也没有执行任何任务。

```text
Real Research Task Definition ≠ Executed Research Task
Paper 3 Reference ≠ Paper 3 Data Access
Task Output ≠ Scientific Result
```

## 2. Common Preconditions（共同前提）

每项任务在执行前必须具有：

- 经 Human Review 的 Context Package 与来源版本；
- Human Research Owner、Reviewer 和授权引用；
- 相同实验条件间的输入材料、时间预算和验收说明；
- 明确 Allowed Action（允许行为）、Prohibited Action（禁止行为）和停止条件；
- 预注册的 Evaluation Metrics（评价指标）与 Evidence Plan；
- 医学、伦理、隐私、数据和发表边界。

## 3. Task 1: Literature Review（文献综述）

### Objective（目标）

在批准的来源集合内组织 EOA 相关研究主张、方法、限制、冲突和 Unknown。

### Allowed Assistance（允许的辅助）

- Literature organization；
- 来源定位与版本整理；
- 有来源的 Knowledge synthesis；
- 冲突、缺失和 Unknown 标记。

### Required Output（必要输出）

- Literature Map（文献图谱）；
- 来源与版本索引；
- 主张—来源连接；
- 冲突、Unknown 与限制列表。

### Prohibited（禁止）

不得自动抓取未批准来源、伪造引用、把摘要写成 Scientific Truth 或形成最终 Related Work（相关工作）结论。

## 4. Task 2: Benchmark Design（基准设计）

### Objective（目标）

依据已批准研究问题和材料，组织可比较的任务案例、输入边界、评分 Rubric（量表）和泄漏控制候选。

### Required Output（必要输出）

- Benchmark Case 候选；
- 条件等价性检查项；
- Scoring Rubric 候选；
- 偏差、泄漏、伦理和限制清单。

### Prohibited（禁止）

不得运行 Benchmark、观察结果后修改评分规则、导入医学影像数据或声称 Benchmark 已验证。

## 5. Task 3: Experiment Planning（实验规划）

### Objective（目标）

组织 Human-only、Generic AI Assistant 与 Governed Research Agent 三条件的候选程序、对照、停止规则和 Evidence Capture（证据捕获）要求。

### Required Output（必要输出）

- 步骤与条件映射；
- 变量、对照和混杂因素；
- Human Review 与停止点；
- Evidence 和 Evaluation 数据需求；
- 待 Human Research Owner 决定的 Unknown。

### Prohibited（禁止）

不得批准或运行实验、选择最终统计结论、修改原始数据或把计划写成 Execution Record（执行记录）。

## 6. Task 4: Draft Organization（草稿组织）

### Objective（目标）

根据已完成并复核的真实 Experiment Record、Evidence Record、Evaluation Result 和 Analysis Report，组织 Manuscript Section（论文部分）候选结构。

### Required Output（必要输出）

- Claim-to-Evidence Map（主张—证据映射）；
- Section Outline（章节结构）；
- 引用、Unknown、限制和负面结果入口；
- 明确标记的 Draft Text Candidate（草稿文本候选）。

### Prohibited（禁止）

没有真实实验记录时不得生成 Results Claim（结果主张）；不得自主署名、投稿、发表、隐藏负面结果或把 Draft Paper 写成 Accepted Paper。

## 7. Cross-condition Comparability（跨条件可比性）

四项任务在三个实验条件中必须冻结相同：

- Task ID 与版本；
- 来源集合与访问边界；
- 时间预算；
- 期望材料类型；
- 禁止行为；
- Human Review Rubric；
- Unknown 与失败保留规则。

任何偏离必须进入 Experiment Record，不能静默修复。

## 8. Current State（当前状态）

```text
TASK_DEFINITION_VERSION=v0.1
TASKS_DEFINED=4
TASK_SOURCE_SCOPE=PAPER_3_EOA_WORKFLOW
SOURCE_DOCUMENTS_BOUND=0
BENCHMARK_CASES_FROZEN=0
TASK_AUTHORIZATIONS=0
TASKS_EXECUTED=0
RESEARCH_RESULTS_CREATED=0
```
