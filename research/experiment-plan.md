---
plan_id: DBRAP-EXPERIMENT-PLAN-0.1
status: design-only
preregistered: false
approved: false
executed: false
---

# Experiment Plan v0.1（实验计划 v0.1）

## 1. Purpose（目的）

本文件定义未来比较实验的最小设计。当前只定义，不招募参与者、不读取研究数据、不调用模型、不运行任务，也不产生实验结果。

## 2. Comparison Conditions（比较条件）

| 条件 | 定义 | 需要控制的边界 |
|---|---|---|
| Human-only Baseline（纯人工基线） | 人类研究者使用批准材料与常规研究工具完成任务 | 记录工具、时间、经验和缺失项；不能把未记录过程当作 Agent 劣势 |
| AI Assistant Baseline（人工智能助手基线） | 人类使用一般 AI 助手，但没有完整 DBOS 引用与 SAEE 评价闭环 | 固定模型、版本、提示、访问边界和人工操作；输出仍需人工核验 |
| Governed Research Agent（受治理科研智能体） | 未来系统在明确身份、执行、证据、验证引用及人工监督下辅助任务，并接受 SAEE 评价 | 必须另行实现和授权；不能因治理结构更多而预设效果更好 |

三个条件应接收等价任务、材料版本、时间预算和验收说明。次序效应、学习效应和研究者经验必须在未来协议中处理。

## 3. Task Families（任务族）

- Literature Tasks（文献任务）：查找、比较、引用和冲突识别；
- Experiment Planning Tasks（实验规划任务）：变量、对照、步骤、风险和停止规则；
- Evidence Organization Tasks（证据整理任务）：来源、版本、过程、输出、失败和复核链组织。

任务定义来自 [`benchmark-design.md`](benchmark-design.md)，不得在观察结果后任意修改评分标准。

## 4. Metrics（指标）

| 指标 | 候选定义 | 防止误读 |
|---|---|---|
| Reproducibility（可复现性） | 独立复核者依据保存材料重建步骤并获得可比较结果的程度 | 可复现不等于结论正确 |
| Evidence Completeness（证据完整性） | 必需输入、过程、输出、版本、失败和限制字段的覆盖程度 | 完整不等于 Evidence 为真 |
| Traceability（可追溯性） | 结论候选能否回溯到来源、步骤、版本和复核决定 | 可追溯不等于因果有效 |
| Human Review Efficiency（人工复核效率） | 在复核质量不下降前提下完成复核所需的人类时间与操作量 | 更快不能以漏检错误为代价 |

具体量表、阈值、权重、样本量和统计分析尚未定义，必须在执行前预注册。

## 5. Minimum Procedure（最小程序）

1. 冻结任务、输入版本、允许工具和排除项；
2. 任命 Human Research Owner 与 Human Reviewer；
3. 完成数据、伦理、隐私和安全审查；
4. 预注册指标、评分规则、样本量、统计方法和停止规则；
5. 在隔离环境中运行三个条件；
6. 保存所有成功、失败、中间、冲突和人工修订记录；
7. 由 Reviewer 评分并处理分歧；
8. 由 Owner 决定接受、修订、拒绝或保持 `inconclusive`；
9. 另行决定是否允许任何外部发布。

这些步骤是 future requirements（未来要求），不是已开始的执行记录。

## 6. Bias and Confounders（偏差与混杂因素）

未来协议至少需要控制：

- 不同参与者的领域经验；
- 模型与工具版本变化；
- 任务次序和学习效应；
- 治理条件产生的额外记录成本；
- Reviewer 知道实验条件造成的评分偏差；
- 不同条件可访问材料或时间不等价；
- 医学影像任务中的隐私、伦理与临床语境误读。

## 7. Execution Gate（执行闸门）

```text
EXPERIMENT_PLAN_DEFINED=true
EXPERIMENT_PLAN_PREREGISTERED=false
DATA_ACCESS_APPROVED=false
ETHICS_REVIEW_STATUS=UNKNOWN
HUMAN_ROLES_ASSIGNED=false
AGENT_IMPLEMENTED=false
RUNTIME_CREATED=false
EXPERIMENT_AUTHORIZED=false
EXPERIMENT_EXECUTED=false
```

只有上述未完成项被独立解决并获得新的人工授权后，才能讨论执行。
