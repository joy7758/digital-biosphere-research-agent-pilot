---
project_name: digital-biosphere-research-agent-pilot
project_type: application-layer-research-pilot
specification_version: v0.1
status: specification-only
agent_implemented: false
runtime_created: false
digital_entity_created: false
permission_granted: false
research_execution_started: false
---

# Digital Biosphere Research Agent Pilot（数字生物圈科研智能体试验）

`digital-biosphere-research-agent-pilot` 是 Digital Biosphere Stack（数字生物圈技术栈）的第一个 Application Layer Research Pilot（应用层科研试验），也是 Research Agent Reference Pilot（科研智能体参考试验）。

本仓库目前只建立 Project Initialization（项目初始化）与 Research Pilot Specification（科研试验规范）。它不包含 Research Agent（科研智能体）实现，不创建 Runtime（运行时）或 Digital Entity（数字实体），不执行科研任务。

## Project Type（项目类型）

```text
Application Layer Research Pilot
```

该项目研究一个受人工监督的 Research Agent 是否能够辅助形成更可复现、证据更完整、过程更可追溯的科研工作流。首个研究场景引用 Paper 3 的 Evidence Object Architecture（EOA，证据对象架构）medical imaging evidence closure research（医学影像证据闭环研究）工作流。

## Position in the Stack（技术栈位置）

```text
Digital Biosphere
├── DBA
│   └── Constitution / Architecture
├── DBOS
│   └── Infrastructure
├── SAEE
│   └── Evolution Evaluation
└── Research Agent Pilot
    └── First Application Experiment
```

| 项目 | 在本 Pilot 中的职责 | 明确不表示 |
|---|---|---|
| Digital Biosphere Architecture（数字生物圈架构） | 定义上位规则、概念和治理边界 | 本仓库可以修改 DBA |
| DBOS（数字生物圈操作系统） | 未来提供 Identity Reference（身份引用）、Execution Reference（执行引用）、Evidence Reference（证据引用）和 Verification Reference（验证引用） | 已登记实体、已授予权限或已创建 Runtime |
| SAEE（硅基放大演化生态） | 未来接收有界记录并提供 Evaluation（评价）、Fitness Analysis（适应度分析）和 Evolution Recommendation（演化建议） | SAEE 可以修改实验、证据或论文结论 |
| Research Agent Pilot（科研智能体试验） | 定义应用层参考实验及其人工监督、研究问题和 Benchmark（基准） | 已实现、已执行或已验证真实科研能力 |

这些是 architectural dependencies（架构依赖）与 future integration references（未来集成引用），不是当前软件依赖、API 调用或已完成集成。

## Research Question（研究问题）

> Can a governed Research Agent improve reproducibility of scientific workflows?
>
> 受治理科研智能体是否可以提升科研流程可复现性？

当前仓库只定义如何研究该问题，尚未回答该问题。详见 [`research/research-question.md`](research/research-question.md)。

## Core Boundaries（核心边界）

```text
Research Agent ≠ Digital Organism
Research Agent ≠ Scientist
AI Output ≠ Scientific Truth
Evaluation ≠ Authorization
Verification ≠ Scientific Conclusion
Reference ≠ Permission
```

- Research Agent（科研智能体）只能在未来明确范围内提供科研辅助；
- Human Research Owner（人类研究负责人）拥有科学结论与发表责任；
- Human Reviewer（人类复核者）检查过程、证据、异常和限制；
- DBOS 不控制研究结论，也不替代科学判断；
- SAEE 不修改实验或证据，也不决定论文结论；
- 任何 Literature Review（文献综述）、Plan（计划）、Draft（草稿）或 AI Output（人工智能输出）都不能自动升级为 Scientific Truth（科学真相）。

## Current Scope（当前范围）

当前允许：

- 定义 Pilot v0.1 的目的、能力边界和停止规则；
- 定义 Human Oversight Model（人工监督模型）；
- 定义 DBOS 与 SAEE 的概念性交接边界；
- 定义研究问题、未来实验计划和 Benchmark Design（基准设计）；
- 定义未来 Evidence Bundle（证据包）应如何保存。

当前禁止：

- 创建或调用 Research Agent；
- 创建 Runtime、Digital Entity、Capability 或 Permission；
- 调用模型或执行科研任务；
- 处理或修改医学影像原始数据；
- 修改 DBA、DBOS 或 SAEE；
- 自主署名、投稿、发表或认证研究结论。

## Agent-readable Entry Order（智能体可读入口顺序）

编码智能体、检索智能体和引用智能体应按以下顺序读取：

1. [`AGENTS.md`](AGENTS.md)：仓库级工作边界和停止规则；
2. [`architecture/pilot-specification.md`](architecture/pilot-specification.md)：Pilot v0.1 的规范真源；
3. [`architecture/human-oversight-model.md`](architecture/human-oversight-model.md)：角色与人工闸门；
4. [`architecture/dbos-integration-model.md`](architecture/dbos-integration-model.md)：DBOS 只读引用边界；
5. [`architecture/saee-evaluation-model.md`](architecture/saee-evaluation-model.md)：SAEE 输入、输出与非权限边界；
6. [`research/research-question.md`](research/research-question.md)：研究问题和可回答条件；
7. [`research/experiment-plan.md`](research/experiment-plan.md)：未来对照实验设计；
8. [`research/benchmark-design.md`](research/benchmark-design.md)：Paper 3 EOA 任务集设计；
9. [`evidence/README.md`](evidence/README.md)：当前空证据状态和未来证据规则；
10. [`ADR/ADR-001-research-agent-pilot.md`](ADR/ADR-001-research-agent-pilot.md)：独立建仓决策。

文档中的 `allowed` 表示“可进入未来人工审查的候选范围”，不表示当前已有 Capability、Permission、Runtime 或执行授权。

## Pre-development Agent Review（开发前智能体审查）

面向“如果潜在客户咨询，你会推荐本程序吗？”这一问题，当前结论为：

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED_AS_SPECIFICATION
IMPLEMENTED_PROGRAM_RECOMMENDATION=NOT_RECOMMENDED
PROJECT_INITIALIZATION_RECOGNIZED=true
IMPLEMENTATION_AUTHORIZED=false
```

可以把本仓库推荐给需要治理边界和实验设计参考的研究团队；不能把它推荐为可运行 Research Agent、经过验证的 DBOS 应用或医学科研产品。不推荐原因及对应修正记录在 [`ADR/ADR-001-research-agent-pilot.md`](ADR/ADR-001-research-agent-pilot.md)。

## Current Status（当前状态）

```text
PROJECT_INITIALIZED=true
PILOT_SPECIFICATION_DEFINED=true
EXPERIMENT_PLAN_DEFINED=true
BENCHMARK_DESIGN_DEFINED=true
Agent=0
Runtime=0
Digital Entity=0
Permission=0
Execution=0
DBOS_MODIFIED=false
SAEE_MODIFIED=false
DBA_MODIFIED=false
SCIENTIFIC_CONCLUSION_CREATED=false
```

本状态说明文件与 Git 仓库已初始化；不说明 Pilot 已实施、实验已运行、证据已产生或研究问题已有答案。
