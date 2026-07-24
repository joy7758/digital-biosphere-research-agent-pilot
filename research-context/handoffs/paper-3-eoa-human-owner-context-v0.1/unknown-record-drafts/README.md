# Unknown Record Drafts v0.1（未知事项记录草案）

本目录把 `unknown-register.yaml` 中的 10 个 Unknown（未知事项）映射为独立、可逐项复核的 Unknown Record Draft（未知事项记录草案）。

```text
Draft != Unknown Record
Candidate Resolution != Human Decision
Human Review != Automatic Resolution
Unknown must remain Unknown
```

每份草案必须保持：

- `record_status: DRAFT_NOT_HUMAN_REVIEWED`；
- `status: OPEN`；
- `truth_value: UNKNOWN`；
- `human_review_decision: PENDING_HUMAN_DECISION`；
- `resolution_reference: null`；
- `approved_by: []`。

Human Research Owner 可以选择 `KEEP_OPEN`、`RESOLVE` 或 `REVISE`。只有明确的人工决定、可定位的 Resolution Reference（解决依据）和时间，才能另建正式 Unknown Record。草案不得原地升级为已解决记录，也不得直接修改 `context-manifest.yaml`。

当前状态：

```text
UNKNOWN_RECORD_DRAFTS=10
UNKNOWN_RECORD_INSTANCES=0
HUMAN_REVIEWED_UNKNOWN_RECORDS=0
AUTOMATIC_UNKNOWN_RESOLUTION=false
```
