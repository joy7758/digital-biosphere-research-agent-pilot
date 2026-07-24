---
spec_id: DBRAP-HUMAN-OVERSIGHT-0.1
status: specification-only
roles_assigned: false
authority_granted: false
---

# Human Oversight Model v0.1（人工监督模型 v0.1）

## 1. Principle（原则）

> Human owns scientific conclusions.
>
> 人类拥有并承担科学结论责任。

Human Oversight（人工监督）不是点击确认的形式步骤，而是研究问题、数据使用、方法采用、异常处理、科学解释和外部发表的责任分配。本模型只定义角色，不任命人员或授予权限。

## 2. Role Separation（角色分离）

| 角色 | 责任 | 可以做 | 不可以做 |
|---|---|---|---|
| Human Research Owner（人类研究负责人） | 对研究问题、方法采用、结论、署名和发表承担最终责任 | 定义范围；批准或拒绝计划；解释结果；决定是否保持 `inconclusive` | 把科学责任转移给 Agent；以人工确认绕过数据、伦理或治理要求 |
| Human Reviewer（人类复核者） | 独立检查来源、方法、证据、失败、异常和限制 | 接受进入 Owner 审查、要求修改、拒绝或记录未解决问题 | 自动代表 Owner 作最终结论；把 Traceability 等同于 Scientific Validity |
| Research Agent（科研智能体） | 在批准范围内提供可追溯的辅助材料 | 文献、知识、计划、草稿和证据整理辅助 | 自我授权、自我认证、自主实验、自主署名、自主发表或删除 Evidence |

同一人承担 Owner 与 Reviewer 时必须披露 non-independence（非独立性）；医学影像等高风险任务是否要求独立领域复核，必须在未来实验批准前决定。

## 3. Decision Ownership（决定归属）

| 决定 | 负责角色 | Agent 地位 |
|---|---|---|
| 研究问题与停止规则 | Human Research Owner | 可提供建议，不拥有决定权 |
| 数据能否使用 | 数据 Owner 与适用治理主体 | 不得推断访问权 |
| 实验计划是否采用 | Human Research Owner 与适用审批主体 | 只提供候选计划 |
| 输出是否完整 | Human Reviewer | Agent 可标记但不能自证 |
| 科学结论是否成立 | Human Research Owner | 不得自我认证 |
| 作者、投稿与发表 | 人类作者与明确授权者 | 不得自主行动 |
| 系统变化是否采用 | 适用 Governance Decision（治理决定） | SAEE Recommendation 也不是授权 |

## 4. Review Flow（复核流程）

```text
Owner defines task and boundaries
  -> Reviewer confirms review checklist
  -> Agent produces bounded draft material
  -> Reviewer checks sources, omissions, conflicts, and failures
  -> Owner chooses accept / revise / reject / inconclusive
```

每次转交必须保留输入版本、输出版本、已知限制和未解决项。没有明确 Reviewer 意见时，输出不得进入 Conclusion Gate（结论闸门）。

## 5. Mandatory Escalation（强制升级）

以下情况必须由 Research Agent 停止并升级给人类：

- 数据授权、伦理、隐私或安全状态不明；
- 医学或科研结论需要领域判断；
- 来源冲突、Evidence 缺失或 Verification 无法解释；
- 请求执行外部操作、投稿、发表、署名或不可逆变化；
- 请求覆盖原始数据或删除历史记录；
- 任务范围、Capability 或 Permission 不明确。

## 6. Non-instantiation Status（非实例化状态）

```text
HUMAN_OVERSIGHT_MODEL_DEFINED=true
HUMAN_RESEARCH_OWNER_ASSIGNED=true
HUMAN_RESEARCH_OWNER_REFERENCE=bin_zhang
HUMAN_REVIEWER_ASSIGNED=false
INDEPENDENT_HUMAN_REVIEWER_REQUIRED=UNKNOWN
RESEARCH_AGENT_INSTANCE_CREATED=false
DECISION_AUTHORITY_GRANTED=false
REVIEW_AUTHORITY_GRANTED=false
PUBLICATION_APPROVED=false
```
