---
spec_id: DBRAP-HUMAN-CONTEXT-GOVERNANCE-0.1
status: specification-only
human_review_executed: false
context_approved: false
agent_read_access_granted: false
---

# Human Context Governance Model v0.1（人工上下文治理模型 v0.1）

## 1. Purpose（目的）

本模型定义 Human Review（人工复核）、Research Context Package（研究上下文包）和未来 Research Agent Read Access（科研智能体读取权限）之间的责任分离。它不创建 Reviewer、Agent、Permission、API 或自动状态转换。

## 2. Core Boundaries（核心边界）

```text
Human Review ≠ Agent Approval
Context Approval ≠ Scientific Truth
Source Selection ≠ Source Validation
Unknown must remain Unknown
Review ≠ Permission
```

Human Review 只判断某个 Context 版本是否适合作为特定科研任务的受控输入。Context 是否适合作为输入、Agent 是否存在以及 Agent 是否有权读取，是三个独立决定。

## 3. Required Flow（必要流程）

```text
Human Research Owner
  ↓ defines ownership and final decision responsibility
Context Review
  ↓ records sources, limitations, unknowns, and decision
Approved Context Package
  ↓ requires separate Agent identity, capability, permission, and access authorization
Research Agent Read Access
```

当前流程停在 Checklist 与 Template 定义阶段：没有 Context Review 实例，没有 Approved Context Package，也没有 Research Agent Read Access。

## 4. Role Responsibilities（角色责任）

| 角色 | 责任 | 禁止行为 |
|---|---|---|
| Human Research Owner（人类研究负责人） | 确认研究责任、范围、来源、Unknown、最终 Context 决定和科学决定 Owner | 把 Context Approval 写成 Scientific Truth 或 Agent Permission |
| Human Reviewer（人类复核者） | 按清单检查版本、来源、限制、冲突、Unknown 和 AI 使用边界 | 代表 Agent、自称自动验证来源或隐藏未解决项 |
| Research Agent（科研智能体） | 未来在独立授权后只读使用指定 `APPROVED` Context | 成为 Reviewer、修改 Review、批准自身 Context 或推断 Unknown |
| DBOS | 未来只处理其职责内的 Identity、Execution、Evidence 与 Verification Reference | 选择研究来源、批准 Context 或决定 Scientific Truth |
| SAEE | 未来评价有界执行与证据记录 | 成为 Context Reviewer、授予 Permission 或修改 Review |

如 Human Research Owner 同时承担 Human Reviewer，应记录 non-independence（非独立性）。是否需要独立领域 Reviewer 必须由研究风险和未来治理要求决定，不能由 Agent 推断。

## 5. Review and Context State Separation（复核与上下文状态分离）

| Review Record 状态 | 可以支持的人类操作 | 禁止自动效果 |
|---|---|---|
| `REVIEW_PENDING` | 继续收集复核信息 | 不改变 Context 状态 |
| `REVIEWED` | Human Research Owner 考虑把 Context 从 `DRAFT` 更新为 `REVIEWED` | 不自动更新 Manifest |
| `APPROVED` | Human Research Owner 在核对版本后考虑把 Context 从 `REVIEWED` 更新为 `APPROVED` | 不创建 Agent、Permission 或 Read Access |
| `REJECTED` | 保留记录并修订新版本或停止使用 | 不删除 Package 或历史 Review |

Review Record 与 Context Manifest 的状态变更必须由人类分别记录。任何工具、Agent、Hook（钩子）或评价结果都不能自动推进二者。

## 6. Review Immutability（复核不可由 Agent 修改）

Research Agent 不能：

- 创建、覆盖或删除 Human Review Record；
- 修改 `reviewer_reference`、`review_status`、`review_notes` 或 `timestamp`；
- 增删 `approved_sources` 或 `identified_unknowns`；
- 把自己的 Self Review（自我复核）作为 Human Review；
- 将 Context `APPROVED` 解读为自身已获批准或有权读取；
- 触发 Context Manifest 的自动状态改变。

发现 Review 与 Package 不一致时，Agent 只能停止并提交 Conflict Report（冲突报告）给 Human Research Owner。

## 7. Read Access Gate（读取权限闸门）

即使 Context Package 已 `APPROVED`，未来 Research Agent Read Access 仍至少需要：

- 已存在且可解析的 Agent Identity（智能体身份）；
- 独立确认的 Capability（能力）范围；
- 明确的 Permission（权限）与数据访问边界；
- 指向特定 `context_id` 和 `version` 的任务授权；
- 只读、最小范围且可撤销的访问机制；
- Human Oversight（人工监督）与停止规则。

这些条件当前均未建立，本规范也不授权建立。

## 8. Prohibited Automation（禁止的自动化）

- 自动批准 Context；
- 把 Agent 指定为 Reviewer；
- 由 Review 生成 Permission；
- 由 Approval 生成 Scientific Truth；
- 自动填充 Unknown；
- 自动创建 Research Agent Read Access。

## 9. Current Status（当前状态）

```text
HUMAN_CONTEXT_GOVERNANCE_MODEL_DEFINED=true
HUMAN_CONTEXT_REVIEW_EXECUTED=false
REVIEW_RECORD_INSTANCE_CREATED=false
CONTEXT_PACKAGE_STATUS=DRAFT
CONTEXT_APPROVED=false
AGENT_REVIEWER_ASSIGNED=false
AGENT_READ_ACCESS_GRANTED=false
Agent=0
Runtime=0
Entity=0
Permission=0
Execution=0
Research Result=0
```
