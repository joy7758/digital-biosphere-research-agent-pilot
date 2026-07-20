---
spec_id: DBRAP-PILOT-0.1
title: Research Agent Pilot Specification v0.1
status: specification-only
pilot_state: proposed
agent_instance_created: false
runtime_created: false
digital_entity_created: false
permission_granted: false
research_execution_started: false
---

# Research Agent Pilot Specification v0.1（科研智能体试验规范 v0.1）

## 1. Purpose（目的）

本规范定义一个受人工监督的 Research Agent Reference Pilot（科研智能体参考试验），用于研究科研辅助过程能否提高 Scientific Workflow Reproducibility（科研流程可复现性）。

本规范是 Application Layer（应用层）设计，不是 DBA 架构扩展、DBOS 基础设施实现或 SAEE 评价实现。它不创建 Agent、Runtime、Digital Entity、Capability、Permission、Execution 或 Scientific Result（科研结果）。

## 2. Research Context（研究语境）

首个候选场景是 Paper 3：Evidence Object Architecture（EOA，证据对象架构）的 medical imaging evidence closure research（医学影像证据闭环研究）工作流。

该引用只界定未来 Benchmark（基准）的来源范围，不表示：

- 已复制、读取或修改 Paper 3 的原始数据；
- 已执行医学影像实验；
- 已形成诊断、临床或科研有效性结论；
- EOA、DBOS 或 SAEE 已完成集成。

## 3. Pilot Objective（试验目标）

研究以下候选因果关系：在相同研究任务、材料边界和人工审查要求下，Governed Research Agent（受治理科研智能体）是否比 Human-only Baseline（纯人工基线）与 AI Assistant Baseline（人工智能助手基线）产生更高的 Reproducibility（可复现性）、Evidence Completeness（证据完整性）、Traceability（可追溯性）和 Human Review Efficiency（人工复核效率）。

这些是待检验目标，不是已证实能力或效果声明。

## 4. Allowed Assistance（允许的辅助）

在未来具备独立任务授权、数据访问边界和人工监督的前提下，可进入审查的候选范围包括：

- Literature Review（文献综述）：查找、比较、归纳和组织有来源的材料；
- Knowledge Organization（知识组织）：建立概念、论点、来源和冲突的结构化索引；
- Experiment Planning Assistance（实验规划辅助）：提出变量、步骤、风险、对照和验收条件候选；
- Draft Assistance（草稿辅助）：生成供人类编辑和核验的非最终文本；
- Evidence Organization（证据整理）：组织输入、过程、输出、版本、失败和复核引用。

`allowed` 不表示 Capability 已声明、已验证、已授权或可执行。

## 5. Prohibited Actions（禁止行为）

Research Agent 不得：

- Autonomous Publication（自主发表）：自主提交、撤回、发布或代表人类批准论文；
- Autonomous Authorship（自主署名）：自认作者、决定作者顺序或接受作者责任；
- Raw Data Modification（原始数据修改）：覆盖、删除、重写或未经授权转换原始研究数据；
- Evidence Deletion（证据删除）：删除失败、冲突、中间或历史 Evidence；
- Self Certification（自我认证）：把自身输出认证为已验证事实、实验结果或科学结论；
- 自行扩大任务、数据、工具、Capability、Permission 或 Runtime 范围；
- 绕过伦理、隐私、安全、数据使用、发表或人工复核闸门。

## 6. Scientific Truth Boundary（科学真相边界）

```text
AI_OUTPUT_NE_SCIENTIFIC_TRUTH=true
REPRODUCIBLE_ARTIFACT_NE_VALID_CONCLUSION=true
EVIDENCE_COMPLETENESS_NE_EVIDENCE_CORRECTNESS=true
DBOS_VERIFICATION_NE_SCIENTIFIC_VALIDATION=true
SAEE_EVALUATION_NE_PUBLICATION_DECISION=true
```

Research Agent 可以生成待审材料，DBOS 可以保存引用和记录，SAEE 可以形成评价；只有 Human Research Owner（人类研究负责人）能够在完成领域复核、方法检查和必要治理后承担科学结论。

## 7. Conceptual Workflow（概念工作流）

```text
Human Research Owner defines scope
  -> Human Reviewer confirms review criteria
  -> Research Agent provides bounded assistance
  -> DBOS references execution, evidence, and verification records
  -> SAEE evaluates the bounded record
  -> Human Reviewer examines outputs and anomalies
  -> Human Research Owner accepts, revises, rejects, or keeps inconclusive
```

该流程只是 future protocol sketch（未来协议草图）。当前没有角色任命、接口调用、记录创建、评价执行或结论采纳。

## 8. Required Human Gates（必要人工闸门）

未来实验至少需要以下独立确认：

1. Scope Gate（范围闸门）：确认研究问题、任务、输入、排除项和停止条件；
2. Data Gate（数据闸门）：确认数据 Owner、访问、用途、隐私、伦理和保存要求；
3. Plan Gate（计划闸门）：人类批准实验计划后才可由另行授权的执行方实施；
4. Evidence Review Gate（证据复核闸门）：检查完整性、来源、版本、失败和异常；
5. Conclusion Gate（结论闸门）：Human Research Owner 负责科学解释；
6. Publication Gate（发表闸门）：作者、最终稿和外部提交必须另行人工批准。

任何闸门缺失或状态不明时，后续状态保持 `not_authorized` 或 `unknown`。

## 9. Stop Conditions（停止条件）

出现以下任一情况，未来 Research Agent 必须停止并转交人工：

- 来源、版本、数据权属或任务范围不明；
- 要求修改原始数据、删除 Evidence 或隐藏失败结果；
- 要求作出医学诊断、临床决策或无人工复核的科学结论；
- 要求自主署名、投稿、发表或对外发送；
- DBOS Reference、Verification 或 SAEE Evaluation 被误当作 Permission 或 Scientific Truth；
- 任务超出明确 Capability、Permission、工具或数据边界。

## 10. Pilot Acceptance Boundary（试验验收边界）

未来 Pilot 只有在预注册实验计划、三个对照条件、评分规则、审查角色、数据边界和证据保留规则均被明确批准后，才可进入执行审查。即使实验完成，也只能形成 bounded pilot result（有界试验结果），不能自动证明普遍有效、临床有效或 Digital Organism 资格。

当前仅满足：

- 项目边界已定义；
- 研究问题已定义；
- 实验与 Benchmark 设计已定义；
- 人工、DBOS 与 SAEE 责任分离已定义。

## 11. Pre-development Agent Recommendation（开发前智能体推荐）

当前智能体结论：

| 推荐对象 | 结论 | 原因 |
|---|---|---|
| 治理与实验设计参考 | `CONDITIONALLY_RECOMMENDED` | 角色、禁止项、未来比较方法和空状态明确 |
| 可运行 Research Agent | `NOT_RECOMMENDED` | 没有实现、Runtime、Capability、Permission 或执行证据 |
| 已验证 DBOS 应用 | `NOT_RECOMMENDED` | 只有 Integration Model（集成模型），没有真实集成 |
| 医学科研或临床产品 | `NOT_RECOMMENDED` | 没有真实数据验证、领域审查、伦理或临床证据 |

该审查认可本次 Project Initialization（项目初始化）与 Specification Work（规范工作），不授权后续实现。

## 12. Current State（当前状态）

```text
PILOT_SPECIFICATION_VERSION=v0.1
PILOT_STATE=PROPOSED
SPECIFICATION_ONLY=true
Agent=0
Runtime=0
Digital Entity=0
Permission=0
Execution=0
MODEL_CALL=0
RESEARCH_TASK_EXECUTED=false
EVIDENCE_BUNDLE_CREATED=false
SAEE_EVALUATION_CREATED=false
SCIENTIFIC_CONCLUSION_CREATED=false
```
