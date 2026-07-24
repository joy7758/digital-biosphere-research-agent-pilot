---
adr_id: ADR-003
title: Require Human Review Before Context Approval
status: accepted-for-specification
date: 2026-07-21
review_executed: false
context_approved: false
implementation_authorized: false
---

# ADR-003: Human Context Review（人工研究上下文复核）

## Status（状态）

`accepted-for-specification`：接受 Human Context Review Checklist v0.1 的结构和治理规则，不表示 Context Review 已执行或 Context Package 已批准。

## Context（背景）

Research Context Package Specification v0.1 已定义什么类型的背景、来源、研究决策、Evidence Reference（证据引用）和 Unknown 可以进入未来 Context。当前 Manifest 仍是 `DRAFT`，`owner_reference: null`、`source_documents: []`、`approved_by: []`。

只有准入结构而没有 Human Review，无法回答以下问题：谁承担研究责任、研究范围是什么、每项来源是否可定位、限制是否披露、Unknown 是否保留，以及未来 AI 辅助边界是否明确。

## Decision（决定）

在 Context Package 可以进入 `APPROVED` 之前，要求使用版本化 Human Context Review Checklist，并产生由人类负责的 Review Record。

Review 必须覆盖：

- Research Ownership（研究所有权）；
- Research Scope（研究范围）；
- Source Review（来源复核）；
- Unknown Review（未知项复核）；
- AI Usage Boundary（人工智能使用边界）；
- Approval Decision（批准决定）。

最终 `APPROVED` Review 只能由 Human Research Owner 明确作出。Review Record 不自动更新 Context Manifest，也不创建 Agent、Permission、Execution、Evidence Truth 或 Scientific Truth。

## Invariants（不变量）

```text
Human Review ≠ Agent Approval
Context Approval ≠ Scientific Truth
Source Selection ≠ Source Validation
Unknown must remain Unknown
REVIEW_NE_PERMISSION=true
AGENT_NE_REVIEWER=true
```

## Alternatives Considered（考虑过的替代方案）

### Automatic Context Approval（自动批准上下文）

拒绝。结构完整、链接通过或字段存在不能替代对研究责任、来源、限制和风险的人工判断。

### Agent Self-review（Agent 自我复核）

拒绝。让未来 Agent 选择并批准自己的上下文会混淆输入使用者、Reviewer 和 Authority（权力主体），并产生 Self Certification（自我认证）风险。

### Treat Source Selection as Validation（把来源选择当作来源验证）

拒绝。来源被选择只表示它进入审查范围，不证明版本正确、方法有效、结论真实或适用于当前研究。

### Approve Context Through an Unrecorded Conversation（通过未记录对话批准上下文）

拒绝。无法稳定定位 Reviewer、版本、批准来源、Unknown、异议和时间，也容易把 Chat History 误当作规范记录。

## Consequences（后果）

正面后果：

- Context Approval 具有明确的人类责任和可审查记录；
- 来源选择、来源验证、科学结论和 Agent Permission 保持分离；
- Unknown、限制、冲突和拒绝决定得到保留；
- Future Research Agent 不能成为自身 Context 的批准者。

代价与限制：

- Human Research Owner 与 Reviewer 需要完成并维护复核记录；
- Review 会增加进入下一阶段前的工作量；
- Checklist 完成也不能证明 Context 内容正确或研究设计有效；
- 本决策不创建自动 Reviewer、状态机、Agent 或访问控制实现。

## Current Decision Boundary（当前决定边界）

```text
HUMAN_CONTEXT_REVIEW_SPECIFICATION_ACCEPTED=true
HUMAN_CONTEXT_REVIEW_EXECUTED=false
REVIEW_RECORD_INSTANCE_CREATED=false
REVIEW_STATUS=REVIEW_PENDING
CONTEXT_PACKAGE_STATUS=DRAFT
Agent=0
Runtime=0
Entity=0
Permission=0
Execution=0
Research Result=0
DBOS_MODIFIED=false
SAEE_MODIFIED=false
DBA_MODIFIED=false
```
