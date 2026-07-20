# Contributing（贡献指南）

## Scope（范围）

当前只接受对 Specification（规范）、Research Design（研究设计）、Human Oversight（人工监督）、Integration Boundary（集成边界）和 Evidence Policy（证据政策）的改进。

任何 Agent 实现、Runtime、模型调用、科研执行、DBOS/SAEE 写入或外部发表都超出当前仓库授权。

## Required Change Process（必要变更流程）

1. 读取 `AGENTS.md` 与 `README.md`；
2. 明确变更属于规范、研究设计还是状态修复；
3. 检查是否会把 `Reference` 写成集成、把 `Plan` 写成执行或把 `Evaluation` 写成授权；
4. 若变更可能进入实现阶段，先完成 Pre-development Recommendation Gate（开发前推荐闸门）；
5. 保持 Human Research Owner、Human Reviewer 与 Research Agent 的责任分离；
6. 更新所有受影响的状态常量和交叉链接；
7. 在 commit 前运行结构、链接、空白和状态边界检查。

## Documentation Rules（文档规则）

- 对每个重要 English Term（英文术语）给出简短中文释义；
- 使用显式状态，如 `defined-not-answered`、`design-only`、`false` 和 `0`；
- 任何尚未验证的事实保留 `unknown`，不得推测；
- 清楚区分 Specification、Implementation、Execution、Verification、Evaluation 和 Scientific Conclusion；
- 新文件必须从 README 或相邻规范链接，便于编码、检索和引用智能体发现；
- 示例必须标为 example（示例）或 future（未来），不能伪装成实例证据。

## Commit Checklist（提交检查清单）

- [ ] 请求范围内的文件完整；
- [ ] Markdown 相对链接存在；
- [ ] `git diff --check` 通过；
- [ ] `Agent=0`；
- [ ] `Runtime=0`；
- [ ] `Digital Entity=0`；
- [ ] `Permission=0`；
- [ ] `Execution=0`；
- [ ] 未修改 DBA、DBOS 或 SAEE；
- [ ] 没有把本地检查写成科研验证或产品能力。

## Future Implementation Proposals（未来实现提案）

未来若提出实现，必须单独说明潜在客户场景、智能体是否推荐、不推荐原因、风险分解、所需修正、DBOS/SAEE 契约、数据与伦理边界、验证计划和人工授权。规范通过本身不授权实现。
