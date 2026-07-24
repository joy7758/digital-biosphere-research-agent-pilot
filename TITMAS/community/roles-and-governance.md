# Ecosystem & Release Mechanism（生态与发布机制）

## Roles Definition（角色定义）
- **Core Contributor（核心贡献者）**：负责架构演进与 ADR 的起草，能够合并底层基础架构的代码变更。
- **Observer（观察者）**：拥有 Read-Only（只读）权限的开发者，负责提供反馈、参与试验（Trial）和试点项目（Pilot）。
- **Independent Reviewer（独立复核者）**：独立于项目负责人的安全或合规审计人员，在发布前验证安全性与合规性。
- **Research Owner（研究负责人）**：拥有最高级别的科学责任与授权权利，批准特定 Context（上下文）的演化或研究结论。

## Governance Process & Release Gates（治理流程与发布闸门）
1. **Proposal（提案）**：任何演进需通过 ADR 的形式提交。
2. **Review & Audit（复核与审计）**：Reviewer（复核者）需评估对架构边界和宪法约定的影响。
3. **Approval Gate（审批闸门）**：通过闸门才能进行正式发布宣言，不得跨越流程提前宣告产品化。
4. **Controlled Trial（受控试用）**：所有新发布先在特定的受控范围（Trial）内进行集成验证。

## Version Compatibility & Deprecation Strategy（版本兼容与废弃策略）
- 遵循 Semantic Versioning（语义化版本控制）。
- 主版本升级（Major Upgrade）表示架构模型、数据契约或核心接口的不兼容更改，需要至少提前一个 Minor（次要）版本发布 Deprecation Notice（废弃通知）。
- 被废弃的接口会在之后的演化中明确移出（Evicted），并更新相应的 Reference（引用）说明。
