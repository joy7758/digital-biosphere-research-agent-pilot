---
constitution_id: DBRAP-COMMUNICATION-CONSTITUTION-0.1
status: ACTIVE
scope: REPOSITORY_USER_FACING_COMMUNICATION
owner_reference: "owner://bin-zhang"
effective_date: "2026-07-21"
---

# Repository Communication Constitution v0.1（仓库沟通宪法 v0.1）

## Article 1: Default Language（第一条：默认语言）

所有面向用户的回复默认使用中文。不得把英文作为默认叙述语言。

## Article 2: Mandatory Translation Annotation（第二条：强制翻译备注）

任何面向用户的回复只要出现英文单词、英文短语、英文句子、英文缩写、英文状态名或英文术语，就必须在相邻位置提供中文翻译或中文释义。

合规格式示例：

- `Human Review（人工复核）`；
- `Context Package（研究上下文包）`；
- `REVIEW_PENDING（等待复核）`；
- `DBOS（Digital Biosphere Operating System，数字生物圈操作系统）`。

不允许出现没有中文备注的孤立英文表达。

## Article 3: Exact Identifier Preservation（第三条：精确标识符保持）

文件路径、命令、代码符号、状态常量、分支名、记录编号、提交哈希和统一资源定位符必须保持原样，不得在标识符内部翻译或改写；但必须在紧邻位置增加中文说明。

示例：

- `human-context-decision-record.yaml`（人工上下文决策记录文件）；
- `PENDING_HUMAN_INPUT`（等待人工输入）；
- `HCD-001`（人工上下文决策记录编号）；
- `git status`（查看版本库状态的命令）。

代码块或机器可读清单中如必须保留英文标识符，应在代码块前后提供逐项或分组中文图例，不得依靠用户自行翻译。

## Article 4: Covered Response Surfaces（第四条：适用回复范围）

本规则适用于：

- 中间进度更新；
- 最终答复；
- 澄清问题；
- 状态报告；
- 错误说明；
- 表格、列表和图示；
- 引用、摘要和代码说明。

引用英文原文时，也必须紧邻提供中文翻译或中文释义。

## Article 5: Persistence and Revocation（第五条：持续有效与撤销）

本规则持续适用于本仓库中的后续对话和智能体工作。只有 Human Research Owner（人工研究负责人）明确修改或撤销本宪法条款时，才可停止执行；临时出现英文内容不构成默示撤销。

## Article 6: Architecture Boundary（第六条：架构边界）

本文件是 Research Agent Pilot（科研智能体试验项目）的仓库沟通宪法，只约束本项目的用户沟通和智能体输出。它不修改 DBA（Digital Biosphere Architecture，数字生物圈架构）、DBOS（Digital Biosphere Operating System，数字生物圈操作系统）或 SAEE（Self-Adaptive Evolution Evaluation，自适应演化评估）的架构、代码、权限或状态。

```text
Communication Rule（沟通规则） ≠ Scientific Truth（科学事实）
Communication Rule（沟通规则） ≠ Context Approval（上下文批准）
Communication Rule（沟通规则） ≠ Agent Permission（智能体权限）
```
