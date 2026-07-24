---
project_name: digital-biosphere-research-agent-pilot
project_type: application-layer-research-pilot
specification_version: v0.1
target_version: v1.0
status: specification-only
delivery_status: PREPARATION_ONLY_NOT_READY
readiness_status: NOT_READY
paper_status: DRAFT_ONLY
agent_implemented: false
runtime_created: false
digital_entity_created: false
permission_granted: false
research_execution_started: false
research_context_package_defined: true
research_context_package_status: DRAFT
research_result_created: false
human_context_review_checklist_defined: true
human_context_review_executed: false
context_handoff_status: DRAFT_PENDING_HUMAN_CONTEXT_REVIEW
---

# Digital Biosphere Research Agent Pilot（数字生物圈科研智能体试验）

`digital-biosphere-research-agent-pilot` 是 Digital Biosphere Stack（数字生物圈技术栈）的第一个 Application Layer Research Pilot（应用层科研试验），也是 Research Agent Reference Pilot（科研智能体参考试验）。

本仓库目前已建立 Project Initialization（项目初始化）、Research Governance（科研治理）、Research Execution Framework Preparation（研究执行框架准备）与 Scientific Paper Preparation Pipeline（科学论文准备管线）。它不包含 Research Agent（科研智能体）实例，不创建 Runtime（运行时）或 Digital Entity（数字实体），不执行科研任务，也没有真实实验结果。

## Project Type（项目类型）

```text
Application Layer Research Pilot
```

该项目研究一个受人工监督的 Research Agent 是否能够辅助形成更可复现、证据更完整、过程更可追溯的科研工作流。首个研究场景引用 Paper 3 的 Evidence Object Architecture（EOA，证据对象架构）medical imaging evidence closure research（医学影像证据闭环研究）工作流。

## Position in the Stack（技术栈位置）

```text
Digital Biosphere
├── DBA
│   └── Constitution / Architecture
├── DBOS
│   └── Infrastructure
├── SAEE
│   └── Evolution Evaluation
└── Research Agent Pilot
    └── First Application Experiment
```

| 项目 | 在本 Pilot 中的职责 | 明确不表示 |
|---|---|---|
| Digital Biosphere Architecture（数字生物圈架构） | 定义上位规则、概念和治理边界 | 本仓库可以修改 DBA |
| DBOS（数字生物圈操作系统） | 未来提供 Identity Reference（身份引用）、Execution Reference（执行引用）、Evidence Reference（证据引用）和 Verification Reference（验证引用） | 已登记实体、已授予权限或已创建 Runtime |
| SAEE（硅基放大演化生态） | 未来接收有界记录并提供 Evaluation（评价）、Fitness Analysis（适应度分析）和 Evolution Recommendation（演化建议） | SAEE 可以修改实验、证据或论文结论 |
| Research Agent Pilot（科研智能体试验） | 定义应用层参考实验及其人工监督、研究问题和 Benchmark（基准） | 已实现、已执行或已验证真实科研能力 |

这些是 architectural dependencies（架构依赖）与 future integration references（未来集成引用），不是当前软件依赖、API 调用或已完成集成。

## Research Question（研究问题）

> Can a governed Research Agent improve reproducibility of scientific workflows?
>
> 受治理科研智能体是否可以提升科研流程可复现性？

当前仓库只定义如何研究该问题，尚未回答该问题。详见 [`research/research-question.md`](research/research-question.md)。

Paper 3 的 `DEC-002` 来源逐项审查仍在进行。五个 Tier A candidate
source（一级候选来源）的公开身份与 publication state（发表状态）已完成
AI-assisted primary-surface refresh（人工智能辅助的一手页面刷新）；该刷新本身
不产生 Human source decision（人工来源决定）。全局现有 1 个完整受限来源决定，
其余 `21/22` 待审。Tier B 与 Tier C 也已完成
official identity refresh（官方身份刷新），因此 22 项候选均有当前身份审查
输入；这些刷新不批准来源、主张或实验。

当前机器可读 DEC-002 顺序入口为
`evidence-object-architecture/references/human-source-review-next-action-queue-v0.1.yaml`，
人工入口为 `evidence-object-architecture/research/human-source-decision-docket-v0.4.md`。
队列的首项是已完成字段集合确认但尚未形成来源决定的
`LIT-GSN-STANDARD-3`；该顺序仅用于 review workflow（审查流程），不表示科学优先级
或 AI 来源推荐。

其中四项版本敏感来源现另有 metadata-only version-convergence review（仅元
数据版本趋同审查）：两项为 strong identity convergence（强身份趋同），两项
为 partial identity convergence（部分身份趋同）。该检查没有完成 VOR
（正式出版版本）全文比对；这四项版本趋同决定仍待 Human 审查。

同一组四项来源现另有 claim-scope version review（主张范围版本审查）：审查
区分了 4 项来源直接支持的候选主张和 4 项只能由 Paper 3 自行承担的边界推论。
当前访问面仅包括 1 项 publisher full text（出版者全文）、1 项 official
abstract（官方摘要）与 2 项经权威页面佐证的 preprint（预印本）；该审查不建立
VOR 全文等价，不批准任何来源、主张或引文。

另有 4 项 mutable-source status review（动态来源状态审查）：VIDS 与
Omni-Decision 当前仍是 arXiv v1；VIDS 的公开 specification（规范）页面显示
v1.0 Release；ODES 仍是固定 technical discussion draft（技术讨论稿）；Paper 2
仍是 `accepted_for_publication / awaiting_production`。这些状态只作为
DEC-002 人工逐项审查输入，不升级发表状态、不建立同行评审或标准采纳、不批准
来源或主张；这四项动态来源决定仍待 Human 审查。

六项最接近 Paper 3 技术边界的规范/框架来源现另有 current-status and
claim-boundary review（当前状态与主张边界审查）：OpenTelemetry Semantic
Conventions 1.43.0、SLSA Provenance 1.2、GSN v3、C2PA 2.4、NIST AI RMF 1.0
与 in-toto Specification 1.0
的官方身份已核对，
并把来源可直接支持的事实与 Paper 3 必须自行承担的推论分开。GSN 官方 130 页
PDF 已完成 AI-assisted full-text review，但仍需 Human Research Owner 独立阅读
和决定；该增量不选择这些来源、不建立 novelty。

Tier A 的 AI Model Passport 正式出版版本现也已完成 AI-assisted
claim-boundary review（人工智能辅助主张边界审查），并与已审 arXiv v1 做了
描述性差异检查。该增量只缩窄待人类判断的 prior-work boundary（既有工作边界）；
它不建立跨版本全文或主张等价、不证明 novelty。Human 已对 AI Model Passport
完成 1 个受限 `INCLUDE` 决定：引用身份已核验，4 类角色和 5 项允许主张已确认，
仅可进入候选 bibliography（参考文献候选集）；正式编号引文、Context、实现、
实验、Agent 和科学结论仍未获授权。

Tier A 的 PROVIMAPS 也已核对正式 DOI 元数据和正式摘要，并复用已审 arXiv v1
全文完成 AI-assisted claim-boundary review（人工智能辅助主张边界审查）。由于
ACM 正式全文当前不可访问，该来源仍受 official-abstract/preprint boundary
（官方摘要／预印本边界）约束；该增量不建立跨版本等价、novelty 或来源批准，
该来源现另有零预选 Human passage-review worksheet（人工逐段审查工作表）和
single-source decision gate（单一来源决定闸门），把正式元数据／摘要与 arXiv v1
分开，并暴露 4 项直接主张、4 项来源表面选择、4 项主张范围选择和 7 项禁止推断。
这些界面没有记录 Human source decision；正式版本全文审查和跨版本等价仍为 `0`。

Tier A 的 VIDS 现已形成独立的 Human passage-review worksheet（人工逐段审查
工作表）与 zero-preselection decision gate（零预选决定闸门）。审查界面把 arXiv
v1、公开 specification v1.0、GitHub tag v1.2.1 和 PyPI validator v1.2.1 分开，
并明确本轮没有安装或执行 validator、没有产生 conformance result（符合性结果）。
这些 review surfaces（审查界面）已就绪，但 VIDS Human source decision 仍为 `0`；
它们不改变全局完整受限决定 `1/22`、待审 `21/22` 的状态。

Tier A 的 Omni-Decision 也已形成独立的 Human passage-review worksheet（人工逐段
审查工作表）与 zero-preselection decision gate（零预选决定闸门）。该界面将术语
碰撞、引用表面、报告结果引用范围和 query-scoped inference state（查询范围推理状态）
与 persisted medical workflow-instance record（持久化医疗工作流实例记录）的候选
分析单元区分拆成独立人工字段。当前 Human source decision 为 `0`，benchmark
execution 为 `0`，reported results reproduced 为 `false`，novelty 仍为 `UNKNOWN`。

Tier A 的 ODES 现也有独立的 Human passage-review worksheet（人工逐段审查工作表）
与 zero-preselection decision gate（零预选决定闸门）。该界面固定当前官网
`v0.2 discussion draft` 与仓库 commit
`7a0c0312037b78da6d995184507384393b51ee2b`，并将 citation surface（引用表面）、
technical-grey-literature status（技术灰色文献状态）、generic portable-object
collision（通用可移植对象碰撞）和 medical workflow-instance analysis unit（医疗
工作流实例分析单元）拆成独立人工字段。当前 ODES Human source decision、schema/
conformance execution、independent implementation review 和 external adoption review
均为 `0`，novelty 仍为 `UNKNOWN`。至此 Tier A `5/5` 来源均有 source-specific Human
review surface，但完整受限决定仍仅为 `1/22`。

Tier B 的 W3C PROV 现也有 source-specific（来源特定）zero-preselection
Human worksheet（零预选人工工作表）与 decision gate（决定闸门）。该界面固定
2013-04-30 的 PROV-O、PROV-DM、PROV-CONSTRAINTS Recommendation（推荐标准）
身份，将 citation surface（引用表面）、概念复用、C2R-to-PROV mapping/conformance
（C2R 到 PROV 的映射／符合性）、event truth（事件真实性）和 analysis unit
（分析单元）拆开。当前 Human source decision、reasoner、instance validation、
constraints implementation、mapping 与 conformance execution 均为 `0`；该准备不
改变 `1/22` 已完成来源决定、novelty `UNKNOWN` 或任何执行授权。

Tier B 的 DICOM PS3.3 2026c 也已形成 source-specific zero-preselection Human
worksheet 与 decision gate。历史静态审查保持原字节与哈希不变，另以 correction
addendum 记录失效的 `sect_c.12.1.html` 定位并改指官方 `sect_C.12.html`，同时将
Enhanced General Equipment 独立定位到 `sect_C.7.5.2.html`。当前五项直接主张、
八项禁止推断及 citation、Type semantics、Device UID/UDI-DI、analysis unit、role
字段均待人工逐项决定；DICOM validation、IOD conformance、private-tag review、
registry lookup、real-device test 与 Human source decision 均为 `0`。

Tier B 的 DICOM PS3.15 2026c 现也有 source-specific zero-preselection Human
worksheet 与 decision gate。该界面把 audit-message format（审计消息格式）、event
truth（事件真实性）、configurable triggering（可配置触发）、de-identification scope
（去标识范围）、device/UDI retention（设备／UDI 保留）与 workflow-instance analysis
unit（工作流实例分析单元）分开。五项直接主张和九项禁止推断均待人工复核；
audit-message/instance validation、profile conformance、de-identifier、private-tag、
real-device test 与 Human source decision 均为 `0`，privacy/novelty effect 仍为 `NONE`/
`UNKNOWN`。

Tier B 的 FHIR R4 Device 4.0.1 现也有 source-specific zero-preselection Human
worksheet 与 decision gate。该界面把 versioned citation surface（版本化引用表面）、
Device/DeviceDefinition、business identifier/UDI-DI、UDI-source precondition、local
readback/conformance 和 workflow-instance analysis unit 分开。五项直接主张和十项
禁止推断均待人工复核；FHIR resource validation、official validator、profile
conformance、terminology validation、registry resolution、本轮 server roundtrip、
real-device test、clinical-interoperability test 与 Human source decision 均为 `0`，
UDI truth/novelty effect 仍为 `NONE`/`UNKNOWN`。

Tier B 的 FHIR R4 Provenance 4.0.1 现也有 source-specific zero-preselection
Human worksheet 与 decision gate。该界面把 versioned citation surface、
Provenance/AuditEvent、generic C2R relations、reference resolution/versioning、
event truth/authenticity/authorization 和 workflow-instance analysis unit 分开。五项
直接主张和十项禁止推断均待人工复核；FHIR resource validation、official validator、
profile conformance、terminology validation、reference resolution、W3C PROV
conformance、本轮 server roundtrip、real-workflow-event test、clinical-
interoperability test 与 Human source decision 均为 `0`，novelty effect 仍为
`UNKNOWN`。

Tier B 的 FHIR R4 AuditEvent 4.0.1 现也有 source-specific zero-preselection
Human worksheet 与 decision gate。该界面把 security-audit event recording、
AuditEvent/Provenance、generic multi-actor log consistency、event truth、audit-trail
completeness、policy/authorization、identity assurance、update/delete guidance 与
cryptographic immutability 分开。五项直接主张和十项禁止推断均待人工复核；FHIR
resource validation、official validator、profile/terminology conformance、DICOM
audit-message validation、本轮 server roundtrip、real-workflow-event test、clinical-
interoperability test 与 Human source decision 均为 `0`。这只把 Tier B review-surface
readiness 推进到 `6/13`，不产生 event truth、log integrity、authorization、identity、
novelty、Context、实现或实验效力。

Tier B 的 FHIR R4 ImagingStudy 4.0.1 现也有 source-specific zero-preselection
Human worksheet 与 decision gate。该界面把 versioned citation surface、generic imaging
linkage、source-object existence/retrieval、identity/UDI/authorization、subset/completeness、
resource separation 和 workflow-instance analysis unit 分开。五项直接主张和十一项禁止
推断均待人工复核；FHIR resource validation、official validator、profile/terminology
conformance、endpoint resolution、DICOM query/retrieval、source DICOM byte inspection、
本轮 server roundtrip、real-workflow test、clinical-interoperability test 与 Human source
decision 均为 `0`。这只把 Tier B review-surface readiness 推进到 `7/13`，不产生
source-object existence、retrieval、completeness、identity、authorization、UDI、novelty、
Context、实现或实验效力。

Tier B 的 OpenTelemetry Semantic Conventions 1.43.0 现也有 source-specific
zero-preselection Human worksheet 与 decision gate。该界面把 versioned citation
surface、generic telemetry assignment to C2R、attribute absence/requirement level、
stability、event representation/truth、correlation/medical binding 和 workflow-instance
analysis unit 分开。五项直接主张和十项禁止推断均待人工复核；SDK、instrumentation、
Collector、exporter、schema/code generation、validator、ingestion、correlation、event
verification、real-workflow test、clinical-interoperability test 与 Human source decision
均为 `0`。这只把 Tier B review-surface readiness 推进到 `8/13`，不产生 telemetry
truth、event truth、producer authenticity、completeness、clock trust、causality、identity、
authorization、medical binding、provenance、novelty、Context、实现或实验效力。

Tier B 的 SLSA 1.2 现也有 source-specific zero-preselection Human worksheet 与
decision gate。该界面把 immutable tag、maintained release branch、official-site
citation surface、generic software-supply-chain assignment to C2R、level/trust、
dependency completeness、medical-workflow non-inference 和 workflow-instance
analysis unit 分开。五项直接主张和十项禁止推断均待人工复核；verifier、build/source
workflow、attestation、signature、VSA、CI/CD、artifact、conformance、medical-event、
real-workflow、clinical-interoperability test 与 Human source decision 均为 `0`。
这只把 Tier B review-surface readiness 推进到 `9/13`，不产生 software artifact/source
truth、medical event truth、identity、authorization、medical semantics、clinical
correctness、provenance continuity、novelty、Context、实现或实验效力。

Tier B 的 GSN Version 3 现新增 source-specific zero-preselection Human worksheet、
decision gate 与边界测试。Human Research Owner 已确认字段集合和审查边界，但未选择
source、citation、role、claim、boundary 或 prohibited-inference 选项。四项直接主张与
十项禁止推断仍待逐项人工决定；parser、validator、model generation、well-formedness、
conformance、assurance evaluation、evidence resolution、medical workflow、clinical/
regulatory assessment 和 Paper 3 experiment 均为 `0`。Tier B review-surface readiness
现为 `10/13`；该确认不产生 argument truth、evidence truth、medical closure、novelty、
Context、实现或实验效力。

Tier B 的 C2PA 2.4 现新增 official-specification claim-boundary review（官方规范主张
边界审查）、零预选 Human worksheet、单一来源决定闸门与两组边界测试。该表面分开
generic content authenticity（通用内容真实性）、hard/soft binding（硬/软绑定）、
signature、signer trust 和 validation state，与 assertion truth、医疗主体/设备身份、
UDI、DICOM、action authorization、clinical correctness 及 workflow-instance evidence
closure。Tier B review-surface readiness 现为 `11/13`，但 C2PA Human source decision
仍为 `0`；未运行 validator、manifest/signature/binding/credential/asset 验证、互操作、
医疗工作流、临床、监管或 Paper 3 实验。

Tier B 的 NIST AI RMF 1.0 现新增 official full-text claim-boundary review（官方全文
主张边界审查）、零预选 Human worksheet、单一来源决定闸门与两组边界测试。该表面
把组织级 `GOVERN`、`MAP`、`MEASURE`、`MANAGE`、TEVV guidance 与 profiles，和
event-level evidence truth、medical semantic correctness、compliance、safety、risk
acceptance、authorization 及 deployment readiness 分开。Tier B review-surface
readiness 现为 `12/13`，但 NIST AI RMF Human source decision 仍为 `0`；未执行框架
应用、Core assessment、profile creation、risk-tolerance determination、measurement、
TEVV、compliance/conformance、医疗工作流、临床、监管或 Paper 3 实验。

Tier B 的 in-toto Specification 1.0 现新增 official stable-tag full-text review
（官方稳定标签全文审查）、零预选 Human worksheet、单一来源决定闸门与两组边界测试。
该表面把 layout、functionary、signature、link、materials/products、artifact rules 与
inspections 的软件供应链符合性，和 policy quality、现实事件真值、医疗身份/授权、
DICOM/UDI/model-action 语义及临床/监管结论分开。稳定 `v1.0` 标签与当前 `master`
正文不同，现已分别固定。Tier B review-surface readiness 现为 `13/13`，但 in-toto
Human source decision 仍为 `0`；未运行安装、metadata generation、签名、验证、
executable baseline、医疗工作流、临床、监管或 Paper 3 实验。

Tier A 五项来源现另有 analysis-unit distinction matrix（分析单元区分矩阵），
把不同来源的研究对象、证据原语、验证目标、重叠范围和残余问题拆开呈现，供
DEC-002 逐项人工决定。该矩阵只提高审查可解释性，不建立 novelty（新颖性），
不批准来源，也不把任何来源绑定到 Context Package。

Tier B 13 项官方标准与框架现也有独立 distinction matrix（区分矩阵），将
representation（表示）、provenance（来源追踪）、telemetry（遥测）、
attestation（证明）、assurance（保证）、governance（治理）和 content
integrity（内容完整性）的验证目标分开。它同样不批准来源、符合性或新颖性。

Tier C 4 项文档与同作者既有工作也已形成独立 distinction matrix（区分矩阵），
将 Model Cards（模型卡）、Datasheets（数据说明书）、Paper 1 profile validation
（第一篇配置验证）和 Paper 2 metadata readiness audit（第二篇元数据就绪度审计）
分开。至此 `22/22` 个 DEC-002 候选均有区别分析；当前 Human source decision
为完整受限 `1/22`、待审 `21/22`，Paper 2 仍是
`accepted_for_publication / awaiting_production`。

Tier C 的 Model Cards for Model Reporting、Datasheets for Datasets、已发表
UDI-DICOM Paper 1 与已接受 Paper 2 现均具备 source-specific（来源特定）主张边界
审查、零预选 Human worksheet、单一来源决定闸门与边界测试。Model Cards 把 model
reporting（模型报告）与 runtime evidence（运行时证据）分开；Datasheets 把 dataset
lifecycle documentation（数据集生命周期文档）与 runtime data use（运行时数据使用）
分开；Paper 1 把既有 profile、manifest、registry 和 validator 与 Paper 3 的
model/action/authority/provenance relationship diagnostic（模型／行为／授权／来源关系诊断）
分开；Paper 2 把公共元数据就绪度审计、合成正控与本地 Orthanc/FHIR 发布路径，和原始
设备真值、独立临床验证及 Paper 3 运行时闭环分开。Tier C review-surface readiness 现为
`4/4`。Paper 1 的审查字段集与边界是 AI 辅助准备面，尚无 Human 确认，也没有选择引用、
角色、主张、分析单元、禁止推断或来源决定；四项 Tier C source decision 均仍为 `null`。
Paper 2 保持 `accepted_for_publication / awaiting_production`，没有 DOI 或 version of
record（正式出版版本）绑定。未生成模型卡或 datasheet，未访问或使用数据集，未执行
Paper 1 validator、registry lookup、scanner/server route、DICOM 处理、基线、医疗工作流、
临床、监管或 Paper 3 实验。

EOA 现有一个 design-only（仅设计态）的 Introduction / Related Work
source-slot pack（引言/相关工作来源槽位包）：它覆盖全部 22 个候选来源 ID，
但不把候选来源渲染为正式引文，不批准 bibliography（参考文献集），也不建立
novelty（新颖性）、result（结果）或 scientific conclusion（科学结论）。

当前 v0.3 决策界面已按真实 Tier 数量 `5/13/4` 绑定全部 22 项来源区别材料，
但没有预选任何 Human decision。独立 novelty challenge（新颖性挑战）目前仅有
协议和空白记录，尚未分配审查人、未执行，也没有 novelty 结论。

Paper 3 另已形成独立 Human methods review（人工方法学审查）packet：绑定 23
个当前设计输入，覆盖 `MR-001..012` 与 `DMR-001..010` 共 22 个原有问题，并新增
`CV-001..012` 共 12 个 construct validity（构念效度）与 anti-tautology（反循环论证）
零预选问题。该记录
仍为空，不能把既有 AI-assisted recommendation（AI 辅助建议）升级为独立审查、
方法批准、`DEC-013` 决定、方案冻结或实验授权。
Research Agent Pilot 只读取这一状态；Context Package 仍为 `DRAFT`。

EOA 当前 preregistration readiness（预注册就绪度）镜像已更新到
`preregistration-readiness-gate-v0.2.yaml`：22/22 来源审查界面已就绪，完整受限
Human source decision 为 1/22，21/22 待审；满足闸门仍为 4/24。该计数修正没有批准
Context、bibliography freeze（参考文献冻结）、novelty、methods、protocol、实现、
Research Agent、实验或科学结论。

EOA 现另有 machine-readable preregistration readiness gate（机器可读预注册
就绪度闸门）：24 项条件中仅 4 项满足、20 项仍开放，并显式记录 protocol v0.1
与未批准 SAP v0.2 candidate（统计分析计划候选）之间的 protocol drift（协议
漂移）。该结果是只读审计状态，不是预注册、协议冻结、实现或实验授权。

该漂移现有独立 zero-preselection reconciliation packet（零预选协调包）和 Human
gate（人工闸门），提供四种协议／统计架构选项。AI 辅助建议为 `RECON-OPTION-A`，
但 Human decision 仍为 `null`，`PRG-008=false`、`PRG-010=false`，协议没有被改写，
满足闸门仍为 `4/24`。

EOA 的 `PRG-022` 现也有独立 preregistration target packet（预注册目标包）、
candidate freeze inventory（候选冻结清单）和 Human gate。四种 OSF/Zenodo 方案均
未选择；`PRT-OPTION-A` 只是非约束性 AI 辅助建议。没有创建、提交或批准外部注册，
没有 DOI 或 registration URL，满足闸门仍为 `4/24`。

EOA 的 `PRG-018` 现有 candidate ground-truth and blinding contract（候选基准真值与
盲法合同）。该合同把案例规范、夹具生成、标签复核、盲态执行和运行后核验分开，并
明确合成标签一致不等于外部医学验证。所有角色均未分配，没有标签、案例、blind pack、
leakage scan 或 benchmark 执行，`PRG-018=false`，满足闸门仍为 `4/24`。

EOA 现另有 evidence-closure construct operationalization（证据闭合构念操作化）
候选合同，将 contract conformance（合同一致性）、internal diagnostic validity（内部
诊断效度）、discriminant validity（区分效度）和 external validity（外部效度）分开。
外部效度保持 `OUT_OF_SCOPE_AND_UNTESTED`，所有人工字段为 `null`，没有独立审查、
实现、案例或结果；当前 Agent recommendation（智能体推荐结论）为
`DO_NOT_RECOMMEND_FOR_OPERATIONAL_OR_CUSTOMER_USE`。

EOA 的 Abstract Objective/Methods（摘要目标/方法）、Limitations（局限性）
和 provisional declarations（临时声明）现已形成 design-only pack（仅设计态
包）。Abstract Results 保持 `NOT_RUN`，Conclusion 保持 `NONE`；该包不表示
正式稿件、公开发布、伦理审查状态或实验结果已经形成。

EOA 现有一份 3,237 词 integrated manuscript design draft（整合稿件设计草案），
把 design-only（仅设计态）的 Abstract、Introduction、Related Work、Methods、
空 Results 结构、conditional Discussion（条件式讨论）、Limitations、Conclusion
gate（结论闸门）和 provisional declarations 连续装配。该装配保留 `DEC-002`、
结果、科学结论、声明和发布闸门，不是 submission manuscript（投稿稿件）。
新增 manuscript coherence matrix（稿件一致性矩阵）逐项追踪 4 个候选研究问题，
reviewer attack register（审稿攻击登记册）暴露 14 个风险；没有风险被记录为
经验上解决，这些工件不产生审稿决定或结果。两张 agent-readable（智能体可读）
SVG 设计图分别呈现受限权限模型与计划中的等源基准流程，均不含实验结果。
四张 agent-readable non-result design tables（智能体可读非结果设计表）
分别呈现方法/权限边界、pre-DEC-013 fault visibility（决定前故障可见性）、
候选 H1-H4 endpoint/falsification rules（端点/证伪规则）以及生成式
claims-ledger audit view（主张台账审计视图），同样不含实验结果、假设支持、
DEC-013 决定或主张验证。

## Core Boundaries（核心边界）

```text
Research Agent ≠ Digital Organism
Research Agent ≠ Scientist
AI Output ≠ Scientific Truth
Evaluation ≠ Authorization
Verification ≠ Scientific Conclusion
Reference ≠ Permission
Research Context ≠ Chat History
Context Package ≠ Scientific Truth
Human Approved Context ≠ Agent Authority
Unknown must remain Unknown
Human Review ≠ Agent Approval
Context Approval ≠ Scientific Truth
Source Selection ≠ Source Validation
Prototype Specification ≠ Prototype Instance
Experiment Result ≠ Publication Claim
Draft Paper ≠ Accepted Paper
```

- Research Agent（科研智能体）只能在未来明确范围内提供科研辅助；
- Human Research Owner（人类研究负责人）拥有科学结论与发表责任；
- Human Reviewer（人类复核者）检查过程、证据、异常和限制；
- DBOS 不控制研究结论，也不替代科学判断；
- SAEE 不修改实验或证据，也不决定论文结论；
- 任何 Literature Review（文献综述）、Plan（计划）、Draft（草稿）或 AI Output（人工智能输出）都不能自动升级为 Scientific Truth（科学真相）。

## Current Scope（当前范围）

当前允许：

- 定义 Pilot v0.1 的目的、能力边界和停止规则；
- 定义 Human Oversight Model（人工监督模型）；
- 定义 DBOS 与 SAEE 的概念性交接边界；
- 定义研究问题、未来实验计划和 Benchmark Design（基准设计）；
- 定义未来 Evidence Bundle（证据包）应如何保存；
- 定义未来 Research Agent 所需的 Research Context Package（研究上下文包）、来源、研究决策和 Unknown 边界；
- 定义 Human Research Owner 如何复核 Context 的所有权、范围、来源、Unknown 和 AI Usage Boundary；
- 定义 Prototype Readiness Gate（原型就绪闸门）、实验对象规范、Research Protocol、Metrics 和 Evidence Plan；
- 定义空 Experiment/Evidence/Evaluation Record 模板、Report 模板与 Manuscript Outline（论文结构）。

当前禁止：

- 创建或调用 Research Agent；
- 创建 Runtime、Digital Entity、Capability 或 Permission；
- 调用模型或执行科研任务；
- 处理或修改医学影像原始数据；
- 修改 DBA、DBOS 或 SAEE；
- 自主署名、投稿、发表或认证研究结论；
- 自动读取历史聊天记录、修改研究决策或产生 Research Result（研究结果）。

## Research Context Package（研究上下文包）

[`research-context/README.md`](research-context/README.md) 定义 Research Context Package Specification v0.1（研究上下文初始化包规范 v0.1）。它为未来 Research Agent 提供由 Human Research Owner 明确选择、版本化并确认的研究背景、研究决策、来源引用、Evidence Reference 和 Unknown 入口。

```text
Human Research Owner
  ↓
Research Context Package
  ↓ future read-only use after separate authorization
Research Agent
  ↓
Human Review
```

当前 Package 为 `DRAFT`，`source_documents: []`、`approved_by: []`。它没有抓取 Chat History，没有产生 Agent Authority、Evidence Truth 或 Research Result。详细只读边界见 [`architecture/research-context-integration-model.md`](architecture/research-context-integration-model.md)，采用理由见 [`ADR/ADR-002-research-context-package.md`](ADR/ADR-002-research-context-package.md)。

Paper 3 EOA Human Research Owner Context Handoff v0.1（人工研究负责人上下文交接包草案）入口见 [`research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/README.md`](research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/README.md)。它已组织 10 个来源候选、10 项研究决策、10 个 `UNKNOWN` 草案项及 10 份逐项 Unknown Record Draft，并提供零预选的 [`human-context-decision-input-template.yaml`](research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-input-template.yaml) 与固定 `HCD-001` 的 [`human-context-decision-record.yaml`](research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-context-decision-record.yaml)。后者已由 Human Research Owner 明确更新为 `HUMAN_CONFIRMED`：原 7 个来源选择、3 项研究决定、10 个 Unknown disposition、AI Usage Boundary 和 `APPROVAL_REQUIRED` autonomy preference 已记录；新增 DBA、SAEE、DBO 三项来源以及 `RD-009` 与独立复核者要求仍待决定。Handoff 保持 `DRAFT_PENDING_HUMAN_CONTEXT_REVIEW`，已批准来源 `0`、Human-reviewed Unknown Record `0`，Context Review 未签署。

EOA 当前新增一项 design-only（仅设计态）风险审计：19 个候选 C3
binding invariants（绑定不变量）中，现有 13 个 fault classes（故障类）
多数可能与强 C2R 通用关系比较器重叠。该结论不是实验结果；待人工决定的
`DEC-013` 将在“增加领域角色语义案例、重构 H1、移除增量假设”之间选择。
7 个扩展候选已有 AI-assisted feasibility review（AI 辅助可行性审查），
但没有任何类被批准。`DEC-013` 的 digest-bound（摘要绑定）零预选决策闸门
已经准备，主决定和 Option B 范围均为 `null`，没有 schema、实现、案例
生成或实验授权效力。

`DEC-002` 的 22 个外部候选来源现已具备 claim-linked（论断关联）逐项审查
界面：每项来源都映射到候选 Paper 3 claim、方法边界、领域规则、禁止推断和
引文版本状态。v0.2 模板是历史零预选界面；当前独立 ledger 已记录 1 个完整受限
`INCLUDE` 决定，并明确批量同意不能替代其余 21 项逐项来源审查。该决定不绑定
任何来源到 Context Package，也不改变
上述 Agent、实现、实验和科学结论禁令。

五个 Tier A 最近邻来源另有 zero-preselection（零预选）逐项决策卡：
`evidence-object-architecture/references/human-source-decision-batch-01-tier-a-v0.1.yaml`。
它只把候选 role（角色）、bounded claim（有限主张）、prohibited inference
（禁止推断）和待人工核对问题放在同一界面；当前完整受限 Human decision 为
`1/22`，Context approval、prototype authorization 与 experiment authorization
均未改变。

Tier B 的 13 项标准/框架和 Tier C 的 4 项基础/既有工作现已使用同一结构，
因此全部 22 个候选都有可逐项签署的 review card（审查卡）。这是
decision readiness（决策就绪），不是 22 项来源批准；当前 1 项受限批准、
21 项待审。

Human Research Owner Discovery v0.1（人工研究负责人发现流程）形成的候选已由人类确认并建立 [`human-owner-record.yaml`](research-context/handoffs/paper-3-eoa-human-owner-context-v0.1/human-owner-record.yaml)。`status: ASSIGNED` 只证明 `bin_zhang` 已接受本 Pilot 的科学责任，不批准 Context、Sources、Prototype 或 Experiment。

Human Context Review Checklist v0.1（人工研究上下文复核清单 v0.1）入口为 [`research-context/human-review-checklist.md`](research-context/human-review-checklist.md)。Review Record（复核记录）字段见 [`research-context/review-record-template.yaml`](research-context/review-record-template.yaml)，Human 与 Agent 责任分离见 [`architecture/human-context-governance-model.md`](architecture/human-context-governance-model.md)。当前仅定义清单和模板，`REVIEW_STATUS=REVIEW_PENDING`，没有执行 Review 或批准 Context。

Human Decision（人工决定）从输入、复核到独立 Context Update 的流程见 [`docs/human-decision-process.md`](docs/human-decision-process.md)。该流程禁止 AI 选择或推断 `HCD-001` 的决定，但允许根据明确 Human Input 作机械转录；并明确 `Decision Record ≠ Scientific Truth`、`Context Approval ≠ Experiment Authorization`、`Review Record ≠ Agent Permission`。

## v1.0 Research Execution Framework Preparation（v1.0 研究执行框架准备）

目标版本是 Research Agent Pilot v1.0，但当前只完成可在无执行授权下建立的规范、空模板和接口准备。Phase 1 Gate 的直接证据结论为 `NOT_READY`。

逐项完成证据与未完成项见 [`docs/v1.0-completion-audit.md`](docs/v1.0-completion-audit.md)。该审计明确区分 framework prepared（框架已准备）与 research loop complete（研究闭环完成）；当前后者为 `false`。

需要 Human Research Owner 亲自完成的 Owner、Sources、Unknown、Context Review、Prototype Authorization、Preregistration 与 Experiment Authorization 顺序见 [`docs/human-authorization-handoff.md`](docs/human-authorization-handoff.md)。该 Handoff（交接清单）不代替人类决定。

| Phase | 已建立入口 | 当前事实状态 |
|---|---|---|
| 1. Prototype Readiness | [`architecture/research-agent-readiness-gate.md`](architecture/research-agent-readiness-gate.md) | `NOT_READY`；Context、Owner、Sources、Unknown Record 与人工授权未满足 |
| 2. Minimal Prototype | [`prototype/prototype-specification.md`](prototype/prototype-specification.md) | `DESIGN_ONLY_NOT_AUTHORIZED`；Instance `0` |
| 3. Research Protocol | [`research/experiment-protocol.md`](research/experiment-protocol.md) | `DRAFT_NOT_AUTHORIZED`；未预注册、未执行 |
| 4. Evaluation Metrics | [`research/evaluation-metrics.md`](research/evaluation-metrics.md) | 已定义 1 个 Primary 与 5 个 Secondary；未预注册、无结果 |
| 5. Research Tasks | [`prototype/task-definition.md`](prototype/task-definition.md) | 4 项 Paper 3 EOA 任务已定义；来源未绑定、执行 `0` |
| 6. Evidence Flow | [`evidence/research-evidence-model.md`](evidence/research-evidence-model.md) | `PLAN_DEFINED_NOT_EXECUTED`；Records `0` |
| 7. DBOS Preparation | [`architecture/dbos-integration-model.md`](architecture/dbos-integration-model.md) | `PREPARED_ONLY`；没有 DBOS 调用或修改 |
| 8. SAEE Preparation | [`architecture/saee-evaluation-model.md`](architecture/saee-evaluation-model.md) | `PREPARED_ONLY`；没有 SAEE 调用、修改或输出 |
| 9. Reports | [`reports/experiment-report-template.md`](reports/experiment-report-template.md)、[`reports/analysis-report-template.md`](reports/analysis-report-template.md) | `EMPTY_TEMPLATE`；不是 Report 实例 |
| 10. Paper Preparation | [`paper/manuscript-outline.md`](paper/manuscript-outline.md) | `DRAFT_ONLY`；只有结构，没有 Manuscript Draft 或 Results |

空模板入口：

- [`research/experiment-record-template.yaml`](research/experiment-record-template.yaml)：Experiment Record Template（实验记录模板）；
- [`evidence/evidence-record-template.yaml`](evidence/evidence-record-template.yaml)：Evidence Record Template（证据记录模板）；
- [`evaluation/evaluation-result-template.yaml`](evaluation/evaluation-result-template.yaml)：Evaluation Result Template（评价结果模板）。
- [`evidence/verification-result-template.yaml`](evidence/verification-result-template.yaml)：Verification Result Template（验证结果模板）；
- [`prototype/prototype-authorization-template.yaml`](prototype/prototype-authorization-template.yaml)：Prototype Authorization Template（原型授权模板）；
- [`research/experiment-authorization-template.yaml`](research/experiment-authorization-template.yaml)：Experiment Authorization Template（实验授权模板）；
- [`research/preregistration-checklist.md`](research/preregistration-checklist.md)：实验预注册清单。
- [`research/protocol-freeze-candidate.yaml`](research/protocol-freeze-candidate.yaml)：17 个 Protocol、Task、Metrics、Evidence、Context、DBOS/SAEE 边界文件的 `sha256` 冻结候选；`DRAFT_FREEZE_CANDIDATE_NOT_APPROVED`。

这些模板不得在真实授权执行前填入结果。

## Agent-readable Entry Order（智能体可读入口顺序）

编码智能体、检索智能体和引用智能体应按以下顺序读取：

0. [`CONSTITUTION.md`](CONSTITUTION.md)：仓库沟通宪法；所有英文表达必须紧邻提供中文翻译或释义；
1. [`AGENTS.md`](AGENTS.md)：仓库级工作边界和停止规则；
2. [`architecture/pilot-specification.md`](architecture/pilot-specification.md)：Pilot v0.1 的规范真源；
3. [`architecture/human-oversight-model.md`](architecture/human-oversight-model.md)：角色与人工闸门；
4. [`architecture/dbos-integration-model.md`](architecture/dbos-integration-model.md)：DBOS 只读引用边界；
5. [`architecture/saee-evaluation-model.md`](architecture/saee-evaluation-model.md)：SAEE 输入、输出与非权限边界；
6. [`research-context/README.md`](research-context/README.md)：Research Context Package 规范、来源规则和生命周期；
7. [`research-context/human-review-checklist.md`](research-context/human-review-checklist.md)：Human Context Review 的六部分检查清单；
8. [`architecture/human-context-governance-model.md`](architecture/human-context-governance-model.md)：Human Review、Context Approval 和 Agent Read Access 的责任分离；
9. [`architecture/research-context-integration-model.md`](architecture/research-context-integration-model.md)：未来 Agent 的只读使用流程；
10. [`architecture/research-agent-readiness-gate.md`](architecture/research-agent-readiness-gate.md)：Prototype 创建前提与当前 `NOT_READY` 证据；
11. [`prototype/prototype-specification.md`](prototype/prototype-specification.md)：最小实验对象边界；
12. [`prototype/task-definition.md`](prototype/task-definition.md)：四项真实科研任务定义；
13. [`prototype/human-interaction-model.md`](prototype/human-interaction-model.md)：Prototype 与 Human 的交互和复核边界；
14. [`research/research-question.md`](research/research-question.md)：研究问题和可回答条件；
15. [`research/experiment-protocol.md`](research/experiment-protocol.md)：三条件 Research Protocol；
16. [`research/evaluation-metrics.md`](research/evaluation-metrics.md)：主要与次要评价指标；
17. [`research/experiment-plan.md`](research/experiment-plan.md)：未来对照实验设计；
18. [`research/benchmark-design.md`](research/benchmark-design.md)：Paper 3 EOA 任务集设计；
19. [`evidence/README.md`](evidence/README.md)：Evidence 类别与零记录事实面；
20. [`evidence/research-evidence-model.md`](evidence/research-evidence-model.md)：Evidence 流程和失败保留；
21. [`research/protocol-freeze-candidate.yaml`](research/protocol-freeze-candidate.yaml)：预注册前的 17 项文件哈希候选；当前未获批准；
22. [`research/experiment-record-template.yaml`](research/experiment-record-template.yaml)：Experiment Record 空模板；
23. [`evidence/evidence-record-template.yaml`](evidence/evidence-record-template.yaml)：Evidence Record 空模板；
24. [`evaluation/evaluation-result-template.yaml`](evaluation/evaluation-result-template.yaml)：Evaluation Result 空模板；
25. [`reports/experiment-report-template.md`](reports/experiment-report-template.md)：实验报告空模板；
26. [`reports/analysis-report-template.md`](reports/analysis-report-template.md)：分析报告空模板；
27. [`paper/manuscript-outline.md`](paper/manuscript-outline.md)：`DRAFT_ONLY` 论文结构；
28. [`docs/v1.0-completion-audit.md`](docs/v1.0-completion-audit.md)：v1.0 六类产物和 Phase 1–10 的完成证据审计；
29. [`docs/human-authorization-handoff.md`](docs/human-authorization-handoff.md)：Human Research Owner 的直接证据与授权交接顺序；
30. [`ADR/ADR-001-research-agent-pilot.md`](ADR/ADR-001-research-agent-pilot.md)：独立建仓决策；
31. [`ADR/ADR-002-research-context-package.md`](ADR/ADR-002-research-context-package.md)：受控上下文包决策；
32. [`ADR/ADR-003-human-context-review.md`](ADR/ADR-003-human-context-review.md)：人工上下文复核决策。

文档中的 `allowed` 表示“可进入未来人工审查的候选范围”，不表示当前已有 Capability、Permission、Runtime 或执行授权。

## Pre-development Agent Review（开发前智能体审查）

面向“如果潜在客户咨询，你会推荐本程序吗？”这一问题，当前结论为：

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED_AS_SPECIFICATION
IMPLEMENTED_PROGRAM_RECOMMENDATION=NOT_RECOMMENDED
PROJECT_INITIALIZATION_RECOGNIZED=true
IMPLEMENTATION_AUTHORIZED=false
PROTOTYPE_READINESS_RECOMMENDATION=DO_NOT_CREATE_PROTOTYPE_YET
```

可以把本仓库推荐给需要治理边界和实验设计参考的研究团队；不能把它推荐为可运行 Research Agent、经过验证的 DBOS 应用或医学科研产品。不推荐原因及对应修正记录在 [`ADR/ADR-001-research-agent-pilot.md`](ADR/ADR-001-research-agent-pilot.md)，当前 Prototype 判断见 [`architecture/research-agent-readiness-gate.md`](architecture/research-agent-readiness-gate.md)。

## Current Status（当前状态）

```text
PROJECT_INITIALIZED=true
V1_0_STATUS=INCOMPLETE_NOT_READY
RESEARCH_LOOP_COMPLETE=false
PILOT_SPECIFICATION_DEFINED=true
EXPERIMENT_PLAN_DEFINED=true
BENCHMARK_DESIGN_DEFINED=true
RESEARCH_CONTEXT_PACKAGE_SPECIFICATION_DEFINED=true
CONTEXT_PACKAGE_STATUS=DRAFT
CONTEXT_HANDOFF_STATUS=DRAFT_PENDING_HUMAN_CONTEXT_REVIEW
CONTEXT_HANDOFF_DRAFT_PREPARED=true
OWNER_CANDIDATES_DISCOVERED=1
OWNER_CANDIDATE_STATUS=CONFIRMED_AND_ASSIGNED
OWNER_DISCOVERY_CONFIDENCE=MEDIUM
OWNER_CONFIRMATION_REQUIRED=false
HUMAN_RESEARCH_OWNER_ASSIGNED=true
HUMAN_RESEARCH_OWNER_REFERENCE=bin_zhang
HUMAN_OWNER_RECORD_INSTANCE_CREATED=true
INDEPENDENT_HUMAN_REVIEWER_REQUIRED=UNKNOWN
SOURCE_CANDIDATES=7
SOURCE_DOCUMENTS=0
APPROVED_BY=0
CHAT_HISTORY_IMPORTED=false
HUMAN_CONTEXT_REVIEW_CHECKLIST_DEFINED=true
HUMAN_CONTEXT_REVIEW_EXECUTED=false
HUMAN_CONTEXT_DECISION_INPUT_TEMPLATE_PREPARED=true
HUMAN_CONTEXT_DECISION_RECORD_PREPARED=true
HUMAN_CONTEXT_DECISION_RECORD_STATUS=HUMAN_CONFIRMED
HUMAN_CONTEXT_DECISIONS_STATUS=RECORDED
HUMAN_CONTEXT_DECISIONS_RECORDED=23
REVIEW_RECORD_INSTANCE_CREATED=false
REVIEW_STATUS=REVIEW_PENDING
DRAFT_UNKNOWN_ENTRIES=10
UNKNOWN_RECORD_DRAFTS=10
HUMAN_REVIEWED_UNKNOWN_RECORDS=0
CONTEXT_APPROVED=false
HUMAN_GATE_TEMPLATES_DEFINED=true
HUMAN_GATE_RECORD_INSTANCES=2
HUMAN_AUTHORIZATION_HANDOFF_DEFINED=true
READINESS_STATUS=NOT_READY
PROTOTYPE_SPECIFICATION_DEFINED=true
PROTOTYPE_INSTANCE_CREATED=false
RESEARCH_PROTOCOL_DEFINED=true
PROTOCOL_STATUS=DRAFT_NOT_AUTHORIZED
EXPERIMENT_AUTHORIZED=false
PREREGISTRATION_COMPLETED=false
PROTOCOL_FREEZE_CANDIDATE_PREPARED=true
PROTOCOL_FREEZE_CANDIDATE_STATUS=DRAFT_FREEZE_CANDIDATE_NOT_APPROVED
PROTOCOL_FREEZE_ARTIFACTS=17
PROTOCOL_FREEZE_APPROVED=false
PROTOTYPE_AUTHORIZATION_RECORD_CREATED=false
EXPERIMENT_AUTHORIZATION_RECORD_CREATED=false
EXPERIMENT_RECORDS=0
EVIDENCE_PLAN_DEFINED=true
EVIDENCE_RECORDS=0
EVALUATION_RESULTS=0
VERIFICATION_RESULTS=0
ANALYSIS_REPORT_CREATED=false
MANUSCRIPT_OUTLINE_DEFINED=true
MANUSCRIPT_DRAFT_CREATED=false
DBOS_CONNECTION_STATUS=PREPARED_ONLY
SAEE_CONNECTION_STATUS=PREPARED_ONLY
Paper Status = DRAFT_ONLY
Agent=0
Runtime=0
Entity=0
Digital Entity=0
Permission=0
Execution=0
Research Result=0
Agent Instance = 0
Runtime = 0
Digital Entity = 0
Permission = 0
DBOS_MODIFIED=false
SAEE_MODIFIED=false
DBA_MODIFIED=false
SCIENTIFIC_CONCLUSION_CREATED=false
```

本状态说明文件与 Git 仓库已初始化；不说明 Pilot 已实施、实验已运行、证据已产生或研究问题已有答案。
