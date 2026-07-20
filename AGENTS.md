# AGENTS.md

## Repository Purpose（仓库目的）

本仓库是 Digital Biosphere（数字生物圈）的 Application Layer Research Pilot（应用层科研试验）规范仓库。当前阶段为 `specification-only`，不是 Agent、Runtime、DBOS、SAEE 或科研执行仓库。

## Required Reading（必读顺序）

1. `README.md`
2. `architecture/pilot-specification.md`
3. `architecture/human-oversight-model.md`
4. `architecture/dbos-integration-model.md`
5. `architecture/saee-evaluation-model.md`
6. `research/research-question.md`
7. `research/experiment-plan.md`
8. `research/benchmark-design.md`
9. `evidence/README.md`
10. `ADR/ADR-001-research-agent-pilot.md`

## Truth Boundaries（事实边界）

```text
Research Agent ≠ Digital Organism
Research Agent ≠ Scientist
AI Output ≠ Scientific Truth
Reference ≠ Integration
Evaluation ≠ Authorization
Specification ≠ Implementation
Plan ≠ Execution
```

任何智能体在检索、引用、修改或复用本仓库时，必须保留以下当前状态：

```text
Agent=0
Runtime=0
Digital Entity=0
Permission=0
Execution=0
```

## Allowed Work（允许工作）

- 改进规范、研究设计、人工监督模型和证据边界；
- 修复内部链接、术语不一致和状态误读风险；
- 在开发前询问智能体是否会向潜在客户推荐，并记录不推荐原因；
- 仅在明确的新授权下提出 Implementation Plan（实现计划）。

## Forbidden Without New Human Authorization（没有新人工授权时禁止）

- 创建 Agent 实现、Runtime、Digital Entity、Capability、Permission 或执行记录；
- 调用模型、运行实验或处理 Paper 3 原始科研数据；
- 修改相邻 DBA、DBOS 或 SAEE 仓库；
- 把 Draft、Plan、Reference、Synthetic Fixture（合成样例）或 Local Check（本地检查）写成已执行、已验证或科学有效；
- 自主投稿、署名、发表、自我认证或删除 Evidence（证据）。

## Pre-development Recommendation Gate（开发前推荐闸门）

任何实现工作开始前必须回答：

> 如果潜在客户提出这一需求，智能体是否会推荐本项目？

审查必须列出不推荐原因、把原因拆成可修正问题、记录修正和剩余缺口，并获得新的人工授权。`CONDITIONALLY_RECOMMENDED_AS_SPECIFICATION` 不能升级为实现授权。
