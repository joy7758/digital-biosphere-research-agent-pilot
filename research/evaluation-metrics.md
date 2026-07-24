---
metrics_id: DBRAP-EVALUATION-METRICS-0.1
status: DRAFT_NOT_PREREGISTERED
primary_metric: reproducibility
secondary_metric_count: 5
scores_computed: false
---

# Evaluation Metrics v0.1（评价指标 v0.1）

## 1. Boundary（边界）

本文件定义未来比较实验的一个 Primary Metric（主要指标）与五个 Secondary Metrics（次要指标）。当前没有冻结 Rubric、阈值、权重、样本量或统计方法，也没有计算任何分数。

```text
Metric Definition ≠ Metric Result
Metric Result ≠ Scientific Truth
Higher Score ≠ Smarter AI
```

禁止使用“AI 更聪明”“输出更像专家”“感觉更好”等未操作化的主观指标。

## 2. Primary Metric: Reproducibility（主要指标：可复现性）

### Evaluation Question（评价问题）

独立 Reviewer 能否仅依赖保存的输入、版本、步骤、工具、输出、人工修改和限制，重建工作流并得到预注册意义下的 comparable outcome（可比较结果）？

### Candidate Components（候选组成）

- Procedure Reconstruction Coverage（程序重建覆盖率）；
- Version Reconstruction Coverage（版本重建覆盖率）；
- Independent Replay Agreement（独立复现一致性）；
- Unexplained Divergence Count（无法解释的偏差数量）。

具体公式、权重和可接受差异必须在实验前预注册。无法重建或缺失记录不能自动按零分处理后隐藏原因；必须同时记录 Failure 与 Unknown。

## 3. Secondary Metric: Evidence Completeness（次要指标：证据完整性）

评价必需 Input、Action、Human Review、Output、Failure、Version、Limitation 和 Evidence Reference 字段的覆盖情况。

候选计算：

```text
explicitly_present_required_fields / applicable_required_fields
```

显式 `unknown` 可以作为“状态已记录”，但不能作为“事实已提供”。必须分别报告结构完整性与内容可验证性。

## 4. Secondary Metric: Traceability（次要指标：可追溯性）

评价输出主张、步骤和人工决定能否回溯到具体输入、来源版本、Action、Review 和 Evidence Record。

候选计算：

```text
sampled_items_with_complete_reference_chain / sampled_items_reviewed
```

引用链存在不表示主张正确；Broken、Ambiguous 和 Unknown 链必须单独报告。

## 5. Secondary Metric: Human Review Efficiency（次要指标：人工复核效率）

在 Review Quality Guardrail（复核质量护栏）不下降的前提下，记录：

- Human Review 时间；
- 人工操作与往返次数；
- Revision 次数；
- 未解决问题数量；
- Reviewer 间分歧处理成本。

更快但漏检更多错误、Unknown 或越权内容不能被判为效率改善。

## 6. Secondary Metric: Error Detection（次要指标：错误发现）

评价工作流识别预先确认或事后经独立 Human Review 确认的来源错误、版本冲突、范围越界、缺失 Evidence 和不一致的能力。

候选计算：

```text
verified_errors_detected / eligible_verified_errors
```

“错误真值集合”必须独立建立并记录来源；不能由被评价 Agent 自己定义。

## 7. Secondary Metric: Unknown Preservation（次要指标：未知保留）

评价输入中的已知 Unknown 是否在 Action、Output、Human Review 和 Analysis 中继续保持 Unknown，除非有可定位的人工确认解决记录。

至少报告：

- Preserved Unknown Count（保留未知数量）；
- Unsupported Resolution Count（无依据解决数量）；
- Omitted Unknown Count（遗漏未知数量）；
- Newly Identified Unknown Count（新识别未知数量）。

Unknown 数量更多或更少都不自动表示更好；重点是是否诚实保留与可解释解决。

## 8. Cross-metric Rules（跨指标规则）

- 不得用一个总分隐藏失败、负面或 Unknown；
- Primary 与每个 Secondary 必须分别报告；
- 缺失数据、不可比较单元和 Protocol Deviation 必须显式呈现；
- 条件间比较必须使用相同 Rubric 与冻结版本；
- Human Review Efficiency 必须同时报告 Error Detection 与 Unknown Preservation；
- 任何统计显著性都不自动产生实际意义、科学有效性或 Publication Claim。

## 9. Preregistration Gaps（预注册缺口）

当前仍需 Human Research Owner 与方法 Reviewer 决定：

- Rubric 项目和评分单位；
- Reviewer 数量、训练和一致性测量；
- 样本量与统计模型；
- 阈值、权重和聚合策略；
- 缺失值、失败和不可比较单元处理；
- 多重比较和敏感性分析；
- Quality Guardrail 与停止条件。

## 10. Current State（当前状态）

```text
EVALUATION_METRICS_DEFINED=true
PRIMARY_METRIC=REPRODUCIBILITY
SECONDARY_METRICS=5
SUBJECTIVE_AI_SMARTNESS_METRIC_ALLOWED=false
METRICS_PREREGISTERED=false
METRIC_RESULTS_CREATED=0
```
