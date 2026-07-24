---
checklist_id: DBRAP-PREREGISTRATION-0.1
status: TEMPLATE_NOT_COMPLETED
preregistered: false
experiment_authorized: false
---

# Experiment Preregistration Checklist v0.1（实验预注册清单 v0.1）

## 1. Purpose（目的）

本 Checklist（清单）定义 Human Research Owner 与方法 Reviewer 在任何实验执行前必须冻结的研究决定。它不是 Preregistration Record（预注册记录），也不创建 Experiment Authorization。

```text
Preregistration ≠ Experiment Authorization
Preregistration ≠ Scientific Validity
Checklist Completion ≠ Experiment Execution
```

当前待审版本集合已记录为 [`protocol-freeze-candidate.yaml`](protocol-freeze-candidate.yaml)。该文件只固定候选文件路径、当前状态和 `sha256`，状态为 `DRAFT_FREEZE_CANDIDATE_NOT_APPROVED`；它不是 Preregistration、Human Approval 或 Experiment Authorization。

## 2. Ownership and Authorization（所有权与授权）

- [ ] Human Research Owner Record 已存在且状态为 `ASSIGNED`；
- [ ] Human Reviewer、方法 Reviewer 和角色冲突已记录；
- [ ] Context Package 与 Human Review Record 版本已冻结；
- [ ] `protocol-freeze-candidate.yaml` 中所有路径与 `sha256` 已由人类复核，修订后形成新的 Final Freeze Record；
- [ ] Prototype Authorization 已单独记录；
- [ ] Experiment Authorization 将在 Preregistration 完成后单独决定。

## 3. Research Question and Hypotheses（研究问题与假设）

- [ ] 主要研究问题文本与 [`research-question.md`](research-question.md) 一致；
- [ ] Primary / Secondary Hypotheses（主要/次要假设）已记录，或明确声明无方向性假设；
- [ ] Confirmatory（验证性）与 Exploratory（探索性）分析已区分；
- [ ] 不使用“AI 更聪明”等未操作化成功标准。

## 4. Conditions and Tasks（条件与任务）

- [ ] Human-only、Generic AI Assistant、Governed Research Agent 三条件已冻结；
- [ ] 四项 Task 的 ID、版本、输入、输出和停止条件已冻结；
- [ ] Source Documents、Context 和访问边界在条件间可比较；
- [ ] 时间、工具、人工干预和资源预算已记录；
- [ ] Task/Condition 偏离的记录与处理规则已定义。

## 5. Sample and Allocation（样本与分配）

- [ ] Experimental Unit（实验单元）已定义；
- [ ] 样本量、重复次数和依据已记录；
- [ ] Randomization（随机化）或其不可行性已说明；
- [ ] Counterbalancing（顺序平衡）与学习效应控制已说明；
- [ ] 纳入、排除和停止标准已预先定义。

## 6. Metrics and Analysis（指标与分析）

- [ ] Reproducibility 的 Rubric、单位和计算已冻结；
- [ ] 五个 Secondary Metrics 的 Rubric 已冻结；
- [ ] Reviewer 数量、训练与一致性评估已定义；
- [ ] Missing Data（缺失数据）、Failure、Unknown 和不可比较单元处理已定义；
- [ ] 统计模型、阈值、权重、多重比较和敏感性分析已定义；
- [ ] 不使用单一总分隐藏失败或负面结果。

## 7. Evidence and Verification（证据与验证）

- [ ] Experiment Record、Evidence Record、Verification Result 和 Evaluation Result 模板版本已冻结；
- [ ] Input → Action → Human Review → Output → Evidence Reference 流程已接受；
- [ ] 原始材料、Human Edit、失败、拒绝和 Protocol Deviation 的版本规则已定义；
- [ ] Verifier、Verification Scope 和 Method 已明确；
- [ ] Record 保存位置、访问控制、摘要和保留期已定义。

## 8. Ethics, Data, Privacy, and Safety（伦理、数据、隐私与安全）

- [ ] 数据 Owner、访问、用途和保留决定已记录；
- [ ] Ethics Review（伦理审查）要求和状态已记录；
- [ ] 医学影像、隐私、临床非适用性和安全边界已记录；
- [ ] 外部模型/工具的数据发送边界已明确；
- [ ] 未解决项保持 Unknown，不得以 Checklist 完整性推测批准。

## 9. Failure and Publication Boundary（失败与发表边界）

- [ ] 失败、拒绝、负面和 `INCONCLUSIVE` 结果必须保留；
- [ ] 不自动署名、投稿、发表或对外发送；
- [ ] Experiment Result ≠ Publication Claim；
- [ ] Draft Paper ≠ Accepted Paper；
- [ ] Human Research Owner 保留科学结论和发表责任。

## 10. Completion Record（完成记录）

- Preregistration ID：`NOT_ASSIGNED`
- Protocol Version：`v0.1`
- Context Version：`NOT_BOUND`
- Prototype Version：`v0.1`
- Completed By：`NOT_ASSIGNED`
- Reviewed By：`NOT_ASSIGNED`
- Timestamp：`NOT_RECORDED`
- Status：`NOT_PREREGISTERED`

```text
PREREGISTRATION_CHECKLIST_DEFINED=true
PROTOCOL_FREEZE_CANDIDATE_PREPARED=true
PROTOCOL_FREEZE_CANDIDATE_STATUS=DRAFT_FREEZE_CANDIDATE_NOT_APPROVED
PROTOCOL_FREEZE_ARTIFACTS=17
PROTOCOL_FREEZE_APPROVED=false
PREREGISTRATION_COMPLETED=false
PREREGISTERED=false
EXPERIMENT_AUTHORIZED=false
EXPERIMENT_EXECUTED=false
```
