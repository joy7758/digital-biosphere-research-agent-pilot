---
protocol_id: DBRAP-EXPERIMENT-PROTOCOL-0.1
title: Governed Research Agent Comparative Experiment Protocol v0.1
status: DRAFT_NOT_AUTHORIZED
preregistered: false
human_owner_approved: false
experiment_executed: false
experiment_records_created: 0
---

# Governed Research Agent Comparative Experiment Protocol v0.1（受治理科研智能体比较实验协议 v0.1）

## 1. Protocol Status（协议状态）

本文件是 Research Protocol（研究协议）草案。它尚未预注册、尚未由 Human Research Owner 批准，也没有触发模型调用、参与者招募、数据访问或实验执行。

```text
PROTOCOL_STATUS=DRAFT_NOT_AUTHORIZED
PREREGISTERED=false
EXPERIMENT_AUTHORIZED=false
EXPERIMENT_EXECUTED=false
```

## 2. Research Question（研究问题）

> Can a governed Research Agent improve reproducibility of scientific workflows?
>
> 受治理科研智能体是否可以提升科研流程可复现性？

“improve”必须由预注册指标和跨条件比较支持，不能用“AI 更聪明”或主观偏好替代。

## 3. Study Objective（研究目标）

在冻结相同任务、来源、时间预算和 Human Review 要求的条件下，比较三种工作流在 Reproducibility（可复现性）及五个次要指标上的差异。

任何观察仅是 bounded pilot result（有界试验结果），不能自动推广到其他科研领域、临床实践、生产系统或 Digital Organism。

## 4. Experimental Conditions（实验条件）

### Baseline A: Human-only Workflow（纯人工工作流）

人类研究者使用批准的来源和常规工具完成任务。必须记录工具、步骤、时间、人工判断、失败和 Unknown，不能以较少日志作为默认优势或劣势。

### Baseline B: Generic AI Assistant Workflow（通用人工智能助手工作流）

人类研究者使用固定且明确版本的通用 AI Assistant（人工智能助手）完成相同任务。必须冻结模型、界面、提示、工具、访问范围和人工干预；AI Output 仍需 Human Review。

### Baseline C: Governed Research Agent Workflow（受治理科研智能体工作流）

未来 Prototype 在受控 Context、Task Boundary、Evidence Plan、Human Oversight 和停止规则下辅助相同任务。该条件只有在 Readiness Gate、Prototype Authorization 和 Experiment Authorization 均通过后才能建立。

```text
Baseline C Specification ≠ Baseline C Instance
Governance Presence ≠ Better Outcome
```

## 5. Research Tasks（科研任务）

四项任务由 [`../prototype/task-definition.md`](../prototype/task-definition.md) 定义：

1. Literature Review；
2. Benchmark Design；
3. Experiment Planning；
4. Draft Organization。

执行前必须把每项任务冻结为明确 `task_id`、版本、输入、输出、时间预算、停止条件和 Review Rubric。当前 Task Definitions 已定义但来源未绑定、案例未冻结。

## 6. Experimental Unit and Sampling（实验单元与抽样）

候选 Experimental Unit（实验单元）是“一个条件在一个冻结 Task Case（任务案例）上的一次受控工作流”。样本量、重复次数、参与者构成、随机化、Counterbalancing（顺序平衡）和排除标准当前为 `UNKNOWN`，必须在预注册前由 Human Research Owner 与方法 Reviewer 决定。

不得根据初步结果动态选择样本量或删除不利单元。

## 7. Controlled Inputs（受控输入）

三个条件必须使用可比较的：

- Research Context 版本；
- Source Document 集合；
- Task Case 与验收说明；
- 时间和资源预算；
- 可用工具和访问边界；
- Human Review Rubric；
- Evidence Capture 要求；
- 停止与拒绝规则。

任何实际差异必须预注册或记录为 Protocol Deviation（协议偏差）。

## 8. Procedure（程序）

1. Human Research Owner 冻结 Protocol、Context、Task、Metrics 和 Evidence Plan；
2. Human Reviewer 检查来源、Unknown、风险、比较公平性和记录要求；
3. 记录独立 Experiment Authorization；
4. 为每个条件创建新的 Experiment Record，禁止预填结果；
5. 按预注册顺序执行任务并保存 Input、Action、Human Review、Output 和 Failure；
6. Reviewer 在不知道不必要条件信息的情况下按冻结 Rubric 评分；
7. 保存分歧、修改、拒绝、负面和 `INCONCLUSIVE` 结果；
8. 仅在 Evidence 与 Verification 完成后计算 Evaluation Metrics；
9. Human Research Owner 审查 Analysis Report，决定科学解释是否仍为 `INCONCLUSIVE`；
10. 论文相关输出进入独立 Draft 与 Publication Gate。

当前停在步骤 1 之前，因为 Owner、Context、Sources 和 Authorization 均未满足。

## 9. Evaluation（评价）

Primary Metric（主要指标）和 Secondary Metrics（次要指标）由 [`evaluation-metrics.md`](evaluation-metrics.md) 定义。任何阈值、权重、聚合方式、统计检验、多重比较和缺失值处理必须在执行前预注册。

主观“AI 更聪明”、语言更流畅或偏好评分不得作为成功指标。

## 10. Evidence and Records（证据与记录）

- Experiment Record 模板：[`experiment-record-template.yaml`](experiment-record-template.yaml)；
- Evidence Flow：[`../evidence/research-evidence-model.md`](../evidence/research-evidence-model.md)；
- Evidence Record 模板：[`../evidence/evidence-record-template.yaml`](../evidence/evidence-record-template.yaml)；
- Evaluation Result 模板：[`../evaluation/evaluation-result-template.yaml`](../evaluation/evaluation-result-template.yaml)。
- Verification Result 模板：[`../evidence/verification-result-template.yaml`](../evidence/verification-result-template.yaml)；
- Preregistration Checklist：[`preregistration-checklist.md`](preregistration-checklist.md)；
- Experiment Authorization 模板：[`experiment-authorization-template.yaml`](experiment-authorization-template.yaml)。

模板不是 Record。只有真实授权执行产生的不可追溯伪造之外的材料才能成为 Record 候选。

## 11. Failure, Negative, and Unknown Preservation（失败、负面与未知保留）

必须保留：

- Tool、Model、Human 或环境失败；
- Agent 拒绝和停止；
- Reviewer 拒绝、修改和分歧；
- 对主要或次要指标无改善的结果；
- 相反方向结果；
- 缺失、不可比较、Protocol Deviation 和 Unknown；
- 无法形成结论的 `INCONCLUSIVE` 分析。

不得删除失败实验、隐藏负面结果或只选择支持预期叙事的 Record。

## 12. Safety and Stop Rules（安全与停止规则）

遇到以下情况必须停止相关单元并保留记录：

- Context、Owner、Source、Permission 或 Authorization 无法解析；
- 原始数据修改、Evidence 删除、外部提交或发表请求；
- 医学诊断、临床决定或未经批准的敏感数据访问；
- 模型、工具、任务或环境版本偏离 Protocol；
- 无法保留失败、Unknown、人工修改或来源链；
- 参与者安全、隐私、伦理或科学完整性风险超出批准范围。

## 13. Preregistration Requirements（预注册要求）

执行前仍需由人类明确：

- Owner、Reviewer 与角色冲突；
- 来源、数据、伦理和隐私批准；
- Task Cases、样本量和重复次数；
- 随机化、盲法或其不可行性；
- Metric 计算、阈值、统计方法和缺失值处理；
- Protocol Deviation 和停止决策规则；
- 记录保存位置、访问控制和保留期；
- Prototype、模型、工具和环境版本；
- Experiment Authorization 与撤销方法。

## 14. Current State（当前状态）

```text
RESEARCH_PROTOCOL_DEFINED=true
PROTOCOL_STATUS=DRAFT_NOT_AUTHORIZED
PREREGISTERED=false
HUMAN_RESEARCH_OWNER_ASSIGNED=true
HUMAN_RESEARCH_OWNER_REFERENCE=bin_zhang
INDEPENDENT_HUMAN_REVIEWER_REQUIRED=UNKNOWN
PREREGISTRATION_CHECKLIST_DEFINED=true
EXPERIMENT_AUTHORIZATION_TEMPLATE_DEFINED=true
EXPERIMENT_AUTHORIZATION_RECORD_CREATED=false
EXPERIMENT_AUTHORIZED=false
EXPERIMENT_RECORDS_CREATED=0
EXPERIMENT_EXECUTED=false
ANALYSIS_COMPLETED=false
SCIENTIFIC_CONCLUSION=NONE
```
