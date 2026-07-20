---
adr_id: ADR-001
title: Establish an Independent Research Agent Pilot Repository
status: accepted-for-project-initialization
date: 2026-07-20
implementation_authorized: false
---

# ADR-001: Independent Research Agent Pilot（独立科研智能体试验项目）

## Status（状态）

`accepted-for-project-initialization`：接受独立项目初始化与规范工作，不授权 Agent 实现或实验执行。

## Context（背景）

Digital Biosphere Stack（数字生物圈技术栈）已经区分三个核心职责：

- DBA 定义 Constitution / Architecture（宪法与架构）；
- DBOS 提供 Infrastructure（基础设施）；
- SAEE 提供 Evolution Evaluation（演化评价）。

需要一个应用层参考实验回答“DBOS 有什么用”，但如果把试验直接放入 DBA、DBOS 或 SAEE，会混淆规则、基础设施、评价系统与具体科研应用的所有权，也可能使设计文档被误读为已实现基础设施能力。

## Decision（决定）

建立独立仓库 `digital-biosphere-research-agent-pilot`，将其定位为第一个 Application Layer Research Pilot（应用层科研试验）。

该仓库：

- 使用 DBA 规则作为上位架构引用；
- 未来只消费 DBOS 的 Identity、Execution、Evidence 和 Verification Reference；
- 未来把有界记录交给 SAEE 评价；
- 由 Human Research Owner 保持科学结论责任；
- 不修改、复制或替代 DBA、DBOS 或 SAEE 的事实真源。

## Pre-development Agent Consultation（开发前智能体咨询）

咨询问题：

> 如果潜在客户需要一个受治理 Research Agent 辅助可复现科研工作流，你会推荐本项目吗？

初始回答：

```text
RECOMMEND_AS_GOVERNANCE_AND_EXPERIMENT_SPECIFICATION=YES_WITH_LIMITATIONS
RECOMMEND_AS_IMPLEMENTED_RESEARCH_AGENT=NO
RECOMMEND_AS_VALIDATED_MEDICAL_RESEARCH_PRODUCT=NO
```

### Reasons Not to Recommend（不推荐原因）

| 不推荐原因 | 风险 | 本次修正 | 剩余状态 |
|---|---|---|---|
| 没有 Agent、Runtime 或真实集成 | 客户可能把规范误读为可运行产品 | 全仓使用 `specification-only`、`design-only` 和零状态 | 实现仍未授权 |
| 没有 DBOS/SAEE 操作契约或记录 | Reference 可能被误读为已完成集成 | 分别建立 DBOS 与 SAEE 边界模型 | API、Schema 和集成仍不存在 |
| 没有实验或 Benchmark 结果 | 不能声称提高可复现性 | 定义三条件对照、指标、偏差和执行闸门 | 计划尚未预注册或执行 |
| 医学影像属于高风险语境 | 可能产生诊断、伦理、隐私和有效性误读 | 将目标限于 Workflow Reproducibility，并设置人工与数据闸门 | 数据、伦理和领域复核仍未批准 |
| AI Output 容易被误写成科学真相 | 可能造成不当结论或发表 | 固定 `AI Output != Scientific Truth` 和 Self Certification 禁令 | 未来仍需独立实证检查 |

### Post-correction Recognition（修正后认可）

修正后的智能体结论：

```text
AGENT_REVIEW_OUTCOME=ACCEPTED_FOR_PROJECT_INITIALIZATION_ONLY
SPECIFICATION_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
IMPLEMENTED_PROGRAM_RECOMMENDATION=NOT_RECOMMENDED
IMPLEMENTATION_AUTHORIZED=false
```

这表示仓库足以作为可发现、可审查的 Pilot 规范入口；不表示智能体认可其为可运行程序、客户可用产品或已验证科研方法。

## Alternatives Considered（考虑过的替代方案）

### Alternative A: Put the Pilot in DBA（把 Pilot 放入 DBA）

拒绝。DBA 应保持公共意义、规则与架构层；应用实验会使 Architecture 与 Execution 边界模糊。DBA 中已有的设计规范可以作为上位参考，但不替代独立应用仓库。

### Alternative B: Implement the Pilot in DBOS（在 DBOS 中实现 Pilot）

拒绝。DBOS 是 Infrastructure，不是 Research Agent application；把应用放入 DBOS 会扩大核心基础设施职责。

### Alternative C: Implement the Pilot in SAEE（在 SAEE 中实现 Pilot）

拒绝。SAEE 负责 Evaluation，不负责执行科研 Agent 或决定论文结论。

### Alternative D: Keep Only a Concept Note（只保留概念说明）

拒绝。独立、agent-readable（智能体可读）的规范、实验计划和证据边界更容易被检索、审计和未来复用，同时仍能保持零实现状态。

## Consequences（后果）

正面后果：

- Digital Biosphere 获得清楚的第一个应用层实验入口；
- DBA、DBOS、SAEE 与 Pilot 的所有权保持分离；
- 未来实验具备人工监督、对照设计和证据保留基础；
- 智能体可以快速识别当前事实状态和禁止边界。

代价与限制：

- 需要维护跨仓库术语与引用一致性；
- 独立仓库不会自动产生 DBOS 或 SAEE 集成；
- 在实施、数据、伦理、预注册和人工授权完成前，项目只能被描述为规范。

## Current Decision Boundary（当前决定边界）

```text
INDEPENDENT_REPOSITORY_CREATED=true
PROJECT_SPECIFICATION_ACCEPTED=true
Agent=0
Runtime=0
Digital Entity=0
Permission=0
Execution=0
DBOS_MODIFIED=false
SAEE_MODIFIED=false
DBA_MODIFIED=false
```
