---
document_id: DBRAP-CONTEXT-BACKGROUND-0.1
status: draft-context-source
human_approved: false
scientific_truth_claimed: false
---

# Research Agent Pilot Project Background（科研智能体试验项目背景）

## 1. Project Purpose（项目目的）

`digital-biosphere-research-agent-pilot` 是 Digital Biosphere Stack（数字生物圈技术栈）的第一个 Application Layer Research Pilot（应用层科研试验）。它定义受人工监督的 Research Agent 未来如何辅助可复现科研工作流。

当前项目已经定义：

- Pilot Specification（试验规范）；
- Human Oversight Model（人工监督模型）；
- DBOS Integration Model（DBOS 集成模型）；
- SAEE Evaluation Model（SAEE 评价模型）；
- Research Question（研究问题）；
- Experiment Plan（实验计划）；
- Benchmark Design（基准设计）。

这些都是 Specification（规范）或 Design（设计），不是 Agent 实现、实验执行、Evidence Truth 或 Research Result。

## 2. Digital Biosphere Stack Relationship（数字生物圈技术栈关系）

| 层 | 职责 | 与本项目的关系 |
|---|---|---|
| DBA | Architecture（架构） | 定义上位概念、规则和治理边界 |
| DBOS | Infrastructure（基础设施） | 未来提供 Identity、Execution、Evidence 和 Verification Reference |
| SAEE | Evaluation（评价） | 未来评价受控的执行、证据和验证记录 |
| Research Agent Pilot | Application Research（应用研究） | 定义科研辅助参考实验、上下文、人工监督和研究设计 |

```text
Research Agent Pilot ≠ DBOS
Research Agent Pilot ≠ SAEE
Research Agent Pilot ≠ DBA
```

本项目不复制、替代或修改三者的规范事实真源。

## 3. Research Context Need（研究上下文需求）

未来 Research Agent 不应因自动读取大量 Chat History（聊天历史）而获得未审查背景。它应从版本化、来源明确、Unknown 保留且经过人类确认的 Context Package 进入科研流程。

Context Package 可以包含研究背景、已确认研究决策、Evidence Reference、外部来源引用和 Unknown，但不能把其中任何内容自动升级为 Scientific Truth。

## 4. Current Boundary（当前边界）

```text
PROJECT_BACKGROUND_DEFINED=true
PROJECT_BACKGROUND_APPROVED=false
CHAT_HISTORY_READ=false
SOURCE_DOCUMENTS_IMPORTED=0
SCIENTIFIC_CONCLUSION_CREATED=false
RESEARCH_RESULT_CREATED=false
```
