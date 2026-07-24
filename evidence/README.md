---
evidence_state: empty
evidence_records: 0
execution_records: 0
verification_records: 0
saee_evaluations: 0
---

# Evidence Directory（证据目录）

本目录为未来 Research Agent Pilot（科研智能体试验）的 Evidence Boundary（证据边界）说明。当前没有实验、执行、Benchmark、DBOS、SAEE 或科研结论 Evidence。

```text
EVIDENCE_DIRECTORY_DEFINED=true
EVIDENCE_PLAN_DEFINED=true
EVIDENCE_BUNDLE_CREATED=false
EVIDENCE_RECORDS=0
EXECUTION_RECORDS=0
VERIFICATION_RECORDS=0
SAEE_EVALUATIONS=0
```

## Future Evidence Classes（未来证据类别）

在另行批准并执行实验后，候选 Evidence Bundle 至少应区分：

- Input Evidence（输入证据）：任务、来源、版本、范围和授权引用；
- Process Evidence（过程证据）：步骤、工具、版本、人工干预、失败和停止；
- Output Evidence（输出证据）：草稿、索引、计划和结构化材料；
- Review Evidence（复核证据）：Reviewer 意见、分歧、修订和 Owner 决定；
- Verification Evidence（验证证据）：验证主体、范围、方法、结果和限制；
- Evaluation Evidence（评价证据）：SAEE 输入范围、输出维度和 Recommendation 限制。

流程规范见 [`research-evidence-model.md`](research-evidence-model.md)，未来空 Record 结构见 [`evidence-record-template.yaml`](evidence-record-template.yaml)。二者都是准备材料，不是 Evidence Record 实例。

## Preservation Rules（保留规则）

- 原始材料只读保存；转换材料必须与原始材料分离；
- 失败、负面、中间、冲突和 inconclusive 结果不得删除；
- 每个材料记录来源、版本、时间、责任角色和限制；
- AI Output 与 Human Edit 必须可区分；
- DBOS Reference 不能替代实际 Evidence；
- Evidence Completeness 不能写成 Scientific Truth；
- 未知、缺失和未验证状态不得推测补齐；
- 敏感或受限医学数据不得因本目录存在而被复制进仓库。

## Current Boundary（当前边界）

本 README 是目录说明，不是 Evidence Record（证据记录）。项目初始化 commit 只证明规范文件进入版本控制，不证明科研实验、DBOS 集成或 SAEE 评价发生。
