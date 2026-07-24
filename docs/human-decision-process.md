---
document_id: DBRAP-HUMAN-DECISION-PROCESS-0.1
status: HUMAN_DECISION_RECORDED_REVIEW_NOT_EXECUTED
decision_record_status: HUMAN_CONFIRMED
context_status: DRAFT
review_status: REVIEW_PENDING
---

# Human Decision Process v0.1（人工决定流程 v0.1）

## Purpose（目的）

本流程定义 Human Research Owner（人工研究负责人）如何把明确决定保存为可追溯的 Human Context Decision Record（人工上下文决策记录）。它不授权 AI 填写决定，不自动更新 Context，也不创建 Agent、Permission（权限）或 Experiment Authorization（实验授权）。

```text
Human Research Owner
        ↓
Decision Input
        ↓
Human Review
        ↓
Separate Context Update
```

## 1. Human Research Owner（人工研究负责人）

Human Research Owner 必须亲自决定：

- 每个候选来源是 `INCLUDE_WITH_LIMITATIONS`、`EXCLUDE` 还是 `DEFER`；
- 每项待确认研究决定是 `CONFIRM_WITH_BOUNDARIES`、`REVISE` 还是 `REJECT`；
- 每个 Unknown（未知项）是 `ACCEPT_UNKNOWN`、`RESOLUTION_REQUIRED` 还是 `DEFERRED`；
- AI Usage Boundary（AI 使用边界）的允许、限制与需要逐次批准的活动；
- `autonomy_preference` 是否选择 `APPROVAL_REQUIRED`、`DELEGATED_AUTONOMY` 或 `FULL_AUTONOMY_WITHIN_SCOPE`；
- 是否需要 Independent Human Reviewer（独立人工复核者）。

这些选择是治理决定，不是 Scientific Truth（科学事实）、实验结论或 Agent Permission。

## 2. Decision Input（决定输入）

输入字段入口为：

- [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-input-template.yaml`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-input-template.yaml)：定义允许输入与完整性规则；
- [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-record.yaml`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-record.yaml)：固定 `decision_id: HCD-001` 的待填写历史记录壳。

在收到明确 Human Input（人工输入）前，`HCD-001` 必须保持：

```text
status=PENDING_HUMAN_INPUT
review_status=PENDING_HUMAN_REVIEW
human_decisions_recorded=0
```

空值、沉默、推荐文本、复选框草稿、Git 作者信息或 AI 输出均不能作为 Human Decision。

当前 Human Research Owner 已明确提供决定，Codex（代码智能体）仅作机械转录；`HCD-001` 因此为 `HUMAN_CONFIRMED`。这不改变上述输入前规则，也不表示 Human Review 已完成。

## 3. AI Boundary（AI 边界）

AI 可以：

- 建立空字段结构；
- 检查 ID 覆盖、字段完整性、词表合法性和引用可定位性；
- 报告缺失、冲突或无法验证的输入；
- 根据明确的人类逐项输入进行机械转录，并保留输入来源。

AI 不可以：

- 选择或推断任何 `decision`、`disposition`、`reason`、`rationale` 或 `autonomy_preference`；
- 用非绑定 Recommendation（建议）填充 Decision Record；
- 把 Owner Confirmation（负责人确认）解释为 Context Approval；
- 把 Review Record 解释为 Agent Permission、Prototype Authorization 或 Experiment Authorization；
- 自动填写复核者、时间、签署或人类证明。

## 4. Human Review（人工复核）

Human Reviewer 必须核对：

1. `decision_id`、`context_id`、版本和 Owner Reference 与待审对象一致；
2. 7 个 Source Decision、4 个 Research Decision 和 10 个 Unknown Review 均由人类明确填写；
3. 理由、限制、冲突、Unknown 和 Resolution Requirement（解决要求）没有被省略；
4. AI Usage Boundary 与 Autonomy Preference 没有自动扩大能力；
5. 决定者、复核者、时间和 Human Attestation（人工证明）可追溯；
6. `Context Approval ≠ Experiment Authorization` 和 `Review Record ≠ Agent Permission` 边界仍被保留。

复核未完成时，Record 保持 `PENDING_HUMAN_REVIEW`。

## 5. Separate Context Update（独立 Context 更新）

完成 Decision Record 与 Human Review 后，Human Research Owner 才能另行决定是否创建新的 Context Package 版本或更新其状态。该动作必须独立记录，不能由 `HCD-001` 自动触发。

```text
Decision Record ≠ Context Update
Context Review ≠ Context Approval
Context Approval ≠ Prototype Authorization
Prototype Authorization ≠ Experiment Authorization
Review Record ≠ Agent Permission
```

## 6. Current State（当前状态）

```text
HUMAN_OWNER=CONFIRMED
DECISION_RECORD=HUMAN_CONFIRMED
HUMAN_DECISIONS=RECORDED_23
CONTEXT=DRAFT
REVIEW=REVIEW_PENDING
PROTOTYPE=NOT_AUTHORIZED
Agent=0
Runtime=0
Entity=0
Permission=0
Execution=0
```

本流程已记录明确 Human Decision，但没有执行 Human Review、Context Update、Agent 创建或科研实验。
