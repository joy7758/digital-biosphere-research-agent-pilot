# Governance & ADR Model（治理与 ADR 模型）

## Decision / Adoption / Governance（决策 / 采纳 / 治理）约束链
- **Decision（决策）**：所有架构、契约和标准的重大更改必须由核心贡献者提出并记录为 ADR (Architecture Decision Record，架构决策记录)。
- **Adoption（采纳）**：在正式发布前，必须在 Trial（试用）或 Pilot（试点）中验证变更的有效性与可复现性。
- **Governance（治理）**：在 TITMAS 社区中，决策通过特定的审批闸门（Approval Gates）进行，不直接依赖于单一开发者或 Agent 的意图。

## Architecture Change & Versioning（架构变更与版本控制规则）
1. **ADR Process（ADR 流程）**：
   - 任何涉及接口、数据契约、安全模型以及 DBOS（数字生物圈操作系统）/SAEE（自适应演化评估）边界的修改，均需提交 ADR（Architecture Decision Record，架构决策记录）。
   - ADR（架构决策记录）必须详细列出变更原因、潜在影响以及实施计划。
2. **Approval Mechanism（审批机制）**：
   - 需要至少一名 Reviewer（复核者）进行独立审计，确保变更符合 Constitution（宪法）及安全边界。
   - Owner（所有者）必须批准后，才能合并至主线版本。
3. **Version Governance（版本治理）**：
   - 采用 Semantic Versioning（语义化版本控制）。
   - 不向前兼容的变更需提供清晰的迁移路径并发布在 Release Notes（发布说明）中。
