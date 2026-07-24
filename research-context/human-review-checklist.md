---
checklist_id: DBRAP-HUMAN-CONTEXT-REVIEW-0.1
title: Human Context Review Checklist v0.1
status: template-only
context_review_executed: false
review_record_created: false
context_approved: false
---

# Human Context Review Checklist v0.1（人工研究上下文复核清单 v0.1）

## Purpose（目的）

本清单定义 Human Research Owner（人类研究负责人）如何审查一个特定 `context_id` 与 `version` 的 Research Context Package（研究上下文包）。它用于确认研究所有权、范围、来源、Unknown（未知项）和 AI Usage Boundary（人工智能使用边界），不用于创建 Agent、Permission 或科研结论。

当前文件是未填写的 Checklist Template（清单模板），不是已完成的 Human Review Record（人工复核记录）。

## Core Principles（核心原则）

```text
Human Review ≠ Agent Approval
Context Approval ≠ Scientific Truth
Source Selection ≠ Source Validation
Unknown must remain Unknown
```

- Human Review 只确认 Context 是否适合作为有界研究输入，不授予 Agent Authority（智能体权力）；
- Context Approval 不认证来源正确，也不证明研究结论成立；
- Source Selection（来源选择）只表示来源被纳入审查范围，不替代来源验证；
- Unknown 不得被 Agent、Reviewer 或自动化流程推测补全。

## Review Header（复核头信息）

- [ ] 待审 `context_id` 已记录；
- [ ] 待审 `version` 已记录；
- [ ] Context Manifest（上下文清单）当前状态已记录；
- [ ] Human Reviewer（人类复核者）身份和角色已记录；
- [ ] 复核开始时间和适用研究任务已记录；
- [ ] 复核期间没有静默修改待审 Package。

## Section 1: Research Ownership（研究所有权）

- [ ] Human Research Owner identified（已识别人类研究负责人）；
- [ ] Responsibility defined（已定义研究责任）；
- [ ] Final scientific decision owner confirmed（已确认最终科学决定负责人）；
- [ ] Context 批准责任与 DBOS、SAEE、Agent 职责保持分离；
- [ ] Reviewer 是可识别的人类，不是 Research Agent、模型、自动化程序或 SAEE Evaluation（SAEE 评价）。

未识别 Human Research Owner 时，Review 不得进入 `APPROVED`。

## Section 2: Research Scope（研究范围）

- [ ] Research question defined（已定义研究问题）；
- [ ] Scope boundary defined（已定义范围边界）；
- [ ] Out-of-scope items recorded（已记录范围外事项）；
- [ ] 允许的任务、材料、时间和用途已记录；
- [ ] 医学、临床、伦理、隐私、安全和发表限制已记录或明确标为 Unknown；
- [ ] Context Scope（上下文范围）没有被误写成 Agent Capability 或 Permission。

范围不清、相互冲突或无法复核时，应选择 `REVIEW_PENDING` 或 `REJECTED`，不得推测补齐。

## Section 3: Source Review（来源复核）

对每个 `source_document` 分别检查：

- [ ] Source identity（来源身份）可定位；
- [ ] Version（版本）或日期已记录；
- [ ] Origin（来源出处）已记录；
- [ ] Access limitation（访问限制）已记录；
- [ ] Known limitation（已知限制）已记录；
- [ ] 原始来源与派生摘要可区分；
- [ ] 来源冲突、失效、版本漂移或验证缺口已进入 Unknown；
- [ ] 来源不是自动读取的 Chat History（聊天历史）、浏览历史或隐式模型记忆；
- [ ] Source Selection 没有被表述为 Source Validation（来源验证）。

如果 `source_documents: []`，Reviewer 必须记录空来源集合是否是有意状态以及它为何仍不足或足以支持特定 Context。空列表不能被自动解释为“没有限制”。

## Section 4: Unknown Review（未知项复核）

- [ ] Unknown items listed（已列出未知事项）；
- [ ] Missing information documented（已记录缺失信息）；
- [ ] No assumption replacement（没有用假设替代未知）；
- [ ] 来源冲突没有被自动合并为单一结论；
- [ ] 每个已解决 Unknown 都有来源、决定者、时间和 Resolution Reference（解决依据）；
- [ ] 未解决 Unknown 将随 Package 进入后续 Human Review，而不是从 Context 中删除。

Reviewer 不能因为希望推进 Approval 就把 `unknown`、`null`、缺失或冲突改写为肯定或否定。

## Section 5: AI Usage Boundary（人工智能使用边界）

### Allowed Assistance（允许的辅助）

- [ ] Literature organization（文献组织）边界已记录；
- [ ] Knowledge synthesis（知识综合）边界已记录；
- [ ] Draft assistance（草稿辅助）边界已记录；
- [ ] Experiment planning assistance（实验规划辅助）边界已记录。

这些是未来可进入独立 Capability 与 Permission 审查的候选辅助范围，不表示当前 Agent 存在或已获授权。

### Prohibited Actions（禁止行为）

- [ ] Scientific conclusion ownership（科学结论所有权）明确属于人类；
- [ ] Autonomous publication（自主发表）明确禁止；
- [ ] Raw data modification（原始数据修改）明确禁止；
- [ ] Evidence deletion（证据删除）明确禁止；
- [ ] Agent 修改 Context、Review Record、Unknown 或研究决策明确禁止；
- [ ] Context Approval 自动生成 Permission、Execution 或 Scientific Truth 明确禁止。

任一禁止边界缺失时，Review 不得进入 `APPROVED`。

## Section 6: Approval Decision（批准决定）

### Review Status Vocabulary（复核状态词表）

| `review_status` | 含义 | 不表示 |
|---|---|---|
| `REVIEW_PENDING` | 复核尚未完成或仍有阻断项 | Package 已 `REVIEWED` |
| `REVIEWED` | 所有必要部分已由人类检查，问题与限制已记录 | Context 已批准或 Agent 可读取 |
| `APPROVED` | Human Research Owner 接受该版本作为特定任务的有界 Context 输入 | Scientific Truth、Permission、Execution 或 Agent Approval |
| `REJECTED` | 该版本不适合作为目标任务的 Context 输入 | 历史记录可以删除 |

### Decision Completion（决定完成条件）

- [ ] `review_id` 已分配；
- [ ] `context_id` 与待审 Manifest 完全匹配；
- [ ] `reviewer_reference` 指向明确的人类；
- [ ] `review_notes` 记录限制、异议和未解决事项；
- [ ] `approved_sources` 与实际复核来源一致；
- [ ] `identified_unknowns` 与 Package Unknown 一致；
- [ ] `timestamp` 已记录；
- [ ] 最终 `APPROVED` 决定由 Human Research Owner 明确作出。

Review Record 的 `APPROVED` 不得自动修改 `context-manifest.yaml`。Human Research Owner 必须在确认 Record 与 Package 版本一致后，另行人工更新 Context 状态；该更新仍不创建 Agent 读权限。

## Current Checklist State（当前清单状态）

```text
HUMAN_CONTEXT_REVIEW_CHECKLIST_DEFINED=true
HUMAN_CONTEXT_REVIEW_EXECUTED=false
REVIEW_RECORD_INSTANCE_CREATED=false
REVIEW_STATUS=REVIEW_PENDING
CONTEXT_PACKAGE_STATUS=DRAFT
CONTEXT_APPROVED=false
Agent=0
Runtime=0
Entity=0
Permission=0
Execution=0
Research Result=0
```
