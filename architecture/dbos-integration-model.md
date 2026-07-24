---
spec_id: DBRAP-DBOS-INTEGRATION-0.1
status: conceptual-reference-only
dbos_modified: false
integration_implemented: false
---

# DBOS Integration Model v0.1（DBOS 集成模型 v0.1）

## 1. Scope（范围）

DBOS 在未来 Pilot 中只提供以下 canonical references（规范引用）：

- Identity Reference（身份引用）；
- Execution Reference（执行引用）；
- Evidence Reference（证据引用）；
- Verification Reference（验证引用）。

本文件没有定义 endpoint（端点）、SDK（软件开发工具包）、Schema（模式）或写入机制，也没有调用或修改 DBOS。

## 2. Reference Responsibilities（引用职责）

| DBOS Reference | Pilot 的未来用途 | 不表示 |
|---|---|---|
| Identity Reference | 引用被治理参与对象的稳定身份记录 | 当前已创建 Agent、Digital Entity、Owner 或 Permission |
| Execution Reference | 引用一次受治理过程的范围、版本和状态记录 | DBOS 执行科研任务或过程成功 |
| Evidence Reference | 引用输入、过程、输出、失败和复核材料 | Evidence 为真、完整或支持科学结论 |
| Verification Reference | 引用验证主体、范围、方法和结果 | 科学有效、发表批准、Permission 或 SAEE 评价 |

```text
REFERENCE_NE_OBJECT_INSTANCE=true
REFERENCE_NE_PERMISSION=true
EXECUTION_REFERENCE_NE_EXECUTION_ENGINE=true
EVIDENCE_REFERENCE_NE_SCIENTIFIC_TRUTH=true
VERIFICATION_REFERENCE_NE_SCIENTIFIC_VALIDATION=true
```

## 3. Conceptual Exchange（概念性交接）

```text
Research task context
  -> Identity Reference
  -> Execution Reference
  -> Evidence Reference
  -> Verification Reference
  -> bounded input for Human Review and SAEE Evaluation
```

任何 unresolved（未解析）、missing（缺失）、ambiguous（歧义）或 invalid（无效）引用必须保持原状态，不得由 Pilot 猜测、补写或升级。

## 4. DBOS Non-responsibilities（DBOS 非职责）

DBOS 不：

- 控制或形成研究结论；
- 替代科学判断、领域复核或伦理审查；
- 作为 Research Agent Runtime（科研智能体运行时）；
- 把 Identity、Evidence 或 Verification 自动转换为 Capability 或 Permission；
- 执行 SAEE Recommendation（SAEE 建议）；
- 决定论文作者、投稿或发表。

## 5. Ownership Boundary（所有权边界）

- DBA 定义上位架构规则；
- DBOS 拥有其规范身份、生命周期、执行、证据和验证记录；
- Pilot 只消费明确允许的引用，不复制或建立竞争性事实真源；
- Pilot 不回写 DBA、DBOS 或 SAEE；未来若需要写入，必须另行定义契约并获得人类授权。

## 6. Current Status（当前状态）

```text
DBOS_CONNECTION_STATUS=PREPARED_ONLY
DBOS_REFERENCE_MODEL_DEFINED=true
DBOS_API_CALLED=false
DBOS_RECORD_READ=false
DBOS_RECORD_WRITTEN=false
DBOS_MODIFIED=false
IDENTITY_REFERENCE_RESOLVED=false
EXECUTION_REFERENCE_RESOLVED=false
EVIDENCE_REFERENCE_RESOLVED=false
VERIFICATION_REFERENCE_RESOLVED=false
INTEGRATION_IMPLEMENTED=false
```

`PREPARED_ONLY` 表示本项目已经为 Future DBOS References（未来 DBOS 引用）保留 Identity、Execution、Evidence 和 Verification 四类语义位置；它不表示引用已创建、解析、读取、写入或验证。DBOS 仓库没有被本项目修改。
