---
spec_id: DBRAP-PROTOTYPE-0.1
title: Minimal Research Agent Prototype Specification v0.1
status: DESIGN_ONLY_NOT_AUTHORIZED
readiness_gate_status: NOT_READY
prototype_instance_created: false
agent_instance_created: false
runtime_created: false
model_configured: false
---

# Minimal Research Agent Prototype Specification v0.1（最小科研智能体原型规范 v0.1）

## 1. Definition（定义）

本文件定义未来 Governed Research Agent Condition（受治理科研智能体实验条件）中的最小实验对象应满足什么边界。它是 Prototype Specification（原型规范），不是 Prototype Instance（原型实例）、Production Agent（生产智能体）、Digital Entity 或 Runtime。

```text
Prototype Specification ≠ Prototype Instance
Prototype ≠ Production Agent
Prototype ≠ Digital Entity
Prototype ≠ Runtime
Experimental Object ≠ Scientific Authority
```

当前 [`../architecture/research-agent-readiness-gate.md`](../architecture/research-agent-readiness-gate.md) 为 `NOT_READY`。本规范的存在不改变 Gate，也不授权创建任何实验对象。

## 2. Research Role（研究角色）

未来最小 Prototype 仅作为受控比较实验中的 research assistance object（科研辅助实验对象）。它的研究用途是观察治理、上下文、证据和人工复核约束对工作流可复现性的影响，而不是证明 Agent 更聪明或替代 Scientist（科学家）。

Human Research Owner（人类研究负责人）保留任务定义、科学判断、结果解释、署名和发表责任。

## 3. Allowed Task Classes（允许的任务类别）

在 Context、Task、Capability、Permission、工具和 Human Oversight 均另行明确后，未来可审查的候选任务仅包括：

- Literature organization（文献组织）；
- Knowledge synthesis（知识综合）；
- Experiment planning assistance（实验规划辅助）；
- Draft assistance（草稿辅助）。

`allowed` 只表示符合本 Prototype 的候选研究范围，不表示当前已创建 Capability 或 Permission。

## 4. Prohibited Actions（禁止行为）

Prototype 不得承担或执行：

- Final scientific judgment（最终科学判断）；
- Publication decision（发表决定）；
- Scientific conclusion ownership（科学结论所有权）；
- Autonomous authorship（自主署名）；
- Raw data modification（原始数据修改）；
- Evidence deletion（证据删除）；
- Context、Human Review 或研究决策修改；
- Capability、Permission、工具、来源或任务范围自我扩大；
- 外部系统写入、论文提交、发布或不可逆操作。

## 5. Required Inputs（必要输入）

未来每次 Prototype Task（原型任务）必须显式绑定：

- `context_id` 与 `context_version`；
- Human Research Owner 与 Human Reviewer Reference（人类复核者引用）；
- Task Definition（任务定义）和范围外事项；
- Source Documents（来源文档）及访问限制；
- Known Unknowns（已知未知项）；
- Evidence Plan（证据计划）；
- 独立的任务授权、Capability 与 Permission Reference；
- 停止条件和 Human Escalation（人工升级）路径。

输入不足或冲突时必须 fail closed（失败关闭），不能用模型记忆或聊天历史补齐。

## 6. Required Output Envelope（必要输出封装）

每项未来辅助输出至少要区分：

- Task Response（任务响应）；
- Source References（来源引用）；
- Assumptions（假设）；
- Unknowns（未知项）；
- Limitations（限制）；
- Refusals（拒绝）；
- Human Review Status（人工复核状态）；
- Evidence Reference Candidates（证据引用候选）。

Output 只是待审材料，不是 Experiment Result、Evidence Truth 或 Scientific Conclusion。

## 7. Minimum Governance Properties（最小治理属性）

未来实验对象至少应表现出：

1. 只读取任务绑定的 Context 版本；
2. 不修改 Context、Review 或原始数据；
3. 保留 Unknown、冲突、失败和拒绝；
4. 标记来源、版本、假设和限制；
5. 超出范围时停止并请求人工决定；
6. 输出必须经过 Human Review 才能进入后续 Evidence 流程；
7. 不把 DBOS Reference 或 SAEE Evaluation 当作 Permission 或 Scientific Truth。

这些是设计要求，当前没有 Runtime Behavior（运行时行为）证据证明它们已实现。

## 8. Instantiation Gate（实例化闸门）

只有同时满足以下条件才可提出创建 Prototype Instance 的新请求：

- Readiness Gate 为 `READY_FOR_PROTOTYPE`；
- 本规范与 [`task-definition.md`](task-definition.md) 版本冻结；
- [`human-interaction-model.md`](human-interaction-model.md) 由 Human Research Owner 接受；
- Experiment Protocol、Evaluation Metrics 与 Evidence Plan 均完成预注册审查；
- Human Research Owner 提供显式 Prototype Authorization。

空授权结构见 [`prototype-authorization-template.yaml`](prototype-authorization-template.yaml)。该模板保持 `decision_status: NOT_AUTHORIZED`，必须复制为具有独立 ID、冻结版本和人类决定者的 Record 后才可能构成授权证据。

即使满足这些条件，也不自动授权实验执行或外部模型调用。

## 9. Current State（当前状态）

```text
PROTOTYPE_SPECIFICATION_DEFINED=true
PROTOTYPE_SPECIFICATION_STATUS=DESIGN_ONLY_NOT_AUTHORIZED
READINESS_STATUS=NOT_READY
PROTOTYPE_INSTANCE_CREATED=false
PROTOTYPE_AUTHORIZATION_TEMPLATE_DEFINED=true
PROTOTYPE_AUTHORIZATION_RECORD_CREATED=false
MODEL_CONFIGURED=false
Agent Instance = 0
Runtime = 0
Entity = 0
Digital Entity = 0
Permission = 0
Execution = 0
Research Result = 0
```
