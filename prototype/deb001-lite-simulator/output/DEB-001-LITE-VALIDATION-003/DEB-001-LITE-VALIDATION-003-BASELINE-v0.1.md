# DEB-001 Lite Validation-003 Baseline v0.1（DEB-001 Lite 第三次验证基线 v0.1）

## Baseline declaration（基线声明）

This document freezes Validation-003 as the first successful reproducible
DEB-001 Lite local validation baseline.

本文件将 Validation-003（第三次验证）冻结为首个成功且可复现的 DEB-001 Lite
本地验证基线。

```text
BASELINE_ID=DEB-001-LITE-VALIDATION-003-BASELINE-v0.1
BASELINE_STATUS=FROZEN_LOCAL_VALIDATION_BASELINE
DRY_RUN_WORKFLOW_STATUS=PASS
ALPHA_STATUS=PENDING_REVIEW
SCIENTIFIC_RESULT=false
DST_VALIDATED=false
```

`FROZEN_LOCAL_VALIDATION_BASELINE`（已冻结的本地验证基线）只固定本次运行的配置、
证据和观察结果。它不创建 Runtime Authority（运行时权力）、Experiment
Authorization（实验授权）或 Scientific Truth（科学真值）。

## 1. Validation identity（验证身份）

| Field（字段） | Frozen value（冻结值） |
|---|---|
| `run_id` | `DEB-001-LITE-VALIDATION-003` |
| `experiment_id` | `DEB-001-LITE` |
| `version` | `v0.1` |
| `seed` | `20260725` |
| `timestamp` | `2026-07-25T01:25:40.545957+00:00` |
| `validation_status` | `PASS` |
| `record_class` | `LOCAL_WORKFLOW_VALIDATION_ONLY` |

Frozen implementation reference（冻结实现引用）：

- simulator（模拟器）: `prototype/deb001-lite-simulator/simulator.py`
- SHA-256（安全哈希算法摘要）:
  `aafbe950dfd266f7af57286088b3494fada46cfbacbc8530fbb3a3b354efb042`

Frozen result reference（冻结结果引用）：

- result object（结果对象）:
  `DEB-001-LITE-MINIMAL-RESULT-v0.1.json`
- raw SHA-256（原始文件摘要）:
  `8a817c292d4b514f9f8335d3da7263884f6b1340ebdf49b09c3751e3337a4015`
- normalized SHA-256（去除时间戳和存储位置后的标准化摘要）:
  `efa0c2b0b0ea28dbd6dd75d6c1243e6d4d8a3e2deda047586705483d4e6a3bb8`

## 2. Simulator configuration（模拟器配置）

### 2.1 Agent population（个体群体）

| Strategy（策略） | Count（数量） | Agent IDs（个体编号） | Lineage prefix（谱系前缀） |
|---|---:|---|---|
| Efficiency（效率型） | 3 | `EFFI1`, `EFFI2`, `EFFI3` | `EFF-lineage-*` |
| Balance（平衡型） | 3 | `BALA1`, `BALA2`, `BALA3` | `BAL-lineage-*` |
| Exploration（探索型） | 3 | `EXPL1`, `EXPL2`, `EXPL3` | `EXP-lineage-*` |

Frozen common initial state（冻结共同初始状态）：

- initial resource（初始资源）: `24.0`
- initial active state（初始活跃状态）: `ACTIVE`
- generation（代数）: `0`
- member continuation biases（成员延续偏置）: `-0.06`, `0.00`, `0.06`
- population total（群体总数）: `9`

三个延续偏置按成员位置对称应用于每类策略，用于避免同策略成员必然同时退出。它们是
本基线参数，不是隐藏随机变量。

### 2.2 Phase and round configuration（阶段与轮次配置）

| Phase（阶段） | Global rounds（全局轮次） | Round count（轮数） | Environment multipliers（环境乘数） |
|---|---|---:|---|
| Stable（稳定） | `0-2` | 3 | `1.0000`, `1.0000`, `1.0000` |
| Shock（冲击） | `3-4` | 2 | `0.2316`, `0.1618` |
| Recovery（恢复） | `5-6` | 2 | `0.9839`, `1.0865` |

Frozen phase order（冻结阶段顺序）：

```text
Stable -> Shock -> Recovery
```

Shock（冲击）阶段统一 scarcity cost（稀缺成本）为 `4.5`。

### 2.3 Strategy profiles（策略配置）

#### Efficiency（效率型）

- Stable（稳定）与 Recovery（恢复）默认选择 `exploit`（利用）；
- Shock（冲击）期间资源不低于 `18.0` 时选择 `exploit`，低于该值时选择 `adapt`
  （适应）；
- `exploit` reward/cost（收益／成本）: `7.0 / 3.0`；
- `adapt` reward/cost（收益／成本）: `2.5 / 2.0`；
- Shock 期间执行 `exploit` 的 mismatch penalty（错配惩罚）: `4.5`。

#### Balance（平衡型）

- Stable（稳定）阶段按固定轮次规则交替 `explore`（探索）与 `exploit`；
- Shock（冲击）阶段在偶数阶段轮选择 `explore`，奇数阶段轮选择 `exploit`；
- Recovery（恢复）阶段按固定轮次规则限制探索；
- `explore` reward/cost（收益／成本）: `3.2 / 2.0`；
- `exploit` reward/cost（收益／成本）: `4.5 / 2.5`；
- Shock 期间低资源利用的条件惩罚: 资源低于 `12.0` 时惩罚 `1.0`。

#### Exploration（探索型）

- Stable（稳定）阶段按轮次交替 `explore` 与 `exploit`；
- Shock（冲击）阶段按轮次交替 `explore` 与 `adapt`；
- Recovery（恢复）阶段选择 `explore`；
- `explore` reward/cost（收益／成本）: `3.0 / 2.2`；
- `adapt` reward/cost（收益／成本）: `2.8 / 1.5`；
- `exploit` reward/cost（收益／成本）: `2.2 / 2.0`。

### 2.4 Adaptation and continuation rules（适应与延续规则）

Frozen adaptation increments（冻结适应增量）：

- `adapt`: `+0.35`
- `explore`: `+0.20`
- `exploit`: `+0.00`
- maximum adaptation level（最大适应水平）: `1.00`

Frozen continuation score concept（冻结延续分数概念）：

```text
continuation_score =
    resource_component
  + phase_adaptation_component
  + strategy_behavior_component
  + member_continuation_bias
```

Frozen continuation thresholds（冻结延续阈值）：

| Phase（阶段） | Threshold（阈值） |
|---|---:|
| Stable（稳定） | `0.20` |
| Shock（冲击） | `0.35` |
| Recovery（恢复） | `0.25` |

当资源耗尽或 `continuation_score` 低于阶段阈值时，个体转换为 `DROPPED`（已退出）。
本基线不支持退出后的重新进入。

## 3. Observed results（观察结果）

### 3.1 Stable survival（稳定阶段存续）

```text
ACTIVE_START=9
ACTIVE_END=9
ACTIVE_DELTA=0
```

Stable（稳定）阶段全部 9 个个体存续，没有退出事件。

### 3.2 Shock selection event（冲击阶段选择事件）

```text
ACTIVE_START=9
ACTIVE_END=8
ACTIVE_DELTA=-1
```

Observed transition（观察到的转换）：

| Field（字段） | Value（值） |
|---|---|
| `round` | `4` |
| `agent_id` | `EFFI1` |
| `lineage_id` | `EFF-lineage-1` |
| `strategy_origin` | `Efficiency` |
| `generation` | `0` |
| `state_transition` | `ACTIVE->DROPPED` |
| `continuation_score` | `0.3047` |
| `continuation_threshold` | `0.3500` |

Recorded reason（记录原因）：延续分数低于冲击阶段阈值，且 Efficiency（效率型）
行为在环境变化中保持了高错配利用。

### 3.3 Recovery state（恢复阶段状态）

```text
ACTIVE_START=8
ACTIVE_END=8
ACTIVE_DELTA=0
```

Recovery（恢复）阶段没有新增退出。最终策略结果：

| Strategy（策略） | Active agents（活跃个体） | Continuation rate（延续率） | Average resource（平均资源） | Explicit adaptation events（显式适应事件） |
|---|---:|---:|---:|---:|
| Efficiency（效率型） | 2 | 0.6667 | 20.4157 | 0 |
| Balance（平衡型） | 3 | 1.0000 | 20.7069 | 0 |
| Exploration（探索型） | 3 | 1.0000 | 16.0590 | 3 |

这些值是本基线的观察事实，不构成策略优越性排序。

## 4. Reproducibility evidence（可复现性证据）

### 4.1 Deterministic replay（确定性重放）

```text
FIXED_SEED=20260725
CSV_DETERMINISTIC_REPLAY=PASS
NORMALIZED_JSON_DETERMINISTIC_REPLAY=PASS
SHA256_VERIFICATION=PASS
```

同一 `run_id`、`seed`、阶段顺序和轮数在独立临时目录重放：

- 四个 CSV（逗号分隔值）日志逐字节一致；
- JSON（结构化结果）去除运行时间戳和存储位置后完全一致；
- 结果对象中的四个 SHA-256 摘要均与对应文件内容匹配。

### 4.2 Frozen evidence artifacts（冻结证据产物）

| Artifact（产物） | SHA-256 |
|---|---|
| `agent_state_log.csv` | `80e62a32af2db5ac3314426b3199f37b793ac3dc438769b9adde4212c63d29b1` |
| `selection_log.csv` | `9118c8a8e903fff4cc54561637ab3bb73ec553b58c5e16ef3da178ebd7945dbc` |
| `phase_log.csv` | `493fefe252654b5fc0094099b16c971f2cdec509c8b7917a0edacf521010748a` |
| `outcome_log.csv` | `6af6991e1f2bd0cd5bfc8e6c63d16b9327af9178ad86bf0133ff4c64fba66063` |

## 5. Interpretation boundary（解释边界）

### This baseline demonstrates（本基线证明）

- the minimal simulator can produce observable selection dynamics
  （最小模拟器能够产生可观察的选择动力学）；
- the workflow and evidence outputs are reproducible under the frozen seed and
  configuration（冻结种子和配置下的工作流及证据输出可复现）；
- one identity-linked state transition can be traced across environment, action,
  selection, and outcome records（一个带身份的状态转换可以跨环境、行为、选择和结果记录
  追溯）。

### This baseline does not demonstrate（本基线不证明）

- DST validation（DST 有效性）；
- digital life or AI consciousness（数字生命或人工智能意识）；
- scientific law discovery（科学规律发现）；
- long-term superiority of any strategy（任何策略的长期优越性）；
- ecological generalization beyond this configuration（超出本配置的生态普遍性）；
- Alpha approval or execution authorization（Alpha 批准或执行授权）。

```text
VALIDATION_PASS_NE_SCIENTIFIC_VALIDATION=true
DRY_RUN_PASS_NE_ALPHA_APPROVAL=true
EVIDENCE_NE_TRUTH=true
```

## 6. Future comparison rules（未来比较规则）

Any future DEB-001 Lite run, validation, dry run, or experiment must declare its
differences from this baseline before interpretation.

任何未来 DEB-001 Lite 运行、验证、试运行或实验，都必须在解释结果前声明相对本基线的
差异。

Required comparison fields（必须比较的字段）：

1. simulator source reference and hash（模拟器来源引用与摘要）；
2. experiment version, run ID, seed, and timestamp（实验版本、运行编号、种子和时间）；
3. population count, identity, lineage, and generation（群体数量、身份、谱系和代数）；
4. initial resources and continuation biases（初始资源和延续偏置）；
5. phase order, duration, and environment multipliers（阶段顺序、时长和环境乘数）；
6. action reward/cost profiles and strategy rules（行为收益／成本配置和策略规则）；
7. scarcity, mismatch, adaptation, and continuation parameters
   （稀缺、错配、适应和延续参数）；
8. log schema, evidence locations, and checksums（日志结构、证据位置和摘要）；
9. selection events, active population changes, and recovery outcomes
   （选择事件、活跃群体变化和恢复结果）；
10. interpretation limits and unresolved risks（解释限制和未解决风险）。

Comparison status vocabulary（比较状态词表）：

- `IDENTICAL_CONFIGURATION`（相同配置）；
- `PARAMETER_VARIANT`（参数变体）；
- `STRATEGY_VARIANT`（策略变体）；
- `ENVIRONMENT_VARIANT`（环境变体）；
- `EVIDENCE_SCHEMA_VARIANT`（证据结构变体）；
- `NOT_COMPARABLE`（不可比较）。

No future run may silently overwrite this baseline. Any changed artifact or parameter
requires a new run identity and an explicit comparison record.

任何未来运行都不得静默覆盖本基线。任何产物或参数变化都必须使用新的运行身份，并建立
明确的比较记录。

## 7. Transition position（转换位置）

```text
Validation-003
    -> Dry Run Workflow PASS
    -> Alpha Decision Review PENDING
    -> Alpha Execution NOT AUTHORIZED
```

The next permitted step is Alpha Decision Review（Alpha 决策评审）, not Alpha
execution.

下一项允许工作是 Alpha 决策评审，而不是 Alpha 执行。
