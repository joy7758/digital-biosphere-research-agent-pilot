# DEB-001 Lite Dry Run Result Report v0.1（DEB-001 Lite 试运行结果报告 v0.1）

## Record boundary（记录边界）

This record documents a local workflow-validation run only. It is not a scientific
experiment result, Digital Survival Theory validation, runtime authorization,
production execution, or publication claim.

本记录只描述一次本地工作流验证。它不是科学实验结果、Digital Survival Theory
（数字生存理论）验证、运行时授权、生产执行或发表主张。

```text
RECORD_CLASS=LOCAL_WORKFLOW_VALIDATION_ONLY
SCIENTIFIC_RESULT=false
DST_VALIDATED=false
RUNTIME_AUTHORITY_GRANTED=false
PRODUCTION_EXECUTION=false
```

## 1. Dry run identity（试运行身份）

- `dry_run_id`: `DEB-001-LITE-VALIDATION-002`
- `experiment_id`: `DEB-001-LITE`
- `version`: `v0.1`
- `seed`: `20260725`
- `phase_plan`: `Stable -> Shock -> Recovery`
- `rounds`: `3 + 2 + 2 = 7`
- `population`: `Efficiency x3, Balance x3, Exploration x3`

## 2. Workflow validation summary（工作流验证摘要）

| Validation target（验证目标） | Status（状态） | Direct observation（直接观察） |
|---|---|---|
| Initialization（初始化） | `PASS` | 9 个规则型模拟个体以相同资源基线初始化 |
| Agent setup（个体设置） | `PASS` | 三类策略各 3 个，9 个 `lineage_id`（谱系编号）全局唯一 |
| Phase transitions（阶段转换） | `PASS` | 按 `Stable -> Shock -> Recovery` 完成 7 轮 |
| Evidence generation（证据生成） | `PARTIAL` | 4 个要求的日志均已生成；校验和和 `lineage_log`（谱系日志）边界尚未关闭 |
| Result generation（结果生成） | `PASS` | 已生成 `DEB-001-LITE-MINIMAL-RESULT-v0.1.json` |
| Same-seed replay（同种子重放） | `PASS` | 四个 CSV 日志逐字节一致；去除时间戳和存储路径后的 JSON 结果一致 |

## 3. Checklist outcome（清单结果）

```text
OVERALL_DRY_RUN_STATUS=PARTIAL
ALPHA_READINESS_RECOMMENDATION=NEEDS_REVISION
```

`PARTIAL`（部分通过）表示最小执行路径和输出结构可以完成，但实验参数与证据闭包
尚不足以支持 Alpha（首轮真实实验）执行或科学解释。

## 4. Observed local outputs（观察到的本地输出）

| Strategy（策略） | Active agents（活跃个体） | Continuation rate（延续率） | Final average resource（最终平均资源） |
|---|---:|---:|---:|
| Efficiency（效率型） | 3 | 1.0 | 37.6401 |
| Balance（平衡型） | 3 | 1.0 | 32.6060 |
| Exploration（探索型） | 3 | 1.0 | 31.2185 |

Additional observations（补充观察）：

- `dropout_count=0`：没有个体退出，因此本次运行没有观察到群体构成变化；
- `behavior_change_count=33`：记录到规则驱动的动作变化，但这不等于选择优势；
- Stable、Shock、Recovery（稳定、冲击、恢复）阶段的资源快照已分别记录；
- 不同种子 `20260725`、`20260726`、`20260727` 产生不同环境乘数序列；
- 上述数值仅用于工作流检查，不支持总体规律、因果或 DST 有效性主张。

## 5. Issues discovered（发现的问题）

### Corrected in this revision（本次已修正）

- 阶段结果曾错误引用最终状态；现改为阶段结束时的真实快照；
- Efficiency（效率型）与 Exploration（探索型）的谱系编号曾重复；现使用
  `EFF`、`BAL`、`EXP` 前缀保证唯一；
- `seed`（随机种子）曾只存在于元数据；现控制对所有策略公平的环境乘数序列；
- 日志曾缺少实验版本和种子字段；现补充到每类日志。

### Remaining（仍未关闭）

- Lite 规范中的共享资源池仍使用 `R0` 和 `R_agent` 占位符，尚无冻结数值；
- 7 轮运行没有退出事件，尚未证明可观察到 continuation selection
  （延续选择）差异；
- `DEB-001-LITE-EXECUTION-PROTOCOL-v0.1.md` 要求 `lineage_log`，而 Dry Run
  计划和最小结果只要求 4 个日志，规范之间仍需人工统一；
- 证据引用尚未包含 source ID（来源编号）和不可变 checksum（校验和）；
- 9 个个体、7 轮和 3 个种子只支持工程检查，不支持统计意义主张；
- Pilot（试验仓库）的正式 Prototype / Experiment Authorization
  （原型／实验授权）状态仍需由人工责任方单独记录和同步。

## 6. Corrective actions（修正动作）

Before Alpha execution review（进入 Alpha 执行审查前）：

1. 冻结共享资源总量、个体初始资源和每轮资源补充／消耗规则；
2. 冻结 continuation threshold（延续阈值）和 shock severity（冲击强度），确保
   它们可以产生可观察但非预设结论的选择压力；
3. 统一 `lineage_log` 是否为 Lite 必需输出；
4. 为 4 个证据文件增加不可变摘要和来源编号；
5. 使用多个预注册种子运行，并预先定义 `supported`、`rejected`、
   `inconclusive`（支持、拒绝、不确定）解释规则；
6. 由 Human Research Owner（人工研究负责人）记录适用于该版本的明确授权，
   再重新执行 readiness review（就绪审查）。

## 7. Independent agent recommendation gate（独立智能体推荐闸门）

DeepSeek `deepseek-v4-flash`（深度求索快速模型）在修正前给出的状态为
`NOT_RECOMMENDED`（不推荐）。主要原因是阶段快照污染、谱系编号冲突、种子未实际
控制流程、规模过小且没有独立复现。

本次工作关闭了前三项工程缺陷，并完成一次同种子独立重放。规模、共享资源模型、
选择事件可观察性、证据校验和和正式人工授权仍未关闭，因此本报告不把推荐状态自动
升级为产品推荐或 Alpha 执行许可。

修正后的独立复审给出分层状态：

```text
LOCAL_WORKFLOW_PROTOTYPE_RECOMMENDATION=RECOMMENDED
SCIENTIFIC_OR_ALPHA_EXECUTION_RECOMMENDATION=NOT_RECOMMENDED
```

`RECOMMENDED`（推荐）仅适用于检查三阶段流程和基础 CSV / JSON 输出结构的最小本地
原型。`NOT_RECOMMENDED`（不推荐）继续适用于科学结论、Alpha 实验执行、产品级工具
或任何运行授权。复审仍要求统一 `lineage_log` 边界，并在进入 Alpha 前冻结共享资源、
关闭证据校验和、形成可观察的延续差异及取得正式人工授权。

## 8. Alpha readiness recommendation（Alpha 就绪建议）

```text
RECOMMENDATION=NEEDS_REVISION
```

The workflow is technically observable and replayable at the local prototype level,
but the experiment definition is not yet closed enough for Alpha execution.

工作流在本地原型层面已经可观察、可重放，但实验定义尚未闭包，不应进入 Alpha 执行。

## 9. Evidence references（证据引用）

- `agent_state_log.csv`
- `selection_log.csv`
- `phase_log.csv`
- `outcome_log.csv`
- `DEB-001-LITE-MINIMAL-RESULT-v0.1.json`

These are local workflow-validation artifacts only and currently have no immutable
digest closure.

这些只是本地工作流验证产物，目前没有不可变摘要闭包。

## 10. Limitations（限制）

- not a scientific result（不是科学结果）
- not DST validation（不是 DST 验证）
- not production execution（不是生产执行）
- not runtime or governance authority（不是运行时或治理权力）
- not evidence truth（不是证据真值）
- not authorization for Alpha execution（不是 Alpha 执行授权）
