---
template_id: DBRAP-ANALYSIS-REPORT-0.1
status: EMPTY_TEMPLATE
evaluation_results_bound: 0
analysis_completed: false
scientific_conclusion_created: false
---

# Analysis Report Template v0.1（分析报告模板 v0.1）

> 当前是空 Template。Analysis（分析）必须来自真实、已复核的 Experiment Records、Evidence Records、Verification Results 和 Evaluation Results。

## 1. Analysis Metadata（分析元数据）

- Analysis ID：`NOT_ASSIGNED`
- Protocol / Metrics Versions：`NOT_BOUND`
- Analyst Reference：`NOT_ASSIGNED`
- Human Research Owner：`NOT_ASSIGNED`
- Analysis Status：`NOT_STARTED`

## 2. Input Record Set（输入记录集合）

列出所有纳入、排除和缺失的 Experiment/Evidence/Evaluation Record，以及预注册的排除理由。当前 Record Set：`EMPTY`。

## 3. Analysis Method（分析方法）

记录预注册的统计方法、Rubric 聚合、Reviewer 一致性、缺失值处理、Protocol Deviation、敏感性分析和多重比较处理。当前：`NOT_PREREGISTERED`。

## 4. Primary Metric Result（主要指标结果）

### Reproducibility（可复现性）

- Value：`NO_DATA`
- Uncertainty：`NO_DATA`
- Evidence References：`NONE`
- Limitations：`NOT_ASSESSED`

不得把空模板、预期方向或设计目标填入 Result。

## 5. Secondary Metric Results（次要指标结果）

分别报告：Evidence Completeness、Traceability、Human Review Efficiency、Error Detection 和 Unknown Preservation。当前全部为 `NO_DATA`。

## 6. Cross-condition Comparison（跨条件比较）

分别比较 Human-only、Generic AI Assistant 与 Governed Research Agent，不得把治理条件预设为更优。当前：`NOT_PERFORMED`。

## 7. Successes（成功）

只综合有 Record 和 Evidence Reference 支持的成功。当前：`NONE`。

## 8. Failures and Negative Results（失败与负面结果）

完整呈现失败、拒绝、无改善、反向差异、不可比较与分析失败。当前：`NONE_RECORDED_BECAUSE_NO_EXPERIMENT`。

## 9. Unknowns（未知）

列出输入 Unknown、新发现 Unknown、未解决分歧和不能由数据回答的问题。当前结果方向：`UNKNOWN`。

## 10. Limitations（限制）

覆盖 Internal Validity（内部有效性）、External Validity（外部有效性）、Measurement Validity（测量有效性）、Reviewer Bias（复核偏差）、模型/工具漂移、样本与领域限制、临床非适用性和治理开销。

## 11. Human Interpretation（人工解释）

Human Research Owner 可以记录 `SUPPORTED_WITHIN_SCOPE`、`NOT_SUPPORTED`、`MIXED` 或 `INCONCLUSIVE`，但必须说明 Evidence 范围。当前：`INCONCLUSIVE_NO_EXPERIMENT`。

## 12. Publication Boundary（发表边界）

Analysis Result ≠ Publication Claim。即使分析完成，也需要独立作者审查、Claim-to-Evidence Mapping（主张—证据映射）、Limitations 检查和 Publication Gate。

## 13. Current Template State（当前模板状态）

```text
ANALYSIS_REPORT_TEMPLATE_DEFINED=true
ANALYSIS_REPORT_CREATED=false
EVALUATION_RESULTS_BOUND=0
ANALYSIS_COMPLETED=false
SCIENTIFIC_CONCLUSION_CREATED=false
```
