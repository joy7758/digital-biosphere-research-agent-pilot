---
handoff_id: HROCH-PAPER3-EOA-0001
version: v0.1
status: DRAFT_PENDING_HUMAN_CONTEXT_REVIEW
owner_reference: bin_zhang
approved_source_documents: 0
paper3_external_sources_approved_for_candidate_bibliography: 2
paper3_external_sources_pending_human_decision: 20
context_review_status: REVIEW_PENDING
authorization_effect: NONE
---

# Paper 3 EOA Human Research Owner Context Handoff v0.1

本目录是 Human Research Owner Context Handoff（人工研究负责人上下文交接）草案入口，用于把 Paper 3 EOA 的候选范围、来源、决策和 Unknown（未知项）交给已指定的 Human Research Owner `bin_zhang` 复核。

它不是已完成的 Human Context Review（人工上下文复核），不修改 canonical Context Manifest（规范上下文清单），也不批准来源、创建 Agent、授予 Permission（权限）或授权 Prototype / Experiment（原型／实验）执行。

## Read Order（读取顺序）

1. [`research-scope.md`](research-scope.md)：确认研究范围和明确排除项；
2. [`owner-discovery-report.yaml`](owner-discovery-report.yaml)：检查 Owner 候选发现来源、证据、限制和置信度；
3. [`candidate-owner.yaml`](candidate-owner.yaml)：保留候选发现并指向已确认 Owner Record；
4. [`human-context-review-docket.yaml`](human-context-review-docket.yaml)：Owner 已确认；逐项 Sources、Decisions 与 Unknown 决定仍待人类作出；
5. [`human-context-decision-input-template.yaml`](human-context-decision-input-template.yaml)：统一、零预选的 Human Decision 输入模板；Template 不是 Review Record；
6. [`human-context-decision-record.yaml`](human-context-decision-record.yaml)：固定 `HCD-001` 的正式治理记录；当前 `HUMAN_CONFIRMED`，决定已记录但尚未完成人工复核；
7. [`human-owner-confirmation-record.yaml`](human-owner-confirmation-record.yaml)：不可替代的 `HOC-001` 人工确认记录；canonical reference 为 `owner://bin-zhang`；
8. [`human-owner-record.yaml`](human-owner-record.yaml)：`ASSIGNED` Human Research Owner 的责任范围；不批准 Context 或实验；
9. [`research_owner.yaml`](research_owner.yaml)：确认 Human Research Owner 的责任结构与记录引用；
10. [`source-candidates.yaml`](source-candidates.yaml)：复核 10 个候选来源；全部已核验为 review input，原 7 个已有人工选择记录，新增 DBA / SAEE / DBO 三项仍待人工决定；当前批准和绑定数量为 `0`；
11. [`source-verification-report.yaml`](source-verification-report.yaml) 与 [`source-verification-addendum-v0.2.yaml`](source-verification-addendum-v0.2.yaml)：分别固定原 7 项与新增 3 项的路径、版本、哈希、状态和非绑定建议；不是 Source Approval；
12. [`source-record-drafts/README.md`](source-record-drafts/README.md)：10 个独立 `DRAFT_NOT_APPROVED` Source Record Draft；不计为 Source Record Instance；
13. [`human-source-decision-addendum-v0.1.yaml`](human-source-decision-addendum-v0.1.yaml)：新增 3 项来源的零预选人工决定模板；所有决定保持 `null`，不是决定记录；
14. [`research-decisions.yaml`](research-decisions.yaml)：复核 10 项候选决策；6 项记录既有规范边界，4 项等待人工确认；
15. [`human-protocol-design-decision-addendum-v0.1.yaml`](human-protocol-design-decision-addendum-v0.1.yaml)：记录 EOA DEC-001、DEC-003 至 DEC-013 的人工研究设计决策，并同步全部 22 项来源审查的历史增量证据链；Human 已批准精简路线，将 10 项直接影响方法、对照和新颖性的来源设为协议冻结核心，其他 12 项转为补充或延后审查，并为 DEC-013 选择 Option B 的四个领域语义故障类。当前 `5/24` preregistration readiness gate（预注册就绪度闸门）仍未就绪，且不批准 Context、正式编号引文、正文结论、投稿稿件、公开发布、伦理状态、实现、调用或实验；
	    更新说明：上述研究设计记录不自动批准来源；AI Model Passport 与 GSN v3 的两项受限 Human `INCLUDE` 决定已分别完成，可进入候选 bibliography，但不批准 Context、冻结正式编号引文或建立新颖性。
	    增量说明：v0.66 已在 v0.65 之后绑定 DICOM PS3.3 的 DBA/SAEE/DBO `INCLUDE_WITH_LIMITATIONS` 非约束建议与零预选 Human 输入契约；它不新增来源决定，也不改变 GSN -> PROVIMAPS -> VIDS -> Omni-Decision -> ODES -> Paper 1 -> Paper 2 -> Model Cards -> Datasheets -> W3C PROV -> DICOM PS3.3 的人工审查顺序。候选 ID 保留 `2025D`，实际审查版本为 `2026c`；Device UID 不得升级为 UDI-DI，Type 3 未观察到也不得升级为不符合或原设备无能力。
	    增量说明：v0.67 在 v0.66 之后绑定 DICOM PS3.15 的 DBA/SAEE/DBO `INCLUDE_WITH_LIMITATIONS` 非约束建议与零预选 Human 输入契约；它不新增来源决定，也不改变 GSN -> PROVIMAPS -> VIDS -> Omni-Decision -> ODES -> Paper 1 -> Paper 2 -> Model Cards -> Datasheets -> W3C PROV -> DICOM PS3.3 -> DICOM PS3.15 的人工审查顺序。候选 ID 保留 `2025D`，实际审查版本为 `2026c`；审计消息不等于事件真实，可配置触发不等于报告完整，去标识或保留也不等于隐私、原始设备事实或语义闭合。
	    增量说明：v0.68 在 v0.67 之后绑定 FHIR R4 Device `4.0.1` 的 DBA/SAEE/DBO `INCLUDE_WITH_LIMITATIONS` 非约束建议与零预选 Human 输入契约；它不新增来源决定，也不改变既有人工审查顺序。`Device.identifier` 不等于 UDI-DI，DICOM Device UID 不得升级为 UDI-DI，`udiCarrier` 只能来自可追踪来源 UDI，本地 create/readback 不等于 conformance（符合性）或 clinical interoperability（临床互操作）。
	    增量说明：v0.70 在 v0.69 之后绑定 FHIR R4 AuditEvent `4.0.1` 的 DBA/SAEE/DBO `INCLUDE_WITH_LIMITATIONS` 非约束建议与零预选 Human 输入契约；它不新增来源决定，也不改变既有人工审查顺序。AuditEvent 安全审计记录不等于事件真值、完整且未篡改的多参与方日志、授权或身份保证；update/delete guidance（更新/删除指导）不等于密码学不可变性。
	    `v0.70` 是 FHIR R4 AuditEvent 准备完成时的历史增量节点：除 AI Model Passport 外仍未形成其他 Human source decision；GSN v3 只有字段集合与审查边界获得 Human 确认，来源选择和主张决定仍为 `null`。FHIR R4 AuditEvent 只新增非约束建议与空白输入契约，未执行资源生成、validator、profile/terminology、DICOM audit-message、server、real-event、baseline、临床、监管或 Paper 3 实验。
	    当前 preregistration readiness（预注册就绪度）入口为 EOA `preregistration-readiness-gate-v0.2.yaml` 与 `preregistration-readiness-audit-v0.4.md`：总体来源决定仍为 2/22；协议冻结核心为 1/10 已完成、9/10 待审，12 项为补充或延后；满足闸门为 5/24。该同步不批准 Context、方法、协议、实现、Agent、实验或结论。
	    当前 DEC-002 入口仍为 EOA `human-source-decision-docket-v0.4.md` 与 `human-source-review-next-action-queue-v0.1.yaml`：`LIT-PROVIMAPS-2026` 是当前 Human core-source action。其他来源保持既有决定或待审状态；当前增量证据指针为 `human-source-review-evidence-manifest-v0.77.yaml`。
	    当前 manuscript truth（稿件真值）已绑定 `manuscript-assembly-contract-v0.2.yaml` 与 3526 词的 `integrated-manuscript-design-draft-v0.2.md`。全局当前来源审查指针是 `human-source-review-evidence-manifest-v0.77.yaml`；该设计稿仍不是 submission manuscript（投稿稿），Results、结论、协议、实现、Agent 与实验闸门均保持关闭。
	    GSN v3 的 Human `INCLUDE` 已按官方标准页面与 DOI `10.65391/r1386` 记录，只允许用于研究背景、方法边界、通用基线设计和新颖性对比。它不证明证据真实、绑定正确、医疗工作流闭合或 EOA 新颖性；历史零预选候选包保留为审查过程证据，不再是当前决定面。
	    C2PA 2.4 的准备面严格区分 Valid/Trusted Manifest 与 assertion/medical truth、signer credential 与医疗行为者／设备／动作授权、hard/soft binding 与 universal identity/workflow closure；其正式规范身份与单独版本化的 informative guidance surface 也保持分离。所有 C2PA 来源选择、引用、角色、主张、禁止推断、符合性、真值、授权、医学语义与 novelty 决定仍为 `null`。
	    当前 protocol/statistical reconciliation（协议／统计协调）入口为 EOA `protocol-statistical-reconciliation-options-v0.1.yaml` 与 `human-protocol-statistical-reconciliation-gate-v0.1.zh.md`：四个选项全部未选择，AI 辅助建议 `RECON-OPTION-A` 不具约束力，`PRG-008` 与 `PRG-010` 仍未满足，不产生协议修改、预注册、实现、Agent、实验或结论效力。
	    EOA `preregistration-protocol-v0.2-candidate.md` 现提供与 finite-suite SAP（有限套件统计分析计划）一致的单一审查面，并附可审计 change log 与 boundary test；它是 alternative candidate（替代候选），没有取代 protocol v0.1，没有选择任何 reconciliation option，也没有批准来源、方法、实现、案例生成、实验、分析或结论。
	    EOA `independent-methods-review-packet-v0.2-candidate.yaml` 现把 35 个 digest-bound design inputs（摘要绑定设计输入）和 44 个独立方法问题交给外部 Human reviewer（人工审查人）的候选接口，并以空白 v0.2 review record 覆盖 general methods、domain semantics、construct validity 与 protocol reconciliation；该包尚未派发、未分配审查人、未执行、未裁决，也不批准 Context、来源、协议、实现、Agent、实验或结论。
	    EOA 现另有 `independent-methods-reviewer-eligibility-and-conflict-template-v0.1.yaml`、JSON Schema 与 Human gate，用于在发送 v0.2 包前核验真实 Human 的四类专业能力、外部独立性、利益冲突、既往合作、监督依赖和 AI assistance disclosure；当前模板全空、资格决定为 `null`，没有识别、分配、联系或发送给任何候选审查人，也不满足 `PRG-007`。
	    EOA 现已本地构建 deterministic 43-file methods-review dispatch candidate（确定性方法审查发送候选包），包含 35 个 digest-bound inputs、44 项空白记录、资格表、相对路径 checksums 和 reviewer guide；ZIP 完整性及绝对路径／raw-data 扫描通过，但候选人仍未识别或获得资格决定，包未发送、审查未执行，`PRG-007=false`。
	    当前 preregistration target（预注册目标）入口为 EOA `preregistration-target-options-v0.1.yaml`、`preregistration-artifact-freeze-candidate-v0.1.yaml` 与 `human-preregistration-target-decision-gate-v0.1.zh.md`：OSF/Zenodo 四个方案均未选择，`PRT-OPTION-A` 仅为非约束性 AI 辅助建议，`PRG-022=false`，没有外部注册、DOI、冻结、实现、Agent、实验或结论效力。
	    当前 ground-truth and blinding（基准真值与盲法）入口为 EOA `ground-truth-and-blinding-contract-v0.1.yaml` 与 `human-ground-truth-and-blinding-decision-gate-v0.1.zh.md`：角色分离、单故障隔离、clean-control 去重、标签保险库、泄漏扫描和结果后解盲规则均为候选，所有人工字段为 `null`，没有独立审查人、标签、案例、blind pack、执行或外部医学验证，`PRG-018=false`。
	    当前 construct validity（构念效度）入口为 EOA `evidence-closure-construct-operationalization-v0.1.yaml` 与 `construct-validity-and-anti-tautology-review-brief-v0.1.md`：四层测量边界、等源比较、反 checklist、反循环标签和六项 falsifier（证伪条件）均为候选；所有人工字段为 `null`，独立审查未执行，外部效度未测试，当前不推荐运营或客户使用。
16. [`gsn-v3-human-source-decision-sync-v0.1.yaml`](gsn-v3-human-source-decision-sync-v0.1.yaml)：把 GSN v3 的受限 Human `INCLUDE` 决定同步为 agent-readable（智能体可读）事实；它不属于 10 个 Pilot Context Source 的批准或绑定；
17. [`dba-saee-dbo-conversation-capability-context.yaml`](dba-saee-dbo-conversation-capability-context.yaml)：本对话的 DBA / SAEE / DBO 受限能力上下文、精确来源哈希和 Human Research Owner 授权快照；`LOADED_FOR_CONTEXT_ONLY` 不等于运行时加载、能力调用、Context 批准或实验授权；
18. [`unknown-register.yaml`](unknown-register.yaml)：复核 10 个当前 `UNKNOWN` 事项；
19. [`unknown-record-drafts/README.md`](unknown-record-drafts/README.md)：10 个独立 `DRAFT_NOT_HUMAN_REVIEWED` Unknown Record Draft；不计为 Human-reviewed Unknown Record；
20. [`context-review-recommendation.yaml`](context-review-recommendation.yaml)：4 项研究决定、10 个 Unknown 和 AI Boundary 的非绑定建议；Recommendation 中的 `human_decision` 字段保持 `null`，实际人工决定以 `HCD-001` 为准；
21. [`human-context-review-draft.md`](human-context-review-draft.md)：继续完成 Sources、Scope、Unknown 和 AI Boundary 复核；Context 尚未批准。

EOA 的 `DEC-002` 现已准备第一批五个 Tier A source-by-source decision cards
（逐项来源决策卡）。这些卡通过上述 addendum 作为 review input（审查输入）引用，
但不属于本 Handoff 的 10 个 Context Source 决定，也不会改变 Handoff 的
`DRAFT_PENDING_HUMAN_CONTEXT_REVIEW` 状态。

五个 Tier A 候选现另有 analysis-unit distinction matrix（分析单元区分矩阵）和
新版 Human decision brief（人工决定简报），用于区分 model/data lifecycle
（模型/数据生命周期）、curated imaging dataset（整理后影像数据集）、
capture-to-image authenticity（采集到影像真实性）、query-scoped evidence-state
process（查询范围证据状态过程）与 portable decision record（可移植决策记录）。
这些区分和非绑定建议不建立 novelty（新颖性），也不把任何来源批准或绑定到
Context Package；Tier A 人工来源决定仍为 `0/5`。

Tier B 13 项与 Tier C 4 项也已形成同样的零预选卡片，EOA 外部来源审查入口
覆盖 22/22。该覆盖只表示所有候选均可逐项人工决定，不表示任何来源已批准或
绑定到 Pilot Context Package。

Tier B 13 项来源现另有 official-source distinction matrix（官方来源区分矩阵）
和新版 Human decision brief（人工决定简报），用于把 medical representation
（医疗表示）、generic provenance（通用来源追踪）、telemetry（遥测）、
attestation（证明）、assurance argument（保证论证）、risk governance（风险治理）
和 content integrity（内容完整性）拆开审查。该矩阵不批准 standards
conformance（标准符合性）或来源；Tier B 人工来源决定仍为 `0/13`。

Tier C 4 项来源现也有 documentation-and-prior-work distinction matrix（文档与
既有工作区分矩阵），分别覆盖 Model Cards（模型卡）、Datasheets（数据说明书）、
已发表 Paper 1 profile validation（第一篇配置验证）和仍处于
`accepted_for_publication / awaiting_production` 的 Paper 2 metadata audit
（第二篇元数据审计）。该矩阵不批准 self-citation（自引）、版本等价、来源或
新颖性；Tier C 人工来源决定仍为 `0/4`。至此区别覆盖为 `22/22`，完整受限来源
决定为 `2/22`，其余 `20/22` 待审。

Model Cards、Datasheets、已发表 UDI-DICOM Paper 1 与已接受 Paper 2 是 Tier C
四个具备 source-specific（来源特定）人工审查界面的来源。每项均有 6 项直接主张检查、
6 项 Paper 3 边界推论和 10 项禁止推断，进入零预选工作表及决定闸门。Paper 1 的界面
单独处理 same-author overlap（同作者重叠）、self-citation（自引）、profile/runtime
和 validation/generalization 边界；Paper 2 的界面单独处理 series-level convenience
sample（序列级便利样本）、记录级区间、归档元数据与原始设备真值、本地 Orthanc/FHIR
路径和临床部署边界。Paper 1 字段集与审查边界是 AI 辅助准备面，尚无 Human 确认；没有
选择 Paper 1 或 Paper 2 的任何决定选项。界面不建立未审版本等价，不批准来源、引文、
角色、主张、分析单元或新颖性；Tier C review-surface readiness 为 `4/4`，Human source
decision 仍为 `0/4`。未生成模型卡或 datasheet，未访问或使用数据集，未调用模型，也
未执行既有 validator、registry lookup、scanner/server route、DICOM 处理、基线、运行时
验证或 Paper 3 实验。

DEC-002 当前统一入口已升级为 v0.3：真实 Tier 数量为 `5/13/4`，22 项均绑定
traceability（追踪）、distinction matrix（区分矩阵）和 signing card（签署卡），
当前有 2 个完整、受限的 Human `INCLUDE` 来源决定：AI Model Passport 与 GSN v3
均已核验引用身份，并分别限定允许角色、允许主张和禁止推断边界，可进入候选 bibliography
（参考文献候选集）；其余 20 项仍待逐项决定，正式编号引文尚未冻结。另已准备 independent novelty
challenge protocol（独立新颖性挑战协议）、21 输入摘要绑定的 v0.2 pre-source-freeze
candidate packet（来源冻结前候选包）和十问题空白记录。该包当前不可派发；尚未分配独立审查人、
尚未执行、novelty resolution 仍为 `UNKNOWN`。DBA、DBOS、SAEE、DBO、EOA
和本对话都不能充当该独立审查。

EOA 现已补齐 novelty reviewer eligibility（新颖性审查人资格）Schema、零预选冲突披露表、
Human gate、reviewer guide 和 deterministic 29-file pre-freeze package。ZIP 使用相对路径
checksums，不含 raw DICOM、pixel data、patient data、runtime DB 或本地绝对路径；但因为
来源决定仍为 `2/22`，该包明确 `packet_dispatchable=false`，没有 reviewer、dispatch、review、
Human adjudication、`PRG-005`、`PRG-006` 或 novelty 结论效力。

EOA 现进一步把 novelty review 的 Human nomination、post-freeze assignment、one-time
dispatch authorization、transport receipt 和 reviewer acknowledgement 分成独立空白记录，
并提供只读 chain verifier。当前验证状态为
`INCOMPLETE_PRE_SOURCE_FREEZE_NO_EXTERNAL_ACTION_RECORDED`：未提名、未分配、未授权、
未发送、未确认、未审查，novelty 仍为 `UNKNOWN`。

四项版本敏感来源另有 metadata-only identity-convergence review（仅元数据
身份趋同审查）：两项 strong、两项 partial。该增量没有完成 VOR 全文对照，
没有批准来源或论断，也不改变 `DEC-002=CONTINUE_SOURCE_BY_SOURCE_REVIEW`。

同一组四项来源现另有 claim-scope version review（主张范围版本审查），把
4 项来源直接支持的候选主张与 4 项 Paper 3 边界推论明确分开。当前证据面为
1 项 publisher full text、1 项 official abstract 和 2 项经权威页面佐证的
preprint；没有建立跨版本全文等价，这四项 Human source decisions 仍为 `0/4`。

四项动态来源的当前状态也已单独固定：VIDS 与 Omni-Decision 为 arXiv v1，
VIDS 公开 specification 页面显示 v1.0 Release，ODES 为 pinned technical
discussion draft，Paper 2 为 `accepted_for_publication / awaiting_production`。
该固定不升级为 VOR、同行评审或标准采纳，不批准来源或 claim，也不改变 Context、
protocol、implementation、experiment 或 scientific conclusion 的状态。

四项技术相邻规范的官方身份也已刷新：OpenTelemetry Semantic Conventions
1.43.0、SLSA Provenance 1.2、GSN v3 与 C2PA 2.4。该审查仅分离来源直接事实和
Paper 3 自担推论。GSN 官方 130 页全文已完成 Human 审查并记录受限 `INCLUDE`：
可用于研究背景、方法边界、通用基线设计和新颖性对比，但不证明论证／证据真值、
绑定正确、医疗工作流闭合或 EOA 新颖性；`DEC-002` 仍继续逐项来源审查。

Tier A 的 AI Model Passport 正式出版版本现也已完成 AI-assisted
claim-boundary review（人工智能辅助主张边界审查）。该来源直接支持模型／数据
身份、生命周期来源追踪及医疗影像追踪的候选描述；Paper 3 的工作流实例级
设备-DICOM-动作交叉绑定仍是待人类判断的残余研究问题。此审查不建立跨版本
全文等价或 novelty（新颖性）。Human 后续已报告全文审查完成并选择 `INCLUDE`，
并已确认 citation identity（引用身份）、allowed roles/claims（允许角色／主张）
和 prohibited-inference review（禁止推断复核）。该决定仅产生候选参考文献纳入效力。

该来源现另有一个只供 Human 使用的 paragraph-addressable worksheet
（可按段定位工作表）：5 项来源表述核对与 5 项禁止推论核对均绑定官方全文定位符。
Human 已记录 `HUMAN_REVIEWED` 和 `INCLUDE`，并完成 citation identity（引用身份）、
4 类 allowed roles（允许角色）、5 项 allowed claims（允许主张）与 prohibited-inference
review（禁止推断复核）。连同 GSN v3，完整受限来源决定为 `2/22`，其余 `20/22` 待审；
该部分记录不产生 Context、协议冻结、正式引文冻结、实现、实验、Agent 或科学结论效力。

首个来源的单页 Human decision gate（人工决定闸门）作为历史空白界面保留；其后续
正式决定由 `ai-model-passport-human-source-decision-record-v0.2.yaml` 与
`human-source-review-decisions-v0.1.yaml` 记录。该完成决定仍不产生 Context、实现、
实验、Agent 或科学结论授权。

Tier A 的 PROVIMAPS 现已核对正式 DOI 元数据和正式摘要，并复用已审 arXiv v1
全文形成 AI-assisted claim-boundary review（人工智能辅助主张边界审查）。ACM
正式全文当前未取得，因此该来源仍是 official-abstract/preprint-bounded
（受官方摘要／预印本边界限制）的人工决定项；低摘要重合或精确术语缺失均不建立
版本等价、差异结论或 novelty。该来源现另有 Human passage-review worksheet 和
zero-preselection single-source decision gate，把正式元数据／摘要与 arXiv v1 分开，
并暴露 4 项直接主张、4 项来源表面选项、4 项主张范围选项和 7 项禁止推断。所有
Human 字段仍为 `null`；正式版本全文审查、跨版本等价和来源决定均为 `0`。

Tier A 的 VIDS 现已分别固定 arXiv v1、公开 specification、GitHub main/tag
metadata 与 PyPI distribution metadata，并形成 AI-assisted current-specification/
implementation claim-boundary review（当前规范／实现主张边界审查）。公开
specification 仍自报 v1.0 Release，而 repository 与 PyPI 已出现 v1.2.1 表面，
因此只能建立 version-pinning（版本固定）必要性；本轮未安装或运行 validator，
未产生 conformance result（符合性结果）、缺陷严重度、标准采纳或 novelty 结论。
该来源现另有 Human passage-review worksheet（人工逐段审查工作表）和
zero-preselection single-source decision gate（零预选单一来源决定闸门），分别
暴露 4 项直接主张检查、4 项引用表面选项、4 项实现主张范围选项和 7 项禁止推断。
这些界面没有预选值；VIDS Human source decision（人工来源决定）仍为 `0`，
validator execution（验证器执行）与 conformance result（符合性结果）也仍为 `0`。
VIDS 现另有 DBA/SAEE/DBO 三视角非约束建议和 agent-readable Human
source-decision input contract；它只作为 PROVIMAPS 之后的预备来源，不改变当前
GSN 项或下一 PROVIMAPS 项，也不建立 paper/specification/implementation 等价关系。

Tier A 的 Omni-Decision 现已固定 arXiv v1 PDF 和当前 arXiv 元数据，并形成
AI-assisted evidence-state/analysis-unit claim-boundary review（证据状态／分析单元
主张边界审查）。该来源直接使用 evidence state、evidence closure、deterministic
commit、insufficient stopping 和 no-state ablation；Paper 3 只能把候选残余问题
限定为 persisted medical workflow-instance semantic binding（持久化医疗工作流
实例语义绑定）。本轮未审查源码、未运行来源 benchmark、未复现报告结果，且该
analysis-unit 差异仍待 Human 判断，不建立 novelty。该 Omni-Decision 来源决定仍待审。
其 Human passage-review worksheet 与 zero-preselection single-source decision gate
现已把 4 项直接主张、4 项引用表面、4 项报告结果引用范围、4 项分析单元选择和 7 项
禁止推断分开呈现。所有 Human 决定字段仍为 `null`；benchmark execution 为 `0`，
reported results reproduced 为 `false`，cross-domain equivalence 与 novelty 均未建立。
Omni-Decision 现另有 DBA/SAEE/DBO 三视角非约束建议和 agent-readable Human
source-decision input contract；建议仅限 closest-neighbor、method-boundary 与
novelty-collision 使用，不自动分配为 confirmatory baseline，也不主张结果复现。

Tier A 的 ODES 现已固定公开 `v0.2` discussion draft（讨论草案）、`pder-v0.1`
schema（模式）和仓库 commit `7a0c0312037b78da6d995184507384393b51ee2b`，并完成
current-draft/repository static claim-boundary review（当前草案／仓库静态主张边界审查）。
它直接覆盖通用 portable decision-evidence record（可移植决策证据记录）、证据引用／
哈希、人工与机器角色、freshness/revocation（新鲜度／撤销）、fail-closed verifier
（失败关闭验证器）以及 verifier acceptance/reliance（验证器接受／依赖）分离；因此
Paper 3 只能把待检验残余问题收窄为 bounded medical workflow-instance semantic
binding（受限医疗工作流实例语义绑定）。本轮未执行 conformance vectors（符合性向量）、
未审查独立实现、未建立采纳或 novelty，该 ODES 来源决定仍待 Human 审查。

Tier B 的 W3C PROV 已按官方 PROV-O、PROV-DM 和 PROV-CONSTRAINTS Recommendation
（推荐标准）完成静态边界审查。Entity、Activity、Agent、derivation、attribution、
association、delegation、role、plan、bundle 与 validity 等通用 provenance（溯源）
原语属于既有标准工作，不能作为 Paper 3 的新原语主张。当前残余候选贡献仅保留
medical workflow-instance semantic binding（医疗工作流实例语义绑定）与
equal-information fault benchmark（等信息故障基准）。本轮未运行 reasoner（推理器）、
未验证 PROV instance、未建立 C2R 映射或符合性，也未形成 Human 来源决定或 novelty
结论。当前已准备四项 direct-claim checks（直接主张检查）、七项 prohibited-inference
checks（禁止推断检查）以及 citation surface、C2R relationship、analysis unit 和 role
的零预选人工字段；该 W3C PROV 来源决定仍待 Human 审查。

Tier B 的 DICOM PS3.3 已按官方 2026c 全文以及 UDI Macro、Device Identification
Macro、General/Enhanced General Equipment 和 Contributing Equipment 相关章节完成静态边界审查。
DICOM 已经定义设备身份、UDI 及 contributing-equipment（贡献设备）表示路径，
Device UID 也不能自动升级为 UDI-DI 证据；可选 Type 3 UDI 路径未出现时，不能据此
推导普遍不符合标准或原始设备无能力。Paper 3 的候选差异因此只能保留在医疗工作流
实例语义绑定和等信息故障基准。本轮未验证 DICOM instance 或 IOD，未审查 private
tag（私有标签），未做注册库查询或真实设备测试，也未形成 Human 来源决定或 novelty
结论；该 DICOM PS3.3 来源决定仍待 Human 审查。

该来源现另有 correction addendum 与 zero-preselection Human decision surface：
历史审查字节和哈希保持不变，失效的 `sect_c.12.1.html` 定位改由正式
`sect_C.12.html` 页面承接，Enhanced General Equipment 单独定位到
`sect_C.7.5.2.html`。五项 direct-claim checks、八项 prohibited-inference checks，
以及 citation surface、Type semantics、Device UID/UDI-DI、analysis unit 和 role
字段均未预选；Human decision、instance validation、IOD conformance、private-tag
review、registry lookup 和 real-device test 仍为 `0`。

Tier B 的 DICOM PS3.15 已按官方 2026c 全文以及 audit trail message format
（审计轨迹消息格式）、DICOM-specific audit messages（DICOM 特定审计消息）、
Basic Application Level Confidentiality Profile（基本应用级保密配置）和 Retain
Device Identity Option（保留设备身份选项）完成静态边界审查。审计消息的存在不等于
事件真值、授权或完整性，审计消息未出现也不等于事件未发生；公开样本中未观察到
UDI 或设备身份还可能受去标识与导出策略影响，不能自动推断原始设备行为。本轮未验证
审计消息或 DICOM instance，未产生 profile conformance result（配置符合性结果），
未执行 deidentifier（去标识器），未审查 private tag（私有标签），未做真实设备测试，
也未形成 Human 来源决定或 novelty 结论；该 DICOM PS3.15 来源决定仍待审。

该来源现另有 zero-preselection Human decision surface，分别呈现五项 direct-claim
checks、九项 prohibited-inference checks 以及 citation、audit/event-truth、triggering、
de-identification、analysis-unit 和 role 字段。所有人工字段保持 `null` 或空列表；本轮
没有执行 audit-message/instance validation、profile conformance、de-identifier、
private-tag review 或 real-device test，也没有生成 privacy、authority 或 scientific
effect。

Tier B 的 FHIR R4 Device 4.0.1 已按官方 Device 页面、元素定义、映射页和
StructureDefinition JSON 完成静态边界审查。`Device.identifier` 是通用业务标识，
不能自动解释为 UDI-DI；`Device.udiCarrier` 只能从可追踪的来源 UDI 信号投影，
DICOM Device UID 只能保留为带类型的辅助设备标识。本轮未验证 FHIR resource，
未执行官方 validator，未产生 profile conformance、registry resolution 或本轮
server round-trip 结果，未做真实设备或临床互操作测试，也未形成 Human 来源决定
或 novelty 结论；该 FHIR Device 来源决定仍待 Human 审查。

该来源现另有 zero-preselection Human decision surface，分别呈现五项 direct-claim
checks、十项 prohibited-inference checks，以及 citation、Device/DeviceDefinition、
identifier/UDI-DI、UDI-source、local-readback/conformance、analysis-unit 和 role
字段。所有人工字段保持 `null` 或空列表；本轮没有执行 FHIR resource validation、
official validator、implementation-guide conformance、terminology validation、
registry resolution、本轮 server roundtrip、real-device test 或
clinical-interoperability test，也没有生成 UDI truth、authority 或 scientific effect。

Tier B 的 FHIR R4 Provenance 4.0.1 已按官方 Provenance 页面、元素定义、映射页和
StructureDefinition JSON 完成静态边界审查。规范定义围绕单一 activity（活动）的
target、agent、entity、role、reference 与可选 signature，并区分 Provenance 与
AuditEvent。通用 provenance relation（来源关系）完整性已归入 C2R；资源存在或结构
有效不等于事件真实、身份可信、动作获授权、引用已解析或医疗语义闭合。本轮未验证
FHIR resource，未执行官方 validator，未产生 profile 或 W3C PROV conformance，未解析
引用，未做本轮 server round-trip、真实工作流事件或临床互操作测试，也未形成 Human
来源决定或 novelty 结论；该 FHIR Provenance 来源决定仍待 Human 审查。

Tier B 的 FHIR R4 AuditEvent 4.0.1 已按官方 AuditEvent 页面、元素定义、映射页和
StructureDefinition JSON 完成静态边界审查。规范将 AuditEvent 定位为 security-audit
event record，并预期参与可审计事件的多个 actors 各自记录；它也区分 AuditEvent 与
Provenance。通用 expected-record 与 cross-log consistency 已归入 C2R；资源存在、字段
存在或结构有效不等于事件真实、完整审计轨迹、政策已正确执行、身份可信或医疗语义闭合。
update/delete guidance 也不等于 cryptographic immutability。本轮未验证 FHIR resource，
未执行官方 validator、profile/terminology conformance、DICOM audit-message validation、
server round-trip、真实工作流事件或临床互操作测试，也未形成 Human 来源决定或 novelty
结论；该 FHIR AuditEvent 来源决定仍待 Human 审查。

该来源现另有 zero-preselection Human decision surface，分别呈现五项 direct-claim
checks、十项 prohibited-inference checks，以及 citation、Provenance/AuditEvent、
generic C2R relation、reference-resolution/versioning、event-truth/authenticity/
authorization、analysis-unit 和 role 字段。所有人工字段保持 `null` 或空列表；本轮
没有执行 FHIR resource validation、official validator、implementation-guide
conformance、terminology validation、reference resolution、W3C PROV conformance、
本轮 server roundtrip、real-workflow-event test 或 clinical-interoperability test，
也没有生成 event-truth、authority 或 scientific effect。

Tier B 的 FHIR R4 AuditEvent 4.0.1 已按官方 AuditEvent 页面、元素定义、映射页和
StructureDefinition 完成 AI-assisted static review。规范中的 security audit-log、event、
agent、source、entity、policy reference、outcome 和多参与方记录语义属于既有机制；通用
expected-record 与 cross-log consistency 已归入 C2R。资源存在或结构有效不证明事件真值、
日志完整、授权有效、身份可信、源系统未篡改或医疗语义闭合，update/delete 指导也不是密码学
不可变保证。该增量未验证 FHIR resource、未运行官方 validator、未执行 profile、terminology、
DICOM audit-message、server-roundtrip、真实工作流或临床互操作测试；该 FHIR AuditEvent 来源决定仍待 Human 审查。

Tier B 的 FHIR R4 ImagingStudy 4.0.1 已按官方 ImagingStudy 页面、元素定义、映射页和
StructureDefinition JSON 完成 AI-assisted static review。规范提供 study-series-instance
引用、modality、performer、endpoint 与计数等发布表面，但 ImagingStudy 不存储 DICOM
instances 或 pixel data。通用 UID、linkage、count、modality 与 endpoint consistency 已归入
C2R；资源、引用、UID 或 endpoint 的存在不证明来源字节、成功取回、身份、UDI、授权、动作语义、
验证、来源连续性、完整性或医疗语义闭合。本轮未验证 FHIR resource，未执行官方 validator，
未产生 profile 或 terminology conformance，未解析 endpoint，未做 DICOM query/retrieval、
本轮 server round-trip、真实工作流或临床互操作测试；该 FHIR ImagingStudy 来源决定仍待 Human 审查。

该来源现另有 zero-preselection Human decision surface，分别呈现五项 direct-claim
checks、十一项 prohibited-inference checks，以及 citation、generic imaging linkage、
source-object existence/retrieval、identity/UDI/authorization、subset/completeness、
resource separation、analysis-unit 和 role 字段。所有人工字段保持 `null` 或空列表；
本轮没有执行 FHIR resource validation、official validator、profile/terminology
conformance、endpoint resolution、DICOM query/retrieval、source DICOM byte inspection、
server roundtrip、real-workflow test 或 clinical-interoperability test，也没有生成
source-object existence、retrieval、completeness、identity、authorization、UDI、novelty、
Context、实现或实验效力。

Tier B 的 OpenTelemetry Semantic Conventions 1.43.0 已按官方规范页、`v1.43.0`
release、attribute requirement levels、semantic convention groups 与 events 页面
完成 AI-assisted static review。通用 telemetry 名称、类型、有效值、要求级别、稳定性、
EventRecord、event name、Timestamp 与 ObservedTimestamp 属于既有机制，已归入 C2R；
telemetry 存在、stable 状态、规范化命名、时间戳或跨 signal 关联不证明事件真值、producer
真实性、完整性、授权、UDI／DICOM／模型／动作绑定、provenance continuity 或医疗语义
闭合。本轮未运行 SDK、instrumentation、Collector、exporter、schema、code generation、
validator、ingestion、correlation、event verification、真实工作流或临床互操作测试，
该 OpenTelemetry 来源决定仍待 Human 审查。

Tier B 的 SLSA 1.2 已按官方 `Approved` 规范根页、tracks、provenance、build
verification、source requirements、what's new、`v1.2` tag 和维护中的
`releases/v1.2` branch 完成 AI-assisted static review。该规范确立了通用软件构建与来源
provenance、分层保障、attestation format、root of trust 和 expectation-based verification；
这些通用 artifact、identity、signature、digest、predicate、build type、source 与 dependency
检查已归入 C2R。SLSA provenance、signature、VSA、level 或 covered verification pass 不证明
医疗事件真值、UDI、DICOM、模型／动作绑定、授权、临床正确性或医疗工作流证据闭合。本轮未运行
SLSA verifier、build/source workflow、attestation/signature/VSA、CI/CD、artifact build、
conformance assessment、医疗事件验证、真实工作流或临床互操作测试，也未批准来源或建立
novelty；该 SLSA 来源决定仍待 Human 审查。

该 SLSA 来源现另有 DBA/SAEE/DBO 非约束 advisory 与零预选 Human 输入契约。建议仅限
`BACKGROUND`、`METHOD_BOUNDARY`、`BASELINE_DESIGN` 和 `NOVELTY_COLLISION`；Build L1
存在性、L2 签名来源、L3 hardened-build control、verifier trust root、configured
expectation 与 optional dependency recursion 均保持原规范边界。所有 Human 选择、角色、
claim 和 prohibited-inference 字段仍为空；没有 verifier、workflow、attestation、signature、
VSA、CI/CD、conformance、baseline、SAEE、Agent、实验或结论效力。

Tier B 的 NIST AI RMF 1.0 现另有 DBA/SAEE/DBO 非约束 advisory 与零预选 Human 输入
契约。建议仅限 `BACKGROUND`、`METHOD_BOUNDARY`、`GOVERNANCE_DECLARATION` 和
`NOVELTY_COLLISION`；组织级 GOVERN/MAP/MEASURE/MANAGE、TEVV 指导与 profile 属于
既有治理机制，不自动建立事件级证据真值、医疗语义闭合、风险接受、合规、安全、授权或
部署就绪。NIST AI 100-1 与持续演化的 Playbook 保持分离并需在 citation freeze 刷新。
所有 Human 字段仍为空；没有 framework application、profile、TEVV、assessment、baseline、
SAEE、Agent、实验或结论效力。

Tier B 的 GSN Version 3 已新增零预选 Human worksheet 与单一来源决定闸门，分开呈现
官方 citation surface、通用 assurance-argument 归属、notation/well-formedness 与
argument/evidence truth 边界、solution evidence-reference 边界、资料性 evaluation
guidance 与 conformance 边界、medical-workflow non-inference、analysis unit 和允许角色。
这些字段集合与审查边界已由 Human 确认，但该确认不构成 citation、来源选择、角色、claim、
prohibited-inference、comparator assignment 或 novelty 决定。未运行 GSN
parser/validator，未生成图，未评估 well-formedness、conformance 或 assurance argument，
未解析或验证证据引用，也未执行医疗工作流、临床、监管或 Paper 3 实验；该来源决定
仍待 Human 逐项审查，novelty 保持 `UNKNOWN`。

Tier B 的 C2PA 2.4 已新增官方规范静态审查、零预选 Human worksheet、单一来源决定
闸门与边界测试，分开呈现 assertions/signed claims/manifests、hard/soft bindings、signer
credential、`Well-Formed`/`Valid`/`Trusted` states 和 validation，与 assertion truth、
医疗主体/设备身份、UDI、DICOM linkage、action authorization、clinical/regulatory
conclusion 及 workflow-instance domain-semantic closure。未运行 C2PA validator，未生成
或验证 manifest、claim、assertion、binding、signature、credential 或 asset，也未执行
互操作、医疗工作流、临床、监管或 Paper 3 实验；C2PA 来源决定仍为 `null`。

Tier B 的 NIST AI RMF 1.0 已新增官方 48 页全文静态审查、零预选 Human worksheet、
单一来源决定闸门与边界测试，分开呈现组织和 AI 生命周期层面的 `GOVERN`、`MAP`、
`MEASURE`、`MANAGE`、TEVV guidance 与 profiles，和工作流实例的 event truth、医疗
语义、合规、安全、风险接受、授权及部署结论。未应用框架，未执行 Core assessment、
profile creation/comparison、risk-tolerance determination、measurement、TEVV、独立评估、
compliance/conformance、医疗工作流、临床、监管或 Paper 3 实验；NIST AI RMF 来源决定
仍为 `null`。

Tier B 的 in-toto Specification 1.0 已新增官方稳定 `v1.0` 标签全文静态审查、零预选
Human worksheet、单一来源决定闸门与边界测试，并把稳定标签与内容不同的当前 `master`
分开固定。该审查分开呈现 layout/link/functionary/artifact-rule conformance 与 policy
quality、event truth、医疗身份/授权、DICOM/UDI/model-action 语义、临床/监管结论。
未安装或运行 in-toto，未生成或签名 layout/link metadata，未执行 artifact rules、
inspection、final-product verification、key-binding verification、executable baseline、
医疗工作流、临床、监管或 Paper 3 实验；in-toto 来源决定仍为 `null`。
该来源现另有 DBA/SAEE/DBO `INCLUDE_WITH_LIMITATIONS` 非约束建议和零预选 Human
输入契约。它只建议把 in-toto 作为通用供应链 attestation 背景、方法边界、未来等源
baseline 设计和 novelty collision 输入；不把 layout conformance 升级为 policy
quality，不把签名/keys 升级为现实身份、授权或事件真值，也不把 artifact relation
升级为医疗语义闭合。本轮仍未创建或执行 comparator，未调用 SAEE，也未记录 Human
来源决定。

Tier C 的 Model Cards for Model Reporting 已新增正式出版身份／arXiv v2 静态主张
边界审查、零预选 Human worksheet、单一来源决定闸门与边界测试。该审查只把
model reporting、intended use、evaluation、ethical considerations 和 caveats 的
候选文献角色，与 runtime evidence、现实事件真值、医疗授权、临床／监管结论和
Paper 3 novelty 分开。Model Cards 来源决定仍为 `null`；未生成模型卡，未调用模型
或推理，未执行模型评估、运行时验证、医疗工作流或 Paper 3 实验。

Tier C 的 Datasheets for Datasets 已新增正式出版身份／arXiv v8 静态主张边界审查、
零预选 Human worksheet、单一来源决定闸门与边界测试。该审查把 dataset lifecycle
documentation、recommended use、unknown answers 和 implementation challenges，
与 runtime data use、data-object binding、授权、事件真值、医疗语义和临床／监管结论
分开。Datasheets 来源决定仍为 `null`；未生成 datasheet，未访问或使用数据集，未执行
datasheet baseline、运行时验证、医疗工作流或 Paper 3 实验。

## Truth Boundary（事实边界）

```text
Handoff Draft != Approved Context
Discovered Owner Candidate != Assigned Human Research Owner
Source Candidate != Approved Source Document
Accepted Specification Boundary != Context Approval
Unknown Register Draft != Human-reviewed Unknown Record
Decision Record Shell != Human Decision
Human Review != Agent Approval
Context Approval != Scientific Truth
Review != Permission
```

## Current State（当前状态）

```text
HANDOFF_STATUS=DRAFT_PENDING_HUMAN_CONTEXT_REVIEW
HUMAN_RESEARCH_OWNER_REFERENCE=bin_zhang
OWNER_REFERENCE=bin_zhang
CANONICAL_OWNER_REFERENCE=owner://bin-zhang
HUMAN_OWNER_CONFIRMATION_ID=HOC-001
HUMAN_OWNER_CONFIRMATION_STATUS=CONFIRMED
HUMAN_RESEARCH_OWNER_ASSIGNED=true
HUMAN_OWNER_RECORD_INSTANCE_CREATED=true
OWNER_CANDIDATES_DISCOVERED=1
OWNER_CANDIDATE_STATUS=CONFIRMED_AND_ASSIGNED
OWNER_DISCOVERY_CONFIDENCE=MEDIUM
OWNER_CONFIRMATION_REQUIRED=false
INDEPENDENT_HUMAN_REVIEWER_REQUIRED=UNKNOWN
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
RECOMMENDED_RESEARCH_DECISION_CONFIRMATIONS=4
RECOMMENDED_UNKNOWN_KEEP_UNKNOWN=9
RECOMMENDED_UNKNOWN_RESOLUTIONS=1
HUMAN_CONTEXT_DECISIONS_RECORDED=23
SOURCE_CANDIDATES=10
SOURCE_CANDIDATES_VERIFIED_FOR_HUMAN_REVIEW=10
SOURCE_CANDIDATES_PENDING_VERIFICATION=0
SOURCE_VERIFICATION_STATUS=VERIFIED_FOR_HUMAN_REVIEW_NOT_APPROVED
SOURCE_RECORD_DRAFTS=10
SOURCE_RECORD_INSTANCES=0
APPROVED_SOURCE_DOCUMENTS=0
RESEARCH_DECISIONS=10
ACCEPTED_SPECIFICATION_BOUNDARIES=6
PENDING_HUMAN_DECISIONS=4
EOA_PROTOCOL_DESIGN_DECISIONS_RECORDED=13
EOA_RESEARCH_DESIGN_AUTHORIZATION_WITHIN_SCOPE=FULL
EOA_RESEARCH_DESIGN_AUTHORIZATION_SCOPE=DEC_001_AND_DEC_003_THROUGH_DEC_013
EOA_SOURCE_BY_SOURCE_REVIEW=IN_PROGRESS
CONVERSATION_CAPABILITY_CONTEXT_VERSION=v0.2
CONVERSATION_CAPABILITY_CONTEXT_STATUS=LOADED_FOR_CONTEXT_ONLY
DBA_CONTEXT_ROLE=STATIC_REFERENCE_LENS
SAEE_CONTEXT_ROLE=LOCAL_ALPHA_CONTRACTS_LOADED_NOT_INVOKED
DBO_CONTEXT_ROLE=CONCEPT_ONLY_NOT_CALLABLE
CONVERSATION_CAPABILITY_INVOCATION=false
CONVERSATION_CONTEXT_TRUTH_EFFECT=NONE
EOA_EXTERNAL_SOURCE_CANDIDATES=22
EOA_TIER_A_AI_FULL_TEXT_REVIEWS_COMPLETED=5
EOA_TIER_A_HUMAN_SOURCE_DECISIONS=0
EOA_TIER_B_AI_TARGETED_OFFICIAL_REVIEWS_COMPLETED=13
EOA_TIER_B_HUMAN_SOURCE_DECISIONS=0
EOA_TIER_B_SOURCE_DISTINCTIONS_READY=13
EOA_TIER_B_SOURCE_DISTINCTION_HUMAN_DECISIONS=0
EOA_W3C_PROV_OFFICIAL_RECOMMENDATION_REVIEWS=3
EOA_W3C_PROV_ONTOLOGY_TEXT_REVIEWS=1
EOA_W3C_PROV_REASONER_EXECUTIONS=0
EOA_W3C_PROV_INSTANCE_VALIDATIONS=0
EOA_W3C_PROV_C2R_MAPPING_OR_CONFORMANCE=0
EOA_W3C_PROV_HUMAN_SOURCE_DECISIONS=0
EOA_DICOM_PS3_3_OFFICIAL_STANDARD_REVIEWS=1
EOA_DICOM_PS3_3_OFFICIAL_SECTIONS_REVIEWED=4
EOA_DICOM_PS3_3_INSTANCE_VALIDATIONS=0
EOA_DICOM_PS3_3_IOD_CONFORMANCE_RESULTS=0
EOA_DICOM_PS3_3_REGISTRY_LOOKUPS=0
EOA_DICOM_PS3_3_REAL_DEVICE_TESTS=0
EOA_DICOM_PS3_3_HUMAN_SOURCE_DECISIONS=0
EOA_DICOM_PS3_15_OFFICIAL_STANDARD_REVIEWS=1
EOA_DICOM_PS3_15_OFFICIAL_SECTIONS_REVIEWED=5
EOA_DICOM_PS3_15_AUDIT_MESSAGE_VALIDATIONS=0
EOA_DICOM_PS3_15_INSTANCE_VALIDATIONS=0
EOA_DICOM_PS3_15_PROFILE_CONFORMANCE_RESULTS=0
EOA_DICOM_PS3_15_DEIDENTIFIER_EXECUTIONS=0
EOA_DICOM_PS3_15_REAL_DEVICE_TESTS=0
EOA_DICOM_PS3_15_HUMAN_SOURCE_DECISIONS=0
EOA_FHIR_R4_DEVICE_OFFICIAL_STANDARD_REVIEWS=1
EOA_FHIR_R4_DEVICE_OFFICIAL_SURFACES_REVIEWED=4
EOA_FHIR_R4_DEVICE_RESOURCE_VALIDATIONS=0
EOA_FHIR_R4_DEVICE_OFFICIAL_VALIDATOR_EXECUTIONS=0
EOA_FHIR_R4_DEVICE_PROFILE_CONFORMANCE_RESULTS=0
EOA_FHIR_R4_DEVICE_REGISTRY_RESOLUTIONS=0
EOA_FHIR_R4_DEVICE_SERVER_ROUNDTRIPS_FOR_THIS_REVIEW=0
EOA_FHIR_R4_DEVICE_REAL_DEVICE_TESTS=0
EOA_FHIR_R4_DEVICE_CLINICAL_INTEROPERABILITY_TESTS=0
EOA_FHIR_R4_DEVICE_HUMAN_SOURCE_DECISIONS=0
EOA_FHIR_R4_PROVENANCE_OFFICIAL_STANDARD_REVIEWS=1
EOA_FHIR_R4_PROVENANCE_OFFICIAL_SURFACES_REVIEWED=4
EOA_FHIR_R4_PROVENANCE_RESOURCE_VALIDATIONS=0
EOA_FHIR_R4_PROVENANCE_OFFICIAL_VALIDATOR_EXECUTIONS=0
EOA_FHIR_R4_PROVENANCE_PROFILE_CONFORMANCE_RESULTS=0
EOA_FHIR_R4_PROVENANCE_REFERENCE_RESOLUTIONS=0
EOA_FHIR_R4_PROVENANCE_W3C_PROV_CONFORMANCE_RESULTS=0
EOA_FHIR_R4_PROVENANCE_SERVER_ROUNDTRIPS_FOR_THIS_REVIEW=0
EOA_FHIR_R4_PROVENANCE_REAL_WORKFLOW_EVENT_TESTS=0
EOA_FHIR_R4_PROVENANCE_CLINICAL_INTEROPERABILITY_TESTS=0
EOA_FHIR_R4_PROVENANCE_HUMAN_SOURCE_DECISIONS=0
EOA_FHIR_R4_AUDITEVENT_HUMAN_REVIEW_SURFACES_READY=true
EOA_FHIR_R4_AUDITEVENT_DIRECT_CLAIM_CHECKS=5
EOA_FHIR_R4_AUDITEVENT_PROHIBITED_INFERENCE_CHECKS=10
EOA_FHIR_R4_AUDITEVENT_RESOURCE_VALIDATIONS=0
EOA_FHIR_R4_AUDITEVENT_OFFICIAL_VALIDATOR_EXECUTIONS=0
EOA_FHIR_R4_AUDITEVENT_PROFILE_CONFORMANCE_RESULTS=0
EOA_FHIR_R4_AUDITEVENT_TERMINOLOGY_VALIDATIONS=0
EOA_FHIR_R4_AUDITEVENT_DICOM_AUDIT_MESSAGE_VALIDATIONS=0
EOA_FHIR_R4_AUDITEVENT_SERVER_ROUNDTRIPS_FOR_THIS_REVIEW=0
EOA_FHIR_R4_AUDITEVENT_REAL_WORKFLOW_EVENT_TESTS=0
EOA_FHIR_R4_AUDITEVENT_CLINICAL_INTEROPERABILITY_TESTS=0
EOA_FHIR_R4_AUDITEVENT_HUMAN_SOURCE_DECISIONS=0
EOA_FHIR_R4_AUDITEVENT_EVENT_TRUTH_EFFECT=NONE
EOA_FHIR_R4_AUDITEVENT_LOG_INTEGRITY_EFFECT=NONE
EOA_FHIR_R4_AUDITEVENT_AUTHORIZATION_EFFECT=NONE
EOA_FHIR_R4_AUDITEVENT_IDENTITY_ASSURANCE_EFFECT=NONE
EOA_OPENTELEMETRY_SEMCONV_1_43_0_AI_ASSISTED_REVIEWS=1
EOA_OPENTELEMETRY_SEMCONV_1_43_0_OFFICIAL_SURFACES_REVIEWED=5
EOA_OPENTELEMETRY_SEMCONV_1_43_0_DIRECT_CANDIDATE_CLAIMS=5
EOA_OPENTELEMETRY_SEMCONV_1_43_0_BOUNDARY_INFERENCES_SEPARATED=5
EOA_OPENTELEMETRY_SEMCONV_SDK_EXECUTIONS=0
EOA_OPENTELEMETRY_SEMCONV_COLLECTOR_EXECUTIONS=0
EOA_OPENTELEMETRY_SEMCONV_VALIDATOR_EXECUTIONS=0
EOA_OPENTELEMETRY_SEMCONV_EVENT_VERIFICATIONS=0
EOA_OPENTELEMETRY_SEMCONV_REAL_WORKFLOW_TESTS=0
EOA_OPENTELEMETRY_SEMCONV_CLINICAL_INTEROPERABILITY_TESTS=0
EOA_OPENTELEMETRY_SEMCONV_HUMAN_SOURCE_DECISIONS=0
EOA_TIER_C_AI_FULL_TEXT_REVIEWS_COMPLETED=4
EOA_TIER_C_HUMAN_SOURCE_DECISIONS=0
EOA_TIER_C_SOURCE_DISTINCTIONS_READY=4
EOA_TIER_C_SOURCE_DISTINCTION_HUMAN_DECISIONS=0
EOA_ALL_SOURCE_DISTINCTIONS_READY=22
EOA_ALL_SOURCE_DISTINCTION_HUMAN_DECISIONS=0
EOA_REMAINING_SOURCE_CANDIDATES_NOT_YET_AI_REVIEWED=0
EOA_SOURCE_SELECTION_PROPOSAL_ID=EOA-PAPER3-HUMAN-SOURCE-SELECTION-PROPOSAL-0.1
EOA_SOURCE_SELECTION_PROPOSAL_SHA256=10396f3794b6a556c568ca27a91ad334e5783cf247d427dcccfb08df3a963298
EOA_AI_RECOMMEND_INCLUDE=22
EOA_AI_RECOMMEND_DEFER=0
EOA_SOURCE_SELECTION_EFFECT=NONE
EOA_HUMAN_APPROVED_SOURCES=2
EOA_SOURCE_TO_CLAIM_TRACEABILITY_PRESENT=true
EOA_CLAIM_LINKED_SOURCE_REVIEW_MANIFEST_PRESENT=true
EOA_SOURCE_DECISION_INTERFACE_VERSION=0.3
EOA_ZERO_PRESELECTION_SOURCE_DECISION_TEMPLATE_PRESENT=true
EOA_SOURCE_DECISION_TRUE_TIER_COUNTS=5/13/4
EOA_INDEPENDENT_NOVELTY_CHALLENGE_PROTOCOL_PRESENT=true
EOA_INDEPENDENT_NOVELTY_CHALLENGE_EXECUTED=false
EOA_INDEPENDENT_NOVELTY_REVIEWER_ASSIGNED=false
EOA_INDEPENDENT_NOVELTY_PRE_FREEZE_CANDIDATE_INPUTS=24
EOA_INDEPENDENT_NOVELTY_PRE_FREEZE_CANDIDATE_FILES=32
EOA_INDEPENDENT_NOVELTY_PRE_FREEZE_CANDIDATE_DISPATCHABLE=false
EOA_CITATION_READINESS_CURRENT_STATE=LEAN_PROTOCOL_CORE_ONE_OF_TEN_RECORDED_NOT_FROZEN
EOA_CITATION_READINESS_HISTORICAL_REGISTER_PRESERVED=true
EOA_ARTIFACT_VERSION=0.2.142-draft
EOA_RESEARCH_MANIFEST_SHA256=be5165094f8fceb49a647d5421fd4c2004e8c6d9ec31a456a7e1252f51586c2b
EOA_CURRENT_SOURCE_REVIEW_MANIFEST=references/human-source-review-evidence-manifest-v0.77.yaml
EOA_PROTOCOL_CORE_SOURCES=10
EOA_PROTOCOL_CORE_SOURCE_DECISIONS_RECORDED=1
EOA_PROTOCOL_CORE_SOURCE_DECISIONS_PENDING=9
EOA_SUPPLEMENTARY_OR_DEFERRED_SOURCES=12
EOA_HISTORICAL_GSN_DECISION_SURFACE_MANIFEST=references/human-source-review-evidence-manifest-v0.53.yaml
EOA_INDEPENDENT_NOVELTY_POST_FREEZE_REBUILD_STATUS=NOT_READY_FOR_POST_SOURCE_FREEZE_PACKET_REBUILD
EOA_INDEPENDENT_NOVELTY_POST_FREEZE_REBUILD_CONDITIONS_SATISFIED=1
EOA_INDEPENDENT_NOVELTY_POST_FREEZE_REBUILD_CONDITIONS_TOTAL=8
EOA_INDEPENDENT_NOVELTY_POST_FREEZE_REBUILD_ONLY_SATISFIED_CONDITION=NF-002
EOA_INDEPENDENT_NOVELTY_CURRENT_PRE_FREEZE_ARCHIVE_REUSABLE_AFTER_FREEZE=false
EOA_INDEPENDENT_NOVELTY_POST_FREEZE_REBUILD_AUTHORIZED=false
EOA_GSN_V3_HUMAN_SOURCE_DECISION_COMPLETENESS_STATUS=COMPLETE_BOUNDED_INCLUDE_RECORDED
EOA_GSN_V3_HUMAN_SOURCE_DECISION_INPUT_SCHEMA_VALID=true
EOA_GSN_V3_PENDING_REQUIRED_HUMAN_FIELDS=0
EOA_GSN_V3_SELECTION_DEPENDENT_HUMAN_FIELDS=0
EOA_GSN_V3_CANONICAL_SOURCE_DECISION_RECORDED=true
EOA_GSN_V3_SELECTION_DECISION=INCLUDE
EOA_GSN_V3_ALLOWED_ROLES=BACKGROUND,METHOD_BOUNDARY,BASELINE_DESIGN,NOVELTY_COLLISION
EOA_GSN_V3_CITATION_DOI=10.65391/r1386
EOA_GSN_V3_HUMAN_SOURCE_DECISION_CANDIDATE_STATUS=HISTORICAL_ZERO_PRESELECTION_PACKET_SUPERSEDED
EOA_GSN_V3_HUMAN_SOURCE_DECISION_CANDIDATE_BOUND_INPUTS=14
EOA_GSN_V3_HUMAN_SOURCE_DECISION_CANDIDATE_FILES=18
EOA_GSN_V3_HUMAN_SOURCE_DECISION_CANDIDATE_SOURCE_SELECTED=false
EOA_CURRENT_HUMAN_SOURCE_ACTION=LIT-PROVIMAPS-2026
EOA_PROVIMAPS_HUMAN_REVIEW_PACKET_STATUS=CURRENT_ZERO_PRESELECTION_HUMAN_REVIEW_CANDIDATE_BUILT_NOT_DISPATCHED
EOA_PROVIMAPS_HUMAN_REVIEW_PACKET_BOUND_INPUTS=13
EOA_PROVIMAPS_PLAIN_LANGUAGE_DECISION_CARD=research/human-provimaps-source-decision-card-v0.1.zh.md
EOA_PROVIMAPS_HUMAN_SOURCE_DECISION=null
EOA_INDEPENDENT_METHODS_REVIEW_PACKET_PRESENT=true
EOA_INDEPENDENT_METHODS_REVIEW_PACKET_INPUTS=21
EOA_INDEPENDENT_METHODS_REVIEW_QUESTIONS=22
EOA_INDEPENDENT_METHODS_REVIEWER_ASSIGNED=false
EOA_INDEPENDENT_METHODS_REVIEW_COMPLETED=false
EOA_INDEPENDENT_METHODS_REVIEW_PACKET_V0_2_CANDIDATE_PRESENT=true
EOA_INDEPENDENT_METHODS_REVIEW_PACKET_V0_2_CANDIDATE_INPUTS=35
EOA_INDEPENDENT_METHODS_REVIEW_PACKET_V0_2_CANDIDATE_QUESTIONS=44
EOA_INDEPENDENT_METHODS_REVIEW_PACKET_V0_2_CANDIDATE_DISPATCHED=false
EOA_INDEPENDENT_METHODS_REVIEW_PACKET_V0_2_CANDIDATE_REVIEWER_ASSIGNED=false
EOA_INDEPENDENT_METHODS_REVIEW_PACKET_V0_2_CANDIDATE_REVIEW_EXECUTED=false
EOA_INDEPENDENT_METHODS_REVIEWER_ELIGIBILITY_SURFACE_PRESENT=true
EOA_INDEPENDENT_METHODS_REVIEWER_ELIGIBILITY_DECISION=null
EOA_INDEPENDENT_METHODS_REVIEWER_CANDIDATE_IDENTIFIED=false
EOA_INDEPENDENT_METHODS_REVIEWER_ASSIGNED_BY_ELIGIBILITY_SURFACE=false
EOA_INDEPENDENT_METHODS_REVIEW_PACKET_DISPATCHED_BY_ELIGIBILITY_SURFACE=false
EOA_INDEPENDENT_METHODS_REVIEW_DISPATCH_CANDIDATE_BUILT=true
EOA_INDEPENDENT_METHODS_REVIEW_DISPATCH_CANDIDATE_STATUS=BUILT_LOCALLY_NOT_DISPATCHED_NOT_EXECUTED
EOA_INDEPENDENT_METHODS_REVIEW_DISPATCH_CANDIDATE_FILES=43
EOA_INDEPENDENT_METHODS_REVIEW_DISPATCH_CANDIDATE_REVIEWER_ASSIGNED=false
EOA_INDEPENDENT_METHODS_REVIEW_DISPATCH_CANDIDATE_DISPATCHED=false
EOA_INDEPENDENT_METHODS_REVIEW_DISPATCH_CANDIDATE_REVIEW_EXECUTED=false
EOA_INDEPENDENT_METHODS_REVIEWER_NOMINATION_ASSIGNMENT_SURFACE_PRESENT=true
EOA_INDEPENDENT_METHODS_REVIEWER_NOMINATED=false
EOA_INDEPENDENT_METHODS_REVIEWER_ASSIGNMENT_DECISION=null
EOA_INDEPENDENT_METHODS_REVIEWER_ASSIGNED=false
EOA_INDEPENDENT_METHODS_DISPATCH_AUTHORIZATION_DECISION=null
EOA_INDEPENDENT_METHODS_DISPATCH_AUTHORIZED=false
EOA_INDEPENDENT_METHODS_DISPATCH_RECORDED=false
EOA_INDEPENDENT_METHODS_DISPATCH_RECEIPT_RECORDED=false
EOA_INDEPENDENT_METHODS_REVIEWER_ACKNOWLEDGED=false
EOA_INDEPENDENT_METHODS_REVIEW_DISPATCH_CHAIN_VERIFIER_PRESENT=true
EOA_INDEPENDENT_METHODS_REVIEW_DISPATCH_CHAIN_STATUS=INCOMPLETE_NO_EXTERNAL_ACTION_RECORDED
EOA_INDEPENDENT_METHODS_REVIEW_DISPATCH_CHAIN_VALID=true
EOA_BLANKET_SOURCE_APPROVAL_VALID=false
EOA_CITATION_READINESS_AUDIT_COMPLETED=true
EOA_TIER_A_CITATION_IDENTITIES_REFRESHED=5
EOA_TIER_A_IDENTITY_REFRESH_HUMAN_SOURCE_DECISIONS=0
EOA_TIER_B_CITATION_IDENTITIES_REFRESHED=13
EOA_TIER_B_IDENTITY_REFRESH_HUMAN_SOURCE_DECISIONS=0
EOA_TIER_C_CITATION_IDENTITIES_REFRESHED=4
EOA_TIER_C_IDENTITY_REFRESH_HUMAN_SOURCE_DECISIONS=0
EOA_ALL_CANDIDATE_IDENTITIES_REFRESHED=22
EOA_TIER_A_AND_TIER_B_SOURCE_DISTINCTIONS_READY=18
EOA_CITATION_READY_PENDING_HUMAN_SELECTION=8
EOA_CITATION_REFRESH_AT_FREEZE=7
EOA_CITATION_HUMAN_VERSION_CHECK=5
EOA_CITATION_ACCEPTED_MANUSCRIPT_REFRESH=1
EOA_CITATION_TECHNICAL_ROLE_DECISION=1
EOA_PAPER1_PUBLICATION_STATUS=VERSION_OF_RECORD_PUBLISHED
EOA_PAPER2_PUBLICATION_STATUS=ACCEPTED_FOR_PUBLICATION_AWAITING_PRODUCTION
EOA_C2R_BASELINE_CONTRACT_STATUS=DESIGN_ONLY_NOT_IMPLEMENTED
EOA_REASON_CODE_REGISTRY_STATUS=DESIGN_DRAFT_NOT_FROZEN
EOA_REASON_CODE_DEPENDENCY_CONTRACT_PRESENT=true
EOA_REASON_CODE_REGISTRY_HUMAN_APPROVED=false
EOA_REASON_CODE_REGISTRY_BOUND_TO_IMPLEMENTATION=false
EOA_FIVE_ABLATION_DIRECTION_HUMAN_APPROVED=true
EOA_COMPONENT_ABLATION_CONTRACT_STATUS=DESIGN_DRAFT_NOT_FROZEN
EOA_COMPONENT_ABLATION_CONTRACT_HUMAN_APPROVED=false
EOA_COMPONENT_ABLATION_INTERFACE_IMPLEMENTED=false
EOA_SAEE_EXACT_FREEZE_REQUIREMENT_HUMAN_APPROVED=true
EOA_SAEE_COMPARATOR_CONTRACT_STATUS=CANDIDATE_NOT_HUMAN_REVIEWED_NOT_FROZEN
EOA_SAEE_COMPARATOR_CONTRACT_HUMAN_APPROVED=false
EOA_SAEE_COMPARATOR_SOURCE_SNAPSHOT_HUMAN_APPROVED=false
EOA_SAEE_COMPARATOR_PROJECTION_FROZEN=false
EOA_SAEE_COMPARATOR_ENVIRONMENT_FROZEN=false
EOA_SAEE_COMPARATOR_IMPLEMENTED=false
EOA_SAEE_INVOCATION_AUTHORIZED=false
EOA_EXPLORATORY_C3_DEPENDENT_SAEE_ADAPTER_CONFIRMATORY_ELIGIBLE=false
EOA_SOURCE_REVIEW_EVIDENCE_MANIFEST_PRESENT=true
EOA_METHODS_REVIEW_HANDOFF_STATUS=READY_FOR_INDEPENDENT_METHODS_REVIEW_NOT_FINAL_NOT_PREREGISTERED
EOA_METHODS_REVIEW_QUESTIONS=12
EOA_INDEPENDENT_METHODS_REVIEWER_RECOMMENDATION=null
EOA_AI_ASSISTED_METHODS_REVIEW_STATUS=AI_ASSISTED_METHODS_REVIEW_COMPLETE_HUMAN_DECISION_PENDING
EOA_AI_ASSISTED_METHODS_REVIEW_RECOMMENDATION=RETURN_FOR_REVISION_BEFORE_FINAL_METHODS_APPROVAL
EOA_INDEPENDENT_HUMAN_METHODS_REVIEW_COMPLETED=false
EOA_FINAL_METHODS_APPROVAL=false
EOA_SAP_V0_2_CANDIDATE_PRESENT=true
EOA_SAP_V0_2_CANDIDATE_HUMAN_DECISION=null
EOA_SAP_V0_2_CANDIDATE_HUMAN_APPROVED=false
EOA_SAP_V0_1_SUPERSEDED=false
EOA_FINITE_BENCHMARK_ANALYSIS_CONTRACT_FROZEN=false
EOA_DESIGN_ARGUMENT_SKELETON_READY=true
EOA_INTRODUCTION_SOURCE_SLOT_DESIGN_READY=true
EOA_RELATED_WORK_SOURCE_SLOT_SCAFFOLD_READY=true
EOA_FINAL_NUMERIC_CITATIONS_ALLOWED=false
EOA_FINAL_INTRODUCTION_PROSE_AUTHORIZED=false
EOA_FINAL_RELATED_WORK_PROSE_AUTHORIZED=false
EOA_ABSTRACT_OBJECTIVE_METHODS_DESIGN_READY=true
EOA_ABSTRACT_RESULTS_STATUS=NOT_RUN
EOA_ABSTRACT_CONCLUSION_STATUS=NONE
EOA_LIMITATIONS_DESIGN_DRAFT_READY=true
EOA_DECLARATIONS_DESIGN_DRAFT_READY=true
EOA_DISCUSSION_CONDITIONAL_SCAFFOLD_READY=true
EOA_DISCUSSION_BRANCH_SELECTED=false
EOA_CURRENT_MANUSCRIPT_ASSEMBLY_CONTRACT=paper/manuscript-assembly-contract-v0.2.yaml
EOA_HISTORICAL_MANUSCRIPT_ASSEMBLY_CONTRACT=paper/manuscript-assembly-contract-v0.1.yaml
EOA_INTEGRATED_MANUSCRIPT_DESIGN_ASSEMBLY_READY=true
EOA_INTEGRATED_MANUSCRIPT_DESIGN_WORD_COUNT=3475
EOA_MANUSCRIPT_COHERENCE_AUDIT_READY=true
EOA_CANDIDATE_QUESTION_TRACE_COUNT=4
EOA_REVIEWER_ATTACK_COUNT=14
EOA_EMPIRICALLY_RESOLVED_REVIEWER_ATTACK_COUNT=0
EOA_DESIGN_FIGURES_READY=2
EOA_RESULT_DEPENDENT_FIGURES_COMPLETED=0
EOA_DESIGN_TABLES_READY=4
EOA_RESULT_DEPENDENT_TABLES_COMPLETED=0
EOA_FINAL_HUMAN_DECLARATIONS_COMPLETE=false
EOA_PUBLIC_RELEASE_AUTHORIZED=false
EOA_SUBMISSION_MANUSCRIPT_READY=false
EOA_RESULTS_SECTION_STATUS=NOT_RUN_STRUCTURE_ONLY
EOA_SCIENTIFIC_CONCLUSION=NONE
EOA_DOMAIN_SEMANTIC_INVARIANT_CONTRACT_PRESENT=true
EOA_DOMAIN_SEMANTIC_INVARIANT_COUNT=19
EOA_DOMAIN_SEMANTIC_INVARIANT_CONTRACT_HUMAN_APPROVED=false
EOA_DOMAIN_SEMANTIC_INVARIANT_CONTRACT_FROZEN=false
EOA_STATIC_DISTINCTIVENESS_AUDIT_COMPLETED=true
EOA_COMPARATOR_PERFORMANCE_RESULT=NONE
EOA_DEC_013_STATUS=HUMAN_DECISION_RECORDED_DESIGN_ONLY
EOA_DEC_013_HUMAN_DECISION=OPTION_B_ADD_SOURCE_GROUNDED_DOMAIN_ROLE_CLASSES_AND_REVISE_H1
EOA_DEC_013_DECISION_GATE_READY=true
EOA_DEC_013_CURRENT_DECISION_GATE_VERSION=0.2
EOA_DEC_013_OPTION_B_SCOPE_HUMAN_DECISION=ADVANCE_RECOMMENDED_FOUR_TO_SOURCE_AND_SPECIFICATION_REVIEW
EOA_DOMAIN_SEMANTIC_SOURCE_DEPENDENCY_CRITICAL_PATH_PRESENT=true
EOA_DOMAIN_SEMANTIC_SOURCE_DEPENDENCY_REQUIRED_CLASS_COUNT=4
EOA_DOMAIN_SEMANTIC_SOURCE_DEPENDENCY_CURRENT_HUMAN_ACTION=LIT-PROVIMAPS-2026
EOA_DOMAIN_SEMANTIC_EXTENSION_CANDIDATES=7
EOA_DOMAIN_SEMANTIC_EXTENSION_EXACT_CLASS_SET_HUMAN_APPROVED=true
EOA_DOMAIN_SEMANTIC_EXTENSION_IMPLEMENTED=0
EOA_SCHEMA_CHANGE_AUTHORIZED=false
EOA_IMPLEMENTATION_AUTHORIZED=false
EOA_EXPERIMENT_AUTHORIZED=false
DRAFT_UNKNOWN_ENTRIES=10
UNKNOWN_RECORD_DRAFTS=10
HUMAN_REVIEWED_UNKNOWN_RECORDS=0
UNKNOWN_RECORD_INSTANCES=0
CONTEXT_PACKAGE_STATUS=DRAFT
REVIEW_STATUS=REVIEW_PENDING
AUTHORIZATION_EFFECT=NONE
Agent=0
Runtime=0
Entity=0
Permission=0
Execution=0
Research Result=0
```
