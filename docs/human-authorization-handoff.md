---
document_id: DBRAP-HUMAN-AUTHORIZATION-HANDOFF-0.1
status: ACTION_REQUIRED_BY_HUMAN
prototype_authorized: false
experiment_authorized: false
---

# Human Authorization Handoff v0.1（人工授权交接清单 v0.1）

## 1. Current Decision Point（当前决定点）

研究框架、空记录模板和论文准备结构已经建立，Human Research Owner `bin_zhang` 已接受责任，但 Readiness Gate 仍为 `NOT_READY`。本文件把下一步需要 Human Research Owner 亲自完成的动作按依赖顺序列出；它不代填、不代审、不代授权。

```text
HUMAN_ACTION_REQUIRED=true
AUTOMATIC_ADVANCEMENT_ALLOWED=false
```

## 2. Prepared Paper 3 Draft Handoff（已准备的 Paper 3 交接草案）

[`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/README.md`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/README.md) 已把 Paper 3 EOA 的候选材料组织为人工交接入口：

- `owner-discovery-report.yaml` 的候选已由人类确认并解析为 `bin_zhang`；发现证据置信度仍记录为 `MEDIUM`，确认保障级别为 `SELF_ATTESTED_NOT_CRYPTOGRAPHICALLY_VERIFIED`；
- `human-owner-record.yaml` 已建立 `ASSIGNED` Owner Record，Context Manifest 的 `owner_reference` 已更新为 `bin_zhang`；
- `source-candidates.yaml` 列出 10 个候选来源；全部已完成 assistant-prepared verification（辅助核验），原 7 个已有人工选择记录，新增 3 个仍待人工决定，批准和绑定数量为 `0`；
- `research-decisions.yaml` 列出 10 项决策，其中 6 项记录现有规范边界，4 项等待人工确认；
- `unknown-register.yaml` 列出 10 个保持 `UNKNOWN` 的草案项；
- `unknown-record-drafts/` 把 10 个 Unknown 映射为独立、可逐项复核但尚未获人工决定的记录草案；
- `human-context-review-draft.md` 的复核项、Owner、日期和签署均未完成。
- `human-context-review-docket.yaml` 已逐项索引 1 个 Owner、原 7 个来源决定、4 个研究决定和 10 个 Unknown 复核；`HCD-001` 已记录其中 7 个来源决定、3 个研究决定和 10 个 Unknown disposition。新增三项由 `human-source-decision-addendum-v0.1.yaml` 提供零预选入口，当前决定均为 `null`；`RD-009` 与 Human Review 仍为 Pending（待定）。
- `human-context-decision-input-template.yaml` 提供覆盖所有待定项的零预选机器可读输入面；它不是 Human Decision 或 Review Record。
- `human-context-decision-record.yaml` 已由 Human Research Owner 明确更新为 `HUMAN_CONFIRMED`；23 个决定条目已记录，`RD-009` 与独立复核者要求仍待决定，Human Review 尚未完成。

因此 Step A 已完成，Step B 的 Human Decision 已记录但尚未转换为正式 Source / Unknown Records，Step C 的 Human Review 尚未完成。Owner Assignment 与 `HCD-001` 都不等于 Approved Source Set（已批准来源集）、Human-reviewed Unknown Record、Context Review 或实验授权。

## 3. Step A: Establish Research Ownership（建立研究所有权）

1. 人类先复核 [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/owner-discovery-report.yaml`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/owner-discovery-report.yaml) 与 [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/candidate-owner.yaml`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/candidate-owner.yaml)，明确确认、纠正或拒绝候选身份；
2. 只有候选本人或明确授权的人类可以确认是否接受 Human Research Owner 的最终科学责任；
3. 确认后复制 [`../research-context/human-owner-record-template.yaml`](../research-context/human-owner-record-template.yaml) 为新的 Owner Record；
4. 填写可定位的 `human_owner_reference`、责任范围和冲突披露；
5. 由人类确认最终科学决定、署名和发表责任；
6. 不要修改模板本身或候选发现记录来伪装 Record 实例。

完成证据：一个具有独立 ID、时间、记录者且状态为 `ASSIGNED` 的真实 Owner Record。

当前完成证据：[`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-owner-record.yaml`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-owner-record.yaml)，`status: ASSIGNED`，`human_owner_reference: bin_zhang`。本 Step 已完成；不得重复创建第二个冲突 Owner Record。

## 4. Step B: Establish Sources and Unknowns（建立来源与未知项）

1. 每个来源使用 [`../research-context/references/source-document-template.yaml`](../research-context/references/source-document-template.yaml) 创建独立 Record；
2. 先复核 [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/source-verification-report.yaml`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/source-verification-report.yaml) 与 [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/source-verification-addendum-v0.2.yaml`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/source-verification-addendum-v0.2.yaml) 中的路径、哈希、状态与限制；Assistant Recommendation 不得直接转换为 Human Decision；
3. 使用 [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/source-record-drafts/README.md`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/source-record-drafts/README.md) 中 10 个草案逐项记录 Human Decision；新增三项的人工输入使用 [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-source-decision-addendum-v0.1.yaml`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-source-decision-addendum-v0.1.yaml)；确认后另建正式 Source Record，不原地把草案改成已批准记录；
4. 记录身份、版本、出处、访问限制和 Known Limitation；
5. 先复核 [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/unknown-record-drafts/README.md`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/unknown-record-drafts/README.md) 中的 10 个逐项草案；人工决定后再使用 [`../research-context/unknowns/unknown-record-template.yaml`](../research-context/unknowns/unknown-record-template.yaml) 另建正式 Record，不原地升级草案；
6. 复核 [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/context-review-recommendation.yaml`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/context-review-recommendation.yaml)；对 `UNK-006` 的建议解决和其余 9 项 `KEEP_UNKNOWN` 分别作出人类决定；
7. 把真实 Record Reference 添加到新的 Context Package 版本；
8. 不自动读取 Chat History、浏览历史或模型记忆。

完成证据：`source_documents` 不再依赖隐式来源，Unknown 具有真实 Record ID；这仍不表示来源被验证为正确。

## 5. Step C: Complete Human Context Review（完成人工上下文复核）

1. 按 [`human-decision-process.md`](human-decision-process.md) 由 Human Research Owner 填写 [`../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-record.yaml`](../research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-record.yaml)；AI 不能选择或推断决定；
2. 使用 [`../research-context/human-review-checklist.md`](../research-context/human-review-checklist.md) 审查特定 `context_id/version`；
3. 从 [`../research-context/review-record-template.yaml`](../research-context/review-record-template.yaml) 创建独立 Review Record；
4. Human Reviewer 记录 Sources、Unknown、限制与异议；
5. Human Research Owner 决定 `REVIEWED`、`APPROVED` 或 `REJECTED`；
6. Review 状态与 Context Manifest 状态分别由人类记录，不自动同步。

Readiness Gate 最低要求为 Context `REVIEWED`；Context Approval 仍不是 Agent Authority。

## 6. Step D: Re-evaluate Prototype Readiness（重新评估原型就绪）

逐项重新执行 [`../architecture/research-agent-readiness-gate.md`](../architecture/research-agent-readiness-gate.md)。只有全部前提具有直接证据，Human Research Owner 才能考虑从 [`../prototype/prototype-authorization-template.yaml`](../prototype/prototype-authorization-template.yaml) 创建真实 Prototype Authorization Record。

```text
READY_FOR_PROTOTYPE ≠ PROTOTYPE_CREATED
PROTOTYPE_AUTHORIZED ≠ EXPERIMENT_AUTHORIZED
```

## 7. Step E: Preregister and Authorize Experiment（预注册并授权实验）

1. 完成 [`../research/preregistration-checklist.md`](../research/preregistration-checklist.md)；
2. 复核 [`../research/protocol-freeze-candidate.yaml`](../research/protocol-freeze-candidate.yaml) 中 17 个候选文件路径、状态和 `sha256`；按人工决定修订后另建 Final Freeze Record，不把候选清单改写成已批准记录；
3. 冻结 Protocol、Tasks、Metrics、Evidence Plan、Context、Sources、模型/工具和环境版本；
4. 完成数据、伦理、隐私和安全决定；
5. 由 Human Research Owner 从 [`../research/experiment-authorization-template.yaml`](../research/experiment-authorization-template.yaml) 创建独立 Experiment Authorization Record；
6. 授权必须规定条件、任务、run limit（运行次数上限）、有效期和撤销方式。

没有 Experiment Authorization 时，不得调用外部模型或创建 Experiment Record。

## 8. Step F: Execute and Preserve Records（执行并保留记录）

只有前五步全部通过后，未来执行才可以：

- 为每个实验单元创建真实 Experiment Record；
- 为 Input、Action、Human Review、Output 和 Failure 创建 Evidence Record；
- 使用 [`../evidence/verification-result-template.yaml`](../evidence/verification-result-template.yaml) 派生真实 Verification Result；
- 使用冻结 Metrics 形成 Evaluation Result；
- 保留失败、拒绝、负面、修改、Unknown 和 Protocol Deviation。

执行仍不自动产生 Scientific Conclusion 或 Publication Claim。

## 9. Current Handoff State（当前交接状态）

```text
OWNER_RECORD_INSTANCE_CREATED=true
HUMAN_RESEARCH_OWNER_ASSIGNED=true
HUMAN_RESEARCH_OWNER_REFERENCE=bin_zhang
OWNER_CANDIDATES_DISCOVERED=1
OWNER_CANDIDATE_STATUS=CONFIRMED_AND_ASSIGNED
OWNER_DISCOVERY_CONFIDENCE=MEDIUM
OWNER_CONFIRMATION_REQUIRED=false
INDEPENDENT_HUMAN_REVIEWER_REQUIRED=UNKNOWN
CONTEXT_HANDOFF_STATUS=DRAFT_PENDING_HUMAN_CONTEXT_REVIEW
HUMAN_CONTEXT_REVIEW_DOCKET_PREPARED=true
HUMAN_CONTEXT_REVIEW_DOCKET_STATUS=REVIEW_PENDING_HUMAN_SOURCE_AND_CONTEXT_DECISIONS
HUMAN_CONTEXT_DECISION_INPUT_TEMPLATE_PREPARED=true
HUMAN_CONTEXT_DECISION_RECORD_PREPARED=true
HUMAN_CONTEXT_DECISION_RECORD_STATUS=HUMAN_CONFIRMED
HUMAN_CONTEXT_DECISIONS_STATUS=RECORDED
RECORDED_SOURCE_DECISIONS=7
PENDING_SOURCE_DECISIONS=3
RECORDED_RESEARCH_DECISIONS=3
PENDING_RESEARCH_DECISIONS=1
RECORDED_UNKNOWN_DISPOSITIONS=10
PENDING_UNKNOWN_REVIEWS=10
CONTEXT_REVIEW_RECOMMENDATION_PREPARED=true
HUMAN_CONTEXT_DECISIONS_RECORDED=23
SOURCE_CANDIDATES=10
SOURCE_CANDIDATES_VERIFIED_FOR_HUMAN_REVIEW=10
SOURCE_CANDIDATES_PENDING_VERIFICATION=0
SOURCE_VERIFICATION_STATUS=VERIFIED_FOR_HUMAN_REVIEW_NOT_APPROVED
SOURCE_RECORD_DRAFTS=10
SOURCE_RECORD_INSTANCES=0
DRAFT_UNKNOWN_ENTRIES=10
UNKNOWN_RECORD_DRAFTS=10
HUMAN_REVIEWED_UNKNOWN_RECORDS=0
UNKNOWN_RECORD_INSTANCES=0
RESEARCH_DECISIONS=10
PENDING_HUMAN_DECISIONS=4
CONTEXT_REVIEW_COMPLETED=false
PROTOTYPE_AUTHORIZATION_CREATED=false
PREREGISTRATION_COMPLETED=false
PROTOCOL_FREEZE_CANDIDATE_PREPARED=true
PROTOCOL_FREEZE_CANDIDATE_STATUS=DRAFT_FREEZE_CANDIDATE_NOT_APPROVED
PROTOCOL_FREEZE_APPROVED=false
EXPERIMENT_AUTHORIZATION_CREATED=false
VERIFICATION_RESULTS=0
Agent Instance = 0
Runtime = 0
Digital Entity = 0
Permission = 0
Execution = 0
Research Result = 0
```
