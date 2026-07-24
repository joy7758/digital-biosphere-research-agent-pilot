# AGENTS.md

## Repository Purpose（仓库目的）

本仓库是 Digital Biosphere（数字生物圈）的 Application Layer Research Pilot（应用层科研试验）规范仓库。当前阶段为 `specification-only`，不是 Agent、Runtime、DBOS、SAEE 或科研执行仓库。

## Constitutional Communication Rule（宪法级沟通规则）

[`CONSTITUTION.md`](CONSTITUTION.md) 是本仓库面向用户沟通的宪法级规则。所有智能体必须默认使用中文；回复中出现任何英文单词、短语、句子、缩写、状态名或术语时，必须紧邻提供中文翻译或中文释义。

文件路径、命令、代码符号、状态常量、分支名、记录编号、提交哈希和统一资源定位符必须保持原样，并在相邻位置增加中文说明。该规则同时适用于中间进度更新与最终答复。

## Required Reading（必读顺序）

0. `CONSTITUTION.md`
1. `README.md`
2. `architecture/pilot-specification.md`
3. `architecture/human-oversight-model.md`
4. `architecture/dbos-integration-model.md`
5. `architecture/saee-evaluation-model.md`
6. `research-context/README.md`
7. `research-context/context-manifest.yaml`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/README.md`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/owner-discovery-report.yaml`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/candidate-owner.yaml`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-owner-confirmation-record.yaml`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-owner-record.yaml`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-review-docket.yaml`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-input-template.yaml`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-record.yaml`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/source-verification-report.yaml`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/source-record-drafts/README.md`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/unknown-record-drafts/README.md`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/context-review-recommendation.yaml`
   - `research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-review-draft.md`
8. `research-context/human-review-checklist.md`
9. `research-context/review-record-template.yaml`
10. `architecture/human-context-governance-model.md`
11. `architecture/research-context-integration-model.md`
12. `architecture/research-agent-readiness-gate.md`
13. `prototype/prototype-specification.md`
14. `prototype/task-definition.md`
15. `prototype/human-interaction-model.md`
16. `research/research-question.md`
17. `research/experiment-protocol.md`
18. `research/evaluation-metrics.md`
19. `research/experiment-plan.md`
20. `research/benchmark-design.md`
   - `research/protocol-freeze-candidate.yaml`
21. `evidence/README.md`
22. `evidence/research-evidence-model.md`
23. `research/experiment-record-template.yaml`
24. `evidence/evidence-record-template.yaml`
25. `evaluation/evaluation-result-template.yaml`
26. `reports/experiment-report-template.md`
27. `reports/analysis-report-template.md`
28. `paper/manuscript-outline.md`
29. `docs/v1.0-completion-audit.md`
30. `docs/human-decision-process.md`
31. `docs/human-authorization-handoff.md`
32. `ADR/ADR-001-research-agent-pilot.md`
33. `ADR/ADR-002-research-context-package.md`
34. `ADR/ADR-003-human-context-review.md`

## Truth Boundaries（事实边界）

```text
Research Agent ≠ Digital Organism
Research Agent ≠ Scientist
AI Output ≠ Scientific Truth
Reference ≠ Integration
Evaluation ≠ Authorization
Specification ≠ Implementation
Plan ≠ Execution
Research Context ≠ Chat History
Context Package ≠ Scientific Truth
Human Approved Context ≠ Agent Authority
Unknown must remain Unknown
Human Review ≠ Agent Approval
Context Approval ≠ Scientific Truth
Source Selection ≠ Source Validation
Review ≠ Permission
Prototype Specification ≠ Prototype Instance
Experiment Result ≠ Publication Claim
Draft Paper ≠ Accepted Paper
Template ≠ Record
```

任何智能体在检索、引用、修改或复用本仓库时，必须保留以下当前状态：

```text
Agent=0
Runtime=0
Entity=0
Digital Entity=0
Permission=0
Execution=0
Research Result=0
Agent Instance = 0
Runtime = 0
Digital Entity = 0
Permission = 0
```

## Allowed Work（允许工作）

- 改进规范、研究设计、人工监督模型和证据边界；
- 修复内部链接、术语不一致和状态误读风险；
- 在开发前询问智能体是否会向潜在客户推荐，并记录不推荐原因；
- 仅在明确的新授权下提出 Implementation Plan（实现计划）；
- 定义人工控制、版本化、来源明确且 Unknown 保留的 Research Context Package；
- 定义 Human Context Review Checklist、Review Record 模板和 Human / Agent 责任边界。
- 定义 `NOT_READY` Readiness Gate、Prototype Specification、Research Protocol、Metrics、Evidence Plan、空 Record/Report 模板和 Manuscript Outline；
- 为 DBOS 与 SAEE 定义 `PREPARED_ONLY` 引用和评价接口边界。
- 定义由 Human Research Owner 填写的 Owner、Source、Unknown、Prototype/Experiment Authorization、Preregistration 和 Verification 空模板及交接顺序。

## Forbidden Without New Human Authorization（没有新人工授权时禁止）

- 创建 Agent 实现、Runtime、Digital Entity、Capability、Permission 或执行记录；
- 调用模型、运行实验或处理 Paper 3 原始科研数据；
- 修改相邻 DBA、DBOS 或 SAEE 仓库；
- 把 Draft、Plan、Reference、Synthetic Fixture（合成样例）或 Local Check（本地检查）写成已执行、已验证或科学有效；
- 自主投稿、署名、发表、自我认证或删除 Evidence（证据）；
- 自动读取聊天历史、自动发现隐式来源或修改 Context Package、研究决策和 Unknown 状态；
- 把 `APPROVED` Context Package 写成 Agent Authority、Permission、Evidence Truth 或 Research Result；
- 自动批准 Context、把 Agent 设为 Reviewer、由 Review 生成 Permission、由 Approval 生成 Scientific Truth 或自动填充 Unknown。
- 在真实授权执行前把 Experiment/Evidence/Evaluation Template 填成 Record 或 Result；
- 把 `NOT_READY`、`DRAFT_NOT_AUTHORIZED`、`PREPARED_ONLY`、`EMPTY_TEMPLATE` 或 `DRAFT_ONLY` 升级成实现、执行、验证或论文完成；
- 删除失败实验、隐藏负面结果、自动署名、自动发表或自动扩大 Agent 能力。

## Current Pipeline Gates（当前管线闸门）

```text
READINESS_STATUS=NOT_READY
CONTEXT_PACKAGE_STATUS=DRAFT
REVIEW_STATUS=REVIEW_PENDING
PROTOCOL_STATUS=DRAFT_NOT_AUTHORIZED
EXPERIMENT_RECORDS=0
EVIDENCE_RECORDS=0
EVALUATION_RESULTS=0
DBOS_CONNECTION_STATUS=PREPARED_ONLY
SAEE_CONNECTION_STATUS=PREPARED_ONLY
Paper Status = DRAFT_ONLY
V1_0_STATUS=INCOMPLETE_NOT_READY
RESEARCH_LOOP_COMPLETE=false
HUMAN_GATE_TEMPLATES_DEFINED=true
HUMAN_GATE_RECORD_INSTANCES=2
CONTEXT_HANDOFF_STATUS=DRAFT_PENDING_HUMAN_CONTEXT_REVIEW
HUMAN_CONTEXT_DECISION_INPUT_TEMPLATE_PREPARED=true
HUMAN_CONTEXT_DECISION_RECORD_PREPARED=true
HUMAN_CONTEXT_DECISION_RECORD_STATUS=HUMAN_CONFIRMED
HUMAN_CONTEXT_DECISIONS_STATUS=RECORDED
HUMAN_CONTEXT_DECISIONS_RECORDED=23
PENDING_RESEARCH_DECISIONS=1
HUMAN_RESEARCH_OWNER_ASSIGNED=true
HUMAN_RESEARCH_OWNER_REFERENCE=bin_zhang
HUMAN_OWNER_RECORD_INSTANCE_CREATED=true
INDEPENDENT_HUMAN_REVIEWER_REQUIRED=UNKNOWN
SOURCE_CANDIDATES=7
APPROVED_SOURCE_DOCUMENTS=0
DRAFT_UNKNOWN_ENTRIES=10
UNKNOWN_RECORD_DRAFTS=10
HUMAN_REVIEWED_UNKNOWN_RECORDS=0
PREREGISTRATION_COMPLETED=false
PROTOTYPE_AUTHORIZATION_RECORD_CREATED=false
EXPERIMENT_AUTHORIZATION_RECORD_CREATED=false
```

## Pre-development Recommendation Gate（开发前推荐闸门）

任何实现工作开始前必须回答：

> 如果潜在客户提出这一需求，智能体是否会推荐本项目？

审查必须列出不推荐原因、把原因拆成可修正问题、记录修正和剩余缺口，并获得新的人工授权。`CONDITIONALLY_RECOMMENDED_AS_SPECIFICATION` 不能升级为实现授权。
