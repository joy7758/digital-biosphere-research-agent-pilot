---
document_id: DBRAP-MANUSCRIPT-OUTLINE-0.1
status: DRAFT_ONLY
experiment_records_bound: 0
results_section_populated: false
manuscript_draft_created: false
paper_submitted: false
paper_accepted: false
---

# Manuscript Outline v0.1（论文结构 v0.1）

> 当前只生成 Structure（结构）。没有真实 Experiment Record，因此 Results（结果）部分不得填入研究主张。

```text
AI Output ≠ Scientific Truth
Experiment Result ≠ Publication Claim
Draft Paper ≠ Accepted Paper
Paper Status = DRAFT_ONLY
```

## Title（标题）

候选标题必须在研究方法和结果可用后由 Human Research Owner 与人类作者确认。当前：`TO_BE_DETERMINED`。

## Abstract（摘要）

未来结构：Background、Objective、Methods、Results、Limitations、Conclusion。

当前不得生成 Results 或 Conclusion 文本，因为 Experiment Records、Evaluation Results 和 Analysis Report 均不存在。

## Introduction（引言）

未来说明科研工作流可复现性问题、Research Agent Governance（科研智能体治理）动机、研究问题和有界贡献。不得在引言中提前声称实验有效。

## Related Work（相关工作）

未来基于 Human-approved Source Documents，区分 Research Agent、AI Assistant、workflow reproducibility、evidence provenance（证据溯源）、human oversight 和 EOA 研究语境。当前 Context 来源为空，不生成综述结论。

## Methods（方法）

未来引用：

- Research Context Package；
- Human Context Review；
- Prototype Specification；
- Experiment Protocol；
- Evaluation Metrics；
- Research Evidence Model；
- DBOS/SAEE `PREPARED_ONLY` 边界。

清楚说明 Prototype 不是 Production Agent、Digital Entity 或 Runtime。

## Experiment（实验）

未来描述三个条件、四项任务、样本、分配、工具/模型版本、Human Review、Evidence Capture、偏差控制和停止规则。当前状态：`NOT_AUTHORIZED_NOT_EXECUTED`。

## Results（结果）

只允许引用真实 Experiment Records、Evidence Records、Verification Results 和 Evaluation Results。必须同时报告成功、失败、负面、Unknown、排除和 Protocol Deviation。

当前：`NO_RESULTS_AVAILABLE`。

## Discussion（讨论）

未来解释结果范围、可能机制、替代解释、治理成本、条件差异和对 Digital Biosphere Application Layer（数字生物圈应用层）的有限意义。不得把相关性写成因果或把 Pilot 写成普遍证明。

## Limitations（限制）

至少覆盖任务与样本范围、Paper 3 EOA 单一语境、模型/工具版本、Reviewer 偏差、测量有效性、外部验证、临床非适用性、DBOS/SAEE 未真实连接和 Prototype 非生产状态。

## Conclusion（结论）

只能由 Human Research Owner 基于最终 Analysis Report 形成。当前：`NOT_WRITTEN_NO_EXPERIMENT`。

## Evidence Requirements（证据要求）

| Manuscript Section | 必要事实来源 |
|---|---|
| Related Work | Approved Source Documents 与 Literature Task Records |
| Methods | 冻结 Protocol、Prototype、Metrics、Context 和 Evidence Plan |
| Experiment | Experiment Records 与 Protocol Deviations |
| Results | Evaluation Results 与 Evidence References |
| Discussion | Analysis Report、Failures、Negative Results 与 Unknowns |
| Conclusion | Human Research Owner 审查决定 |

任何缺失来源必须保持 Unknown 或留空，不得由 AI 补写。

## Authorship and Publication Boundary（署名与发表边界）

- 不自动署名；
- 不自主决定作者顺序或 CRediT（贡献者角色分类）声明；
- 不自动投稿、发表或对外发送；
- Draft 不等于 Submitted、Accepted 或 Published；
- Human Research Owner 与人类作者保留最终责任。

## Current Paper State（当前论文状态）

```text
MANUSCRIPT_OUTLINE_DEFINED=true
MANUSCRIPT_DRAFT_CREATED=false
EXPERIMENT_RECORDS_BOUND=0
RESULTS_SECTION_POPULATED=false
Paper Status = DRAFT_ONLY
SUBMISSION_STATUS=NOT_SUBMITTED
ACCEPTANCE_STATUS=NOT_ACCEPTED
PUBLICATION_STATUS=NOT_PUBLISHED
```
