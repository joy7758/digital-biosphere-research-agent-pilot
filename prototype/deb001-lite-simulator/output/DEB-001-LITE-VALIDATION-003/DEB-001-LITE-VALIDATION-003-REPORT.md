# DEB-001 Lite Validation-003 Report（DEB-001 Lite 第三次验证报告）

## Result boundary（结果边界）

```text
VALIDATION_ID=DEB-001-LITE-VALIDATION-003
VALIDATION_STATUS=PASS
RECORD_CLASS=LOCAL_WORKFLOW_VALIDATION_ONLY
DST_VALIDATED=false
SCIENTIFIC_LAW_DISCOVERED=false
ALPHA_APPROVED=false
RUNTIME_AUTHORITY_GRANTED=false
```

`PASS`（通过）只表示本次最小修正满足预先给定的工程判据：出现延续差异、至少一个
selection/dropout event（选择／退出事件），并保持确定性重放。它不是 Digital
Survival Theory（数字生存理论）验证、科学规律发现或 Alpha（首轮真实实验）批准。

## 1. Changes from Validation-002（相对第二次验证的变化）

Validation-003（第三次验证）保持原有单文件规则模拟器、9 个个体和
Stable -> Shock -> Recovery（稳定 -> 冲击 -> 恢复）三阶段结构，仅进行了以下最小
修改：

1. Shock（冲击）环境乘数从温和区间调整为资源稀缺区间，并增加统一的冲击期稀缺成本；
2. Efficiency（效率型）提高稳定期短期收益，同时增加冲击期错配惩罚；
3. Balance（平衡型）保留中等收益和交替探索行为；
4. Exploration（探索型）降低早期效率，并通过探索／适应动作更快积累
   adaptation level（适应水平）；
5. `continuation_score`（延续分数）现在同时包含资源状态、阶段适应、当前策略行为和
   对三个成员对称的固定微小偏置；
6. `lineage_id`（谱系编号）、`strategy_origin`（策略来源）、`generation`（代数）和
   `state_transition`（状态转换）写入 `agent_state_log`、`selection_log` 和
   `outcome_log`；
7. 四个 CSV（逗号分隔值）证据文件计算 SHA-256（安全哈希算法）摘要，并写入最小
   JSON（结构化结果）对象。

没有新增 LLM agent（大语言模型智能体）、Web UI（网页界面）、API（应用程序接口）、
数据库、治理基础设施或完整 DEB（Digital Ecology Box，数字生态箱）框架。

## 2. Reproducibility result（可复现性结果）

### Run identity（运行身份）

- `run_id`: `DEB-001-LITE-VALIDATION-003`
- `experiment_id`: `DEB-001-LITE`
- `version`: `v0.1`
- `seed`: `20260725`
- phase rounds（阶段轮数）: `Stable=3`, `Shock=2`, `Recovery=2`
- total rounds（总轮数）: `7`

### Replay verification（重放验证）

```text
SAME_SEED_REPLAY=MATCH
CSV_BYTE_COMPARISON=PASS
NORMALIZED_JSON_COMPARISON=PASS
EMBEDDED_CHECKSUM_VERIFICATION=PASS
```

同一 `run_id`、`seed` 和阶段轮数在独立临时目录重放：

- `agent_state_log.csv`：逐字节一致；
- `selection_log.csv`：逐字节一致；
- `phase_log.csv`：逐字节一致；
- `outcome_log.csv`：逐字节一致；
- JSON 结果去除运行时间戳和存储位置后完全一致；
- normalized result SHA-256（标准化结果摘要）：
  `efa0c2b0b0ea28dbd6dd75d6c1243e6d4d8a3e2deda047586705483d4e6a3bb8`。

### Evidence checksums（证据摘要）

| Evidence artifact（证据产物） | SHA-256 |
|---|---|
| `agent_state_log.csv` | `80e62a32af2db5ac3314426b3199f37b793ac3dc438769b9adde4212c63d29b1` |
| `selection_log.csv` | `9118c8a8e903fff4cc54561637ab3bb73ec553b58c5e16ef3da178ebd7945dbc` |
| `phase_log.csv` | `493fefe252654b5fc0094099b16c971f2cdec509c8b7917a0edacf521010748a` |
| `outcome_log.csv` | `6af6991e1f2bd0cd5bfc8e6c63d16b9327af9178ad86bf0133ff4c64fba66063` |

## 3. Selection events observed（观察到的选择事件）

Stable（稳定）阶段结束时，9 个个体全部保持活跃。

Shock（冲击）阶段第 4 轮发生一个退出事件：

| Field（字段） | Value（值） |
|---|---|
| `agent_id` | `EFFI1` |
| `lineage_id` | `EFF-lineage-1` |
| `strategy_origin` | `Efficiency` |
| `generation` | `0` |
| `state_transition` | `ACTIVE->DROPPED` |
| `continuation_score` | `0.3047` |
| `continuation_threshold` | `0.3500` |
| reason（原因） | 冲击期延续分数低于阈值，且效率型策略未及时适应环境变化 |

阶段活跃个体变化：

| Phase（阶段） | Active start（开始活跃数） | Active end（结束活跃数） | Delta（变化） |
|---|---:|---:|---:|
| Stable（稳定） | 9 | 9 | 0 |
| Shock（冲击） | 9 | 8 | -1 |
| Recovery（恢复） | 8 | 8 | 0 |

这说明模拟器可以产生资源压力、延续差异和可定位的状态转换。单个退出事件本身不能证明
任何策略具有一般性优势。

## 4. Strategy outcome comparison（策略结果比较）

| Strategy（策略） | Final active（最终活跃数） | Continuation rate（延续率） | Final average resource（最终平均资源） | Adaptation events（适应事件） |
|---|---:|---:|---:|---:|
| Efficiency（效率型） | 2 | 0.6667 | 20.4157 | 0 |
| Balance（平衡型） | 3 | 1.0000 | 20.7069 | 0 |
| Exploration（探索型） | 3 | 1.0000 | 16.0590 | 3 |

Observed differentiation（观察到的差异）：

- Efficiency（效率型）在 Stable（稳定）阶段获得最高资源，但在 Shock（冲击）阶段
  出现一个退出；
- Balance（平衡型）最终平均资源最高，并保持三个个体活跃；
- Exploration（探索型）最终资源较低，但记录到三个显式适应事件并全部存续；
- Recovery（恢复）阶段没有新的退出，三类策略呈现不同资源恢复轨迹。

这些结果只描述固定参数和固定种子下的一次本地运行，不支持“Balance 最优”
（平衡策略最优）或其他排序结论。

## 5. Success criteria evaluation（成功判据评估）

| Criterion（判据） | Result（结果） |
|---|---|
| 至少一个 continuation difference（延续差异） | `PASS`：效率型延续率为 `0.6667`，其余两类为 `1.0` |
| 至少一个 selection/dropout event（选择／退出事件） | `PASS`：`EFFI1` 在 Shock 第 4 轮退出 |
| deterministic replay（确定性重放） | `PASS`：CSV 逐字节一致，标准化 JSON 一致 |
| evidence checksum consistency（证据摘要一致性） | `PASS`：四个嵌入摘要均与文件内容一致 |

```text
VALIDATION_STATUS=PASS
```

## 6. Remaining limitations（剩余限制）

- 样本仅包含 9 个个体和 7 轮；
- 主要结果只来自一个固定种子，尚未形成预注册的多种子比较；
- 三个同策略成员之间的微小延续偏置是固定且对称的实验参数，仍会影响具体退出身份；
- 当前资源仍按个体余额计算，不是已冻结的共享资源池；
- 退出是不可逆的，Recovery（恢复）阶段不支持重新进入；
- SHA-256 摘要覆盖四个 CSV 证据文件；JSON 结果自身使用外部标准化摘要验证；
- 当前运行没有独立科学复核、统计推断或外部重复实验；
- `PASS` 不建立 DST（Digital Survival Theory，数字生存理论）有效性；
- `PASS` 不批准 Alpha 执行、生产部署、治理权力或运行权限。

## 7. Output references（输出引用）

- `agent_state_log.csv`
- `selection_log.csv`
- `phase_log.csv`
- `outcome_log.csv`
- `DEB-001-LITE-MINIMAL-RESULT-v0.1.json`

All outputs are local validation artifacts only.

所有输出仅为本地验证产物。
