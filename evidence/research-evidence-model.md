---
spec_id: DBRAP-RESEARCH-EVIDENCE-MODEL-0.1
status: PLAN_DEFINED_NOT_EXECUTED
evidence_records_created: 0
evidence_truth_created: false
---

# Research Evidence Model v0.1（科研证据模型 v0.1）

## 1. Purpose（目的）

本模型定义未来实验如何保存从受控输入到 Human Review 后输出的 Evidence Chain（证据链）。它不生成 Evidence Record，不认证 Evidence Truth，也不修改 DBOS。

## 2. Required Flow（必要流程）

```text
Input
  ↓
Agent Action
  ↓
Human Review
  ↓
Output
  ↓
Evidence Reference
```

对于 Human-only Baseline，`Agent Action` 必须显式记录为 `not_applicable`，并使用可定位的 Human Action（人工行动）记录，不能伪造 Agent 事件以强行匹配流程。

## 3. Evidence Stages（证据阶段）

| 阶段 | 最低记录 | 不表示 |
|---|---|---|
| Input（输入） | Context、Task、Source、版本、限制、Unknown 和授权引用 | 输入正确或可自由使用 |
| Agent Action（智能体行动） | 条件、Actor、工具/模型版本、步骤、停止、失败和中间材料 | 行动成功或合理 |
| Human Review（人工复核） | Reviewer、Rubric、意见、修改、拒绝、分歧和时间 | 输出成为 Scientific Truth |
| Output（输出） | 原始输出、Human Edit、状态、限制和 Unknown | Experiment Result 已确认 |
| Evidence Reference（证据引用） | Record ID、位置、版本、完整性与 Verification 状态 | Evidence Truth、Permission 或 Publication Claim |

## 4. Record Separation（记录分离）

- Experiment Record 保存一个实验单元的条件、任务、授权、时间和结果状态；
- Evidence Record 保存具体材料及其来源、阶段、版本和限制；
- Verification Result 保存验证范围、方法、主体、结果和限制；
- Evaluation Result 保存基于冻结 Metrics 的计算与解释边界；
- Analysis Report 综合已复核结果，但不能追溯性修改任何 Record。

未来 Verification Result 的空结构见 [`verification-result-template.yaml`](verification-result-template.yaml)。模板保持 `result: NOT_VERIFIED`，不是 Verification Result 实例。

这些对象不得相互替代。

## 5. Preservation Rules（保留规则）

以下材料必须保留：

- 成功输出；
- 失败和异常；
- 拒绝与停止；
- Human Revision（人工修改）前后的版本；
- Negative Result（负面结果）；
- Reviewer 分歧；
- Unknown、缺失与不可比较状态；
- Protocol Deviation（协议偏差）；
- 被排除单元及其预注册理由。

```text
FAILURE_MUST_BE_PRESERVED=true
REJECTION_MUST_BE_PRESERVED=true
MODIFICATION_MUST_BE_VERSIONED=true
NEGATIVE_RESULT_MUST_BE_PRESERVED=true
UNKNOWN_MUST_REMAIN_UNKNOWN=true
```

## 6. Immutability and Versioning（不可变性与版本）

- 原始 Input、Action 和 Output 只读保存；
- 修正创建后继版本，不覆盖原记录；
- Human Edit 与 Agent Output 必须可区分；
- 删除请求必须保留治理记录，除非适用隐私或法律要求需要受控删除；
- 受控删除也不能被写成“从未发生”，必须保留允许范围内的删除证明；
- Record ID 与 DBOS Reference 不是同一身份，未来映射必须显式。

## 7. Evidence Acceptance Gate（证据接受闸门）

材料成为可评价 Evidence Record 候选前必须具有：

- 可定位的 Experiment Record；
- Input、Actor、版本和时间；
- Human Review 状态；
- 完整性或缺失声明；
- Unknown 与限制；
- 明确 Evidence Stage；
- 不可变位置或内容摘要计划；
- Verification 状态，即使状态为 `NOT_VERIFIED`。

Evidence Acceptance 不表示 Scientific Validity。

## 8. Future DBOS Projection（未来 DBOS 投影）

未来可以为真实记录建立 Identity、Execution、Evidence 和 Verification Reference。当前只准备引用字段，不调用 DBOS、不写入 DBOS，也不声称引用已解析。

## 9. Current State（当前状态）

```text
EVIDENCE_PLAN_DEFINED=true
EVIDENCE_FLOW_DEFINED=true
EVIDENCE_RECORD_TEMPLATE_DEFINED=true
VERIFICATION_RESULT_TEMPLATE_DEFINED=true
EXPERIMENT_RECORDS=0
EVIDENCE_RECORDS=0
VERIFICATION_RESULTS=0
EVIDENCE_TRUTH_CREATED=false
DBOS_EVIDENCE_REFERENCE_CREATED=false
```
