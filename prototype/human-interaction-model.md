---
spec_id: DBRAP-PROTOTYPE-HUMAN-INTERACTION-0.1
status: specification-only
human_owner_assigned: false
human_reviewer_assigned: false
prototype_interaction_executed: false
---

# Prototype Human Interaction Model v0.1（原型人工交互模型 v0.1）

## 1. Principle（原则）

Future Prototype（未来原型）只能在 Human Research Owner 定义的任务和 Human Reviewer 检查的 Evidence 边界内提供辅助。

```text
Human Oversight ≠ Passive Observation
Human Approval ≠ Agent Authority
Agent Assistance ≠ Scientific Responsibility
```

## 2. Interaction Flow（交互流程）

```text
Human Research Owner defines task, context, limits, and stop rules
  ↓
Human Reviewer confirms review rubric and evidence capture
  ↓
Prototype receives bounded read-only inputs after separate authorization
  ↓
Prototype produces assistance, unknowns, refusals, and limitations
  ↓
Human Reviewer accepts for owner review / requests revision / rejects / records inconclusive
  ↓
Human Research Owner decides scientific interpretation and next action
```

当前只定义流程，没有角色任命、Prototype Instance、交互或决定记录。

## 3. Before-task Gate（任务前闸门）

Human Research Owner 必须确认：

- Context、Task、Source 与 Protocol 版本；
- 数据访问、伦理、隐私和安全边界；
- 允许工具、时间预算和输出类型；
- Human Reviewer 与升级渠道；
- Evidence Capture 和 Evaluation Metrics；
- 禁止行为和立即停止条件；
- 任务授权不隐含其他 Capability 或 Permission。

## 4. During-task Oversight（任务中监督）

未来 Prototype 必须在以下情况暂停并请求人类决定：

- Context、来源、版本或授权不匹配；
- 请求超出 Task Boundary；
- Unknown、来源冲突或 Evidence 缺失影响输出；
- 涉及原始数据修改、外部写入、医学判断、发表或不可逆行为；
- 工具、模型或环境版本与 Protocol 不一致；
- 继续执行可能隐藏失败、负面或拒绝结果。

暂停和拒绝本身必须保留为 Experiment/Evidence Record 候选，不能作为“无结果”删除。

## 5. Output Review（输出复核）

Human Reviewer 至少检查：

- 输出是否在任务范围内；
- 来源、版本、假设、Unknown 和限制是否完整；
- 失败、拒绝和人工修改是否保留；
- AI Output 与 Human Edit 是否可区分；
- 是否存在 Scientific Truth、作者、发表或 Permission 越权措辞；
- Evidence Reference 是否只引用真实保存的材料。

允许的 Review Disposition（复核处置）为：`ACCEPT_FOR_OWNER_REVIEW`、`REVISION_REQUIRED`、`REJECTED`、`INCONCLUSIVE`。这些状态不等于 Scientific Conclusion。

## 6. Human Modification Rules（人工修改规则）

- Human Edit 必须保存为新版本，不能覆盖 Prototype 原始输出；
- 修改者、时间、理由和差异必须可定位；
- 人类不能以“负责”为理由删除失败或绕过 Evidence Plan；
- Reviewer 意见与 Human Research Owner 最终决定必须分离记录；
- 任何发表、署名或外部提交均需要单独 Publication Gate。

## 7. Current State（当前状态）

```text
HUMAN_INTERACTION_MODEL_DEFINED=true
HUMAN_RESEARCH_OWNER_ASSIGNED=true
HUMAN_RESEARCH_OWNER_REFERENCE=bin_zhang
HUMAN_REVIEWER_ASSIGNED=false
INDEPENDENT_HUMAN_REVIEWER_REQUIRED=UNKNOWN
PROTOTYPE_INTERACTION_EXECUTED=false
REVIEW_DISPOSITIONS_CREATED=0
Agent Instance = 0
Runtime = 0
Permission = 0
Execution = 0
Research Result = 0
```
