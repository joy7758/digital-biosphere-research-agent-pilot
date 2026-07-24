---
adr_id: ADR-002
title: Adopt a Controlled Research Context Package
status: accepted-for-specification
date: 2026-07-21
package_status: DRAFT
implementation_authorized: false
---

# ADR-002: Controlled Research Context Package（受控研究上下文包）

## Status（状态）

`accepted-for-specification`：接受 Research Context Package v0.1 的结构与治理规则，不表示 Package 已经人工批准、Agent 已创建或科研任务已授权。

## Context（背景）

未来 Research Agent 需要研究背景、已确认研究决策、Evidence Reference、来源和 Unknown，才能在明确边界内辅助科研。如果直接使用完整 Chat History（聊天历史）、浏览历史或隐式模型记忆，来源范围、版本、人工确认、冲突和删除状态都难以审计。

“模型见过某段内容”不能替代“Human Research Owner 明确选择并批准某个版本的研究上下文”。

## Decision（决定）

采用独立、版本化、人工控制的 Research Context Package：

- 使用 `context-manifest.yaml` 作为 Package 入口；
- 只允许显式登记的 `source_documents`；
- 使用研究决策记录区分已确认决定与一般背景；
- 只引用 Evidence，不产生 Evidence Truth；
- 显式保留 Unknown、冲突、缺失和不可验证状态；
- 只允许未来 Agent 只读使用 `APPROVED` 版本；
- 任何修改都由 Human Research Owner 创建新版本并重新复核。

## Invariants（不变量）

```text
Research Context ≠ Chat History
Context Package ≠ Scientific Truth
Human Approved Context ≠ Agent Authority
Unknown must remain Unknown
AGENT_CONTEXT_WRITE_ALLOWED=false
```

## Alternatives Considered（考虑过的替代方案）

### Use Complete Chat History（使用完整聊天历史）

拒绝。聊天历史包含临时推理、重复内容、过期状态、未经确认的建议和可能不属于当前研究范围的信息，不能作为隐式事实真源。

### Let the Agent Build Its Own Context（让 Agent 自建上下文）

拒绝。Agent 自选来源并确认自身输入会混淆辅助者、来源管理者和批准者，也会使 Unknown 被概率性补全。

### Store Context Only in Prompts（只在提示中保存上下文）

拒绝。Prompt（提示）缺少稳定标识、版本、来源清单、生命周期、人工批准和归档边界。

### Put the Package in DBOS, SAEE, or DBA（把包放入 DBOS、SAEE 或 DBA）

拒绝。该 Package 是 Research Agent Pilot 的应用层研究初始化输入。DBOS 不是研究背景 Owner，SAEE 不负责选择研究上下文，DBA 不承载具体应用实验的 Context 实例。

## Consequences（后果）

正面后果：

- Future Agent（未来智能体）的初始化输入可定位、可版本化、可复核；
- Chat History 与正式 Research Context 被清楚分开；
- Unknown、冲突和限制不会因自动摘要而消失；
- Agent、Human、DBOS 和 SAEE 的职责保持分离。

代价与限制：

- Human Research Owner 需要维护来源、版本和批准记录；
- `APPROVED` Package 仍可能不完整或包含错误，必须接受持续复核；
- 本规范不提供 Agent、Runtime、Schema Validator（模式验证器）或自动加载器。

## Current Decision Boundary（当前决定边界）

```text
CONTEXT_PACKAGE_SPECIFICATION_ACCEPTED=true
CONTEXT_PACKAGE_STATUS=DRAFT
CHAT_HISTORY_CAPTURED=false
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
