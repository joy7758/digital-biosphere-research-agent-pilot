---
evidence_context_status: reference-boundary-only
evidence_records: 0
evidence_truth_created: false
---

# Research Context Evidence（研究上下文证据）

本目录定义未来 Context Package 可以引用的 Evidence Source Class（证据来源类别）。当前不复制来源、不生成 Evidence Record，也不产生 Evidence Truth。

未来可引用：

- Papers（论文）：具有稳定题名、作者、版本、标识符或可定位出处的研究材料；
- Datasets（数据集）：具有 Owner、版本、访问、伦理、隐私和使用限制的受控数据引用；
- Experiment Records（实验记录）：具有计划版本、环境、步骤、输出、失败和复核边界的记录；
- External References（外部引用）：具有来源、访问日期、版本或变更风险说明的外部材料。

## Rules（规则）

- 这里只保存 future reference rules（未来引用规则），不把外部内容自动抓入仓库；
- Evidence Reference ≠ Evidence Truth；
- Paper ≠ Accepted Scientific Conclusion；
- Dataset Availability ≠ Data Permission；
- Experiment Record ≠ Valid Experiment Result；
- 来源缺失、冲突或验证不可用时必须记录为 Unknown；
- 医学影像或其他敏感数据不得因 Context Package 存在而被复制进仓库。

## Current State（当前状态）

```text
PAPERS_REFERENCED=0
DATASETS_REFERENCED=0
EXPERIMENT_RECORDS_REFERENCED=0
EXTERNAL_REFERENCES_REFERENCED=0
EVIDENCE_RECORDS_CREATED=0
EVIDENCE_TRUTH_CREATED=false
```
