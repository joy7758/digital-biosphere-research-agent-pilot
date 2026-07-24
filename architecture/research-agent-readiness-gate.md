---
gate_id: DBRAP-RESEARCH-AGENT-READINESS-0.1
title: Research Agent Prototype Readiness Gate v0.1
status: NOT_READY
evaluated_on: 2026-07-21
prototype_creation_authorized: false
agent_instance_created: false
runtime_created: false
digital_entity_created: false
permission_granted: false
context_handoff_status: DRAFT_PENDING_HUMAN_CONTEXT_REVIEW
---

# Research Agent Prototype Readiness Gate v0.1（科研智能体原型就绪闸门 v0.1）

## 1. Purpose（目的）

本 Gate（闸门）判断 `digital-biosphere-research-agent-pilot` 是否具备进入最小 Research Agent Prototype（科研智能体原型）创建审查的前提。它不创建 Prototype、Agent Instance（智能体实例）、Runtime、Digital Entity 或 Permission，也不授权实验。

当前结论基于仓库中的可检查事实，不基于对 Human Research Owner 意图的推测。

```text
READINESS_STATUS=NOT_READY
PROTOTYPE_CREATION_AUTHORIZED=false
```

## 2. Status Vocabulary（状态词表）

| 状态 | 含义 | 不表示 |
|---|---|---|
| `NOT_READY` | 一个或多个前提尚未满足，但可通过补充受控材料和人工决定继续推进 | 项目失败或永久拒绝 |
| `READY_FOR_PROTOTYPE` | 所有前提均有直接证据，且 Human Research Owner 已明确授权进入原型创建审查 | Agent 已创建、实验已获准或 Prototype 已验证 |
| `BLOCKED` | 前提存在无法在当前权限或材料范围内解决的阻断决定 | 自动关闭项目或删除历史记录 |

只有 Human Research Owner 可以基于完整证据和单独授权，把状态推进为 `READY_FOR_PROTOTYPE`。文档完整、检查通过或智能体建议均不能自动推进状态。

## 3. Prerequisite Evaluation（前提评估）

| 前提 | 通过条件 | 当前直接证据 | 当前判定 |
|---|---|---|---|
| Context Package | `context-manifest.yaml` 为 `REVIEWED` 或后续经人类批准的状态 | 当前 `status: DRAFT` | `NOT_MET` |
| Human Owner | `owner_reference` 指向明确的 Human Research Owner，责任与最终科学决定 Owner 已确认 | [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-owner-record.yaml`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-owner-record.yaml) 记录 `bin_zhang` 为 `ASSIGNED`，责任已接受 | `MET` |
| Source Documents | `source_documents` 明确列出来源身份、版本、出处、访问与限制 | Handoff 已列出并核验 10 个候选来源；原 7 个有选择记录，新增 3 个仍待人工决定；canonical Manifest 仍为 `source_documents: []`，批准和绑定数量为 `0` | `NOT_MET` |
| Unknown | 存在由人类复核的 Unknown Record，而不是只有示例或待审草案 | Handoff 已结构化登记 10 个 `UNKNOWN` 草案项；尚未由 Human Research Owner 复核，canonical Record `0` | `PARTIAL` |
| Task Boundary | 允许任务、禁止任务、范围外事项与停止条件均有规范入口 | [`pilot-specification.md`](pilot-specification.md) 已定义允许、禁止与停止条件 | `MET` |
| Evidence Plan | Input、Agent Action、Human Review、Output、Evidence Reference 及失败保留规则形成明确计划 | [`../evidence/research-evidence-model.md`](../evidence/research-evidence-model.md) 已定义完整流程、记录分离与失败保留 | `MET` |
| Human Authorization | 有可定位、适用于特定 Prototype 版本的人工授权记录 | 当前没有授权记录 | `NOT_MET` |

`PARTIAL` 不等于 `MET`。任何 `NOT_MET` 或 `PARTIAL` 都要求 Gate 保持 `NOT_READY`。

## 4. Prepared Human Record Templates（已准备的人工记录模板）

以下空模板已经建立，用于 Human Research Owner 后续创建直接证据：

- [`../research-context/human-owner-record-template.yaml`](../research-context/human-owner-record-template.yaml)：Owner Record；
- [`../research-context/references/source-document-template.yaml`](../research-context/references/source-document-template.yaml)：Source Document Record；
- [`../research-context/unknowns/unknown-record-template.yaml`](../research-context/unknowns/unknown-record-template.yaml)：Unknown Record；
- [`../prototype/prototype-authorization-template.yaml`](../prototype/prototype-authorization-template.yaml)：Prototype Authorization Record。

Paper 3 EOA 的候选输入已组织为 [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/README.md`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/README.md)。Human Research Owner 已记录为 `bin_zhang`；Handoff 仍为 `DRAFT_PENDING_HUMAN_CONTEXT_REVIEW`，10 个来源候选均未批准，10 个 Unknown 均未完成人工复核，Context Review 也未签署。

Template ≠ Record，Template ≠ Authorization。这些文件的存在不把任何 `NOT_MET` 更新为 `MET`。

## 5. Pre-development Agent Recommendation（开发前智能体推荐）

面向“如果潜在客户现在要求创建这个原型，是否推荐？”的当前回答为：

```text
AGENT_RECOMMENDATION=DO_NOT_CREATE_PROTOTYPE_YET
RECOMMEND_SPECIFICATION_AND_GATE_REPAIR=true
RECOMMEND_PROTOTYPE_IMPLEMENTATION=false
```

当前不推荐原因：

1. Context 仍为 `DRAFT`，没有通过 Human Context Review；
2. 已有 10 个已核验来源候选，但新增 3 个仍待人工决定，批准并绑定到 Context Manifest 的来源仍为 `0`；
3. 已有 10 个结构化 Unknown 草案项，但没有 Human-reviewed Record（人工复核记录）实例；
4. 没有指向特定 Prototype 的人工授权。

修正路径是补齐上述直接证据并重新执行本 Gate，而不是降低通过标准、推测 Owner、自动选择来源或把规范文件当作授权。

## 6. Transition Rules（状态转换规则）

进入 `READY_FOR_PROTOTYPE` 之前必须同时满足：

- Human Context Review Record 至少为 `REVIEWED`；
- Context Manifest 的状态由人类同步且版本匹配；
- Human Research Owner 身份和责任明确；
- Source Documents 与 Unknown Records 均可定位并经过人类复核；
- Task Boundary 与 Evidence Plan 已冻结到明确版本；
- 数据、伦理、隐私、安全和发表限制已记录或诚实保留为 Unknown；
- Human Research Owner 作出单独、显式且可定位的 Prototype Authorization（原型授权）。

`READY_FOR_PROTOTYPE` 仅允许开始创建非生产实验对象的另一次受控工作，不允许：

- 创建 Production Agent（生产智能体）；
- 登记 Digital Entity；
- 创建 Runtime 或 Permission；
- 调用外部模型；
- 执行科研任务；
- 生成 Experiment Result、Scientific Conclusion 或 Publication Claim（发表主张）。

## 7. Re-evaluation Procedure（重新评估程序）

1. Human Research Owner 冻结待审 Context 与 Prototype Specification 版本；
2. Reviewer 逐项提供七项前提的直接 Evidence Reference；
3. 未满足项保持 `NOT_MET` 或 `PARTIAL`，Unknown 不得被自动补齐；
4. Human Research Owner 记录 Gate Decision（闸门决定）；
5. 新决定使用新记录或新版本，不追溯性覆盖本次 `NOT_READY` 事实。

## 8. Current State（当前状态）

```text
READINESS_GATE_DEFINED=true
READINESS_STATUS=NOT_READY
CONTEXT_PACKAGE_STATUS=DRAFT
CONTEXT_HANDOFF_STATUS=DRAFT_PENDING_HUMAN_CONTEXT_REVIEW
HUMAN_RESEARCH_OWNER_ASSIGNED=true
HUMAN_RESEARCH_OWNER_REFERENCE=bin_zhang
OWNER_CANDIDATES_DISCOVERED=1
OWNER_CANDIDATE_STATUS=CONFIRMED_AND_ASSIGNED
OWNER_CONFIRMATION_REQUIRED=false
INDEPENDENT_HUMAN_REVIEWER_REQUIRED=UNKNOWN
SOURCE_CANDIDATES=10
SOURCE_CANDIDATES_VERIFIED_FOR_HUMAN_REVIEW=10
SOURCE_CANDIDATES_PENDING_VERIFICATION=0
SOURCE_DOCUMENTS=0
DRAFT_UNKNOWN_ENTRIES=10
HUMAN_REVIEWED_UNKNOWN_RECORDS=0
UNKNOWN_RECORD_INSTANCES=0
TASK_BOUNDARY_DEFINED=true
EVIDENCE_PLAN_COMPLETE=true
HUMAN_GATE_TEMPLATES_DEFINED=true
HUMAN_OWNER_RECORD_INSTANCE_CREATED=true
SOURCE_RECORD_INSTANCES=0
PROTOTYPE_AUTHORIZATION_RECORD_CREATED=false
PROTOTYPE_CREATION_AUTHORIZED=false
Agent Instance = 0
Runtime = 0
Entity = 0
Digital Entity = 0
Permission = 0
Execution = 0
Research Result = 0
```
