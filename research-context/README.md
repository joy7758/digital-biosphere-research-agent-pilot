---
spec_id: DBRAP-RESEARCH-CONTEXT-PACKAGE-0.1
title: Research Context Package Specification v0.1
status: specification-only
package_status: DRAFT
chat_history_imported: false
agent_instance_created: false
research_result_created: false
---

# Research Context Package Specification v0.1（研究上下文初始化包规范 v0.1）

## 1. Purpose（目的）

Research Context Package（研究上下文包）是未来 Research Agent（科研智能体）进入科研流程前，由 Human Research Owner（人类研究负责人）选择、组织和确认的受控研究背景入口。

它回答“未来 Research Agent 开始辅助前需要看到什么”，不回答研究问题，不抓取历史对话，不创建 Agent，也不授予执行或修改权。

当前目录只定义 Package Structure（包结构）、来源规则、研究决策模板、Evidence Reference（证据引用）边界、Unknown（未知项）保留规则和未来使用流程。

## 2. Core Principles（核心原则）

```text
Research Context ≠ Chat History
Context Package ≠ Scientific Truth
Human Approved Context ≠ Agent Authority
Unknown must remain Unknown
```

这些原则意味着：

- Research Context（研究上下文）只能来自清单中显式列出的受控来源，不能从聊天记录、浏览历史或个人记忆自动聚合；
- Package 的 `APPROVED` 只表示 Human Research Owner 已确认它可作为特定研究任务的输入，不表示内容正确、完整或支持科学结论；
- 人工确认不创建 Capability、Permission、Runtime、Entity 或执行授权；
- 缺失、冲突、不可验证或未决定的信息必须显式保留为 Unknown，不能由 Agent 猜测补全。

## 3. Package Contents（包内容）

| 路径 | 作用 | 当前状态 |
|---|---|---|
| [`context-manifest.yaml`](context-manifest.yaml) | Package 标识、版本、来源、Owner、批准者和状态入口 | `DRAFT`；来源与批准者为空 |
| [`handoffs/paper-3-eoa-human-owner-context-v0.1/README.md`](handoffs/paper-3-eoa-human-owner-context-v0.1/README.md) | Paper 3 EOA 的 Human Research Owner Context Handoff 草案入口 | Owner 已 `ASSIGNED`；`DRAFT_PENDING_HUMAN_CONTEXT_REVIEW`，不是 Approved Context |
| [`handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-input-template.yaml`](handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-input-template.yaml) | 原 7 个来源、4 项研究决定、10 个 Unknown、AI 边界与复核意图的统一人工输入面 | 所有决定为 `null`；Template 不是 Review Record |
| [`handoffs/paper-3-eoa-human-owner-context-v0.1/human-source-decision-addendum-v0.1.yaml`](handoffs/paper-3-eoa-human-owner-context-v0.1/human-source-decision-addendum-v0.1.yaml) | 新增 DBA / SAEE / DBO 三项来源的零预选人工决定输入面 | 所有决定为 `null`；Template 不是 Decision Record |
| [`handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-record.yaml`](handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-record.yaml) | 固定 `HCD-001` 的人工上下文决策记录 | `HUMAN_CONFIRMED`；23 个决定条目已记录，仍待 Human Review |
| [`handoffs/paper-3-eoa-human-owner-context-v0.1/unknown-record-drafts/README.md`](handoffs/paper-3-eoa-human-owner-context-v0.1/unknown-record-drafts/README.md) | 10 个逐项 Unknown Record Draft 的人工复核入口 | `DRAFT_NOT_HUMAN_REVIEWED`；正式 Record `0` |
| [`project-background.md`](project-background.md) | Research Agent Pilot 背景与 DBA / DBOS / SAEE 分层 | 已定义；不是 Scientific Truth |
| [`human-owner-record-template.yaml`](human-owner-record-template.yaml) | Human Research Owner 责任、冲突和科学决定责任的空记录结构 | `UNASSIGNED`；不是 Owner 任命 |
| [`human-review-checklist.md`](human-review-checklist.md) | Human Research Owner 对所有权、范围、来源、Unknown 和 AI 边界的复核清单 | 模板；尚未执行 |
| [`review-record-template.yaml`](review-record-template.yaml) | 未来 Human Review Record 的字段与状态模板 | `REVIEW_PENDING`；不是 Review Record 实例 |
| [`research-decisions/decision-template.yaml`](research-decisions/decision-template.yaml) | 未来已确认研究决策的记录模板 | 模板；不是 Decision Record（决策记录）实例 |
| [`evidence/README.md`](evidence/README.md) | 未来 Evidence Reference 类型与零证据边界 | 当前不生成 Evidence |
| [`references/README.md`](references/README.md) | 来源准入、版本、引用和聊天历史排除规则 | 当前没有已纳入来源 |
| [`unknowns/README.md`](unknowns/README.md) | Unknown 事项和禁止自动补全规则 | 示例存在；不是已验证事实 |

`context_id` 是 Package-local Identifier（包内标识符），不是 DBOS `entity_id`、Agent Identity（智能体身份）或 Permission Source（权限来源）。

## 4. Human Review Requirement（人工复核要求）

Context Package 从 `DRAFT` 进入 `REVIEWED` 或 `APPROVED` 前，必须使用 [`human-review-checklist.md`](human-review-checklist.md) 完成明确的人类复核，并基于 [`review-record-template.yaml`](review-record-template.yaml) 建立独立 Review Record。

```text
Human Review ≠ Agent Approval
Context Approval ≠ Scientific Truth
Source Selection ≠ Source Validation
Review ≠ Permission
```

Review Record 的状态不自动改写 Context Manifest。Human Research Owner 必须核对 `context_id`、`version`、来源、Unknown、限制与决定后，分别执行人工状态变更。当前没有执行 Review，也没有创建 Review Record 实例。

关系模型见 [`../architecture/human-context-governance-model.md`](../architecture/human-context-governance-model.md)，决策理由见 [`../ADR/ADR-003-human-context-review.md`](../ADR/ADR-003-human-context-review.md)。

## 5. Lifecycle（生命周期）

| 状态 | 含义 | 谁可以推进 | 不表示 |
|---|---|---|---|
| `DRAFT` | 正在组织内容，来源和 Unknown 可能不完整 | Human Research Owner | 可被 Agent 使用 |
| `REVIEWED` | Human Reviewer（人类复核者）已检查结构、来源、决策和 Unknown | 明确的 Human Reviewer | 内容为 Scientific Truth |
| `APPROVED` | Human Research Owner 已确认该版本可作为指定任务的上下文输入 | Human Research Owner | Agent Authority、Permission 或实验授权 |
| `ARCHIVED` | 该版本停止作为活动上下文使用，但应保留历史 | Human Research Owner | 可以删除或改写历史 |

允许的人工控制流为：

```text
DRAFT -> REVIEWED -> APPROVED -> ARCHIVED
```

复核发现问题时可以返回新的 `DRAFT` 版本。Agent 不得改变任何状态。

## 6. Source Management Rules（来源管理规则）

未来加入 `source_documents` 的来源必须：

1. 由 Human Research Owner 明确选择，而不是自动发现或自动导入；
2. 记录稳定引用、来源类型、版本或日期、访问限制和复核状态；
3. 区分原始来源、派生摘要和人工决策；
4. 保留冲突来源，不以多数文本自动消除冲突；
5. 在来源失效、版本漂移或访问权限不明时记录 Unknown；
6. 不把聊天历史、浏览历史、模型记忆或未声明工作区扫描作为隐含来源；
7. 不因来源进入 `APPROVED` Package 就把它升级为 Evidence Truth。

当前 Handoff 已列出并核验 10 个 source candidates（来源候选）：原 7 个已有人工选择记录，新增 DBA / SAEE / DBO 三项仍待人工决定；canonical Manifest 仍为 `source_documents: []`，表示尚未纳入任何受审来源。Candidate verification（候选核验）不产生 Source Approval（来源批准）或 Context Binding（上下文绑定）。

未来 Source Record（来源记录）必须从 [`references/source-document-template.yaml`](references/source-document-template.yaml) 创建独立实例，不能直接把模板路径当作来源。Unknown Record（未知事项记录）必须从 [`unknowns/unknown-record-template.yaml`](unknowns/unknown-record-template.yaml) 创建独立实例；模板的 `OPEN` 不代表已登记真实 Unknown。

## 7. Change Control（变更控制）

- Agent 对 Package 只有未来的 read-only consumption（只读使用）资格，而且仅限另行授权的 `APPROVED` 版本；
- Agent 发现缺失、冲突或过期信息时，只能提交 Change Request（变更请求）或 Unknown Report（未知报告）；
- Human Research Owner 决定是否创建新版本；
- 已批准或已归档版本不得原地重写；
- 研究决策只能由人类确认、替代或撤销，Agent 不能修改 Decision Status（决策状态）；
- Package 变更不自动传播到 DBA、DBOS 或 SAEE。

## 8. Prohibited Automation（禁止的自动化）

- 自动读取、整理或摘要历史聊天记录；
- 自动创建 Research Agent、Runtime 或 Entity；
- 自动生成 Research Result（研究结果）；
- 自动产生 Evidence Truth；
- 自动修改研究决策、批准者或 Package 状态；
- 自动批准 Context、把 Agent 指定为 Reviewer 或由 Review 生成 Permission；
- 把 Approval 解释为 Scientific Truth；
- 自动调用模型、运行论文实验或写入外部系统。

## 9. Current State（当前状态）

```text
RESEARCH_CONTEXT_PACKAGE_SPECIFICATION_DEFINED=true
CONTEXT_PACKAGE_STATUS=DRAFT
CONTEXT_HANDOFF_STATUS=DRAFT_PENDING_HUMAN_CONTEXT_REVIEW
CONTEXT_HANDOFF_DRAFT_PREPARED=true
OWNER_CANDIDATES_DISCOVERED=1
OWNER_CANDIDATE_STATUS=CONFIRMED_AND_ASSIGNED
OWNER_DISCOVERY_CONFIDENCE=MEDIUM
OWNER_CONFIRMATION_REQUIRED=false
HUMAN_RESEARCH_OWNER_ASSIGNED=true
HUMAN_RESEARCH_OWNER_REFERENCE=bin_zhang
INDEPENDENT_HUMAN_REVIEWER_REQUIRED=UNKNOWN
SOURCE_CANDIDATES=10
SOURCE_CANDIDATES_VERIFIED_FOR_HUMAN_REVIEW=10
SOURCE_CANDIDATES_PENDING_VERIFICATION=0
SOURCE_DOCUMENTS=0
APPROVED_BY=0
CHAT_HISTORY_IMPORTED=false
HUMAN_CONTEXT_REVIEW_CHECKLIST_DEFINED=true
HUMAN_CONTEXT_REVIEW_EXECUTED=false
REVIEW_RECORD_INSTANCE_CREATED=false
REVIEW_STATUS=REVIEW_PENDING
HUMAN_OWNER_RECORD_TEMPLATE_DEFINED=true
HUMAN_OWNER_RECORD_INSTANCE_CREATED=true
SOURCE_RECORD_TEMPLATE_DEFINED=true
SOURCE_RECORD_INSTANCES=0
UNKNOWN_RECORD_TEMPLATE_DEFINED=true
DRAFT_UNKNOWN_ENTRIES=10
HUMAN_REVIEWED_UNKNOWN_RECORDS=0
UNKNOWN_RECORD_INSTANCES=0
Agent=0
Runtime=0
Entity=0
Permission=0
Execution=0
Research Result=0
```

目录和模板存在只证明规范已建立，不证明 Package 已复核、已批准、已被 Agent 使用或已经产生研究结果。
