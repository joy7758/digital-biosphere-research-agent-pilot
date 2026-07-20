---
benchmark_id: DBRAP-EOA-BENCHMARK-0.1
source_scope: Paper-3-EOA-research-workflow
status: definition-only
dataset_created: false
tasks_executed: false
---

# Benchmark Design v0.1（基准设计 v0.1）

## 1. Source Scope（来源范围）

未来 Benchmark（基准）的实验数据与任务语境来源于 Paper 3 的 Evidence Object Architecture（EOA，证据对象架构）medical imaging evidence closure research（医学影像证据闭环研究）工作流。

当前没有把 Paper 3 数据、医学影像、论文草稿或 Evidence 复制到本仓库。本文件只定义候选任务类型。

## 2. Benchmark Objective（基准目标）

比较三个实验条件在相同任务输入下组织可复现科研过程的能力，而不是测试医学诊断能力、临床性能或论文结论正确性。

```text
BENCHMARK_TARGET=WORKFLOW_REPRODUCIBILITY
BENCHMARK_TARGET_NE_MEDICAL_DIAGNOSIS=true
BENCHMARK_TARGET_NE_CLINICAL_VALIDATION=true
BENCHMARK_TARGET_NE_EOA_SCIENTIFIC_PROOF=true
```

## 3. Task Families（任务族）

### 3.1 Literature Tasks（文献任务）

候选任务：

- 根据给定问题定位相关来源；
- 提取可核验的主张、方法、限制和引用位置；
- 比较来源间的一致、冲突和未知项；
- 形成不超出来源证据的 Literature Map（文献图谱）。

未来评分关注来源准确性、版本记录、引用可定位性、冲突保留和过度概括。

### 3.2 Experiment Planning Tasks（实验规划任务）

候选任务：

- 从明确研究问题形成变量、对照和步骤候选；
- 标记数据、工具、环境、复核和停止条件；
- 识别替代解释、偏差、风险和缺失授权；
- 生成供 Human Research Owner 审批的非执行计划。

未来评分关注计划可复核性、约束覆盖、风险识别和不当自动执行边界。

### 3.3 Evidence Organization Tasks（证据整理任务）

候选任务：

- 连接输入、过程、输出、版本和责任角色；
- 保留失败、负面、冲突和 inconclusive 记录；
- 构造供 DBOS Reference 与人工复核使用的 Evidence Index（证据索引）；
- 检查缺失引用和不可解释状态，但不补造 Evidence。

未来评分关注完整性、可追溯性、历史保留和 unknown（未知）状态的诚实表达。

## 4. Case Definition Requirements（用例定义要求）

每个未来 Benchmark Case（基准用例）至少要有：

- `case_id`：稳定标识符；
- `task_family`：任务族；
- `source_version`：来源版本；
- `input_scope`：允许输入；
- `prohibited_actions`：禁止行为；
- `expected_artifacts`：预期材料，不是标准答案；
- `review_rubric`：人工评分规则；
- `known_unknowns`：已知未知项；
- `stop_conditions`：停止条件。

这些字段是设计要求，不是已创建 Schema 或 Dataset（数据集）。

## 5. Leakage and Fairness Controls（泄漏与公平控制）

- 冻结每个条件可访问的相同来源版本；
- 防止测试答案、人工评分或其他条件输出泄漏；
- 区分 Agent 生成内容与 Human Edit（人工编辑）；
- 记录每个条件的工具、时间和干预；
- 不因某个条件产生更多日志就自动给出更高完整性分；
- 将缺失数据、不可比较结果和协议偏差保留为异常，而不是丢弃。

## 6. Current Status（当前状态）

```text
BENCHMARK_DESIGN_DEFINED=true
BENCHMARK_SCHEMA_CREATED=false
BENCHMARK_CASES_CREATED=0
PAPER_3_DATA_IMPORTED=false
MEDICAL_IMAGE_DATA_IMPORTED=false
BENCHMARK_FROZEN=false
BENCHMARK_APPROVED=false
BENCHMARK_EXECUTED=false
RESULTS_CREATED=false
```

当前状态为“只定义，不执行”。
