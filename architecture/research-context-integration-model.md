---
spec_id: DBRAP-RESEARCH-CONTEXT-INTEGRATION-0.1
status: conceptual-read-only-model
integration_implemented: false
agent_instance_created: false
context_consumed: false
---

# Research Context Integration Model v0.1（研究上下文集成模型 v0.1）

## 1. Purpose（目的）

本模型定义未来 Research Agent 如何只读使用经过人工确认的 Research Context Package。它不是 API、Runtime、Agent 实现或已执行的数据流。

## 2. Required Flow（必要流程）

```text
Human Research Owner
  ↓ selects, reviews, and approves bounded context
Context Package
  ↓ read-only input after separate task authorization
Research Agent
  ↓ produces bounded assistance and reports unknowns
Human Review
```

Human Research Owner 负责选择来源、确认研究决策、保留 Unknown 并批准特定 Package 版本。Research Agent 只能在未来获得独立任务授权后读取 `APPROVED` Package；Package Approval（包批准）本身不是 Agent Authority（智能体权力）。

## 3. Consumption Preconditions（使用前提）

未来 Agent 使用 Package 前至少要确认：

- `context_id` 和 `version` 被任务明确引用；
- `status` 为 `APPROVED`；
- `owner_reference` 与 `approved_by` 不为空且可解释；
- 所有 `source_documents` 均在允许访问范围内；
- Unknown、限制和冲突没有被隐藏；
- 独立的 Capability、Permission、Runtime 和任务授权已经由其各自责任方建立。

任何前提缺失时，Agent 必须停止并向 Human Research Owner 报告，不能自行修复或跳过。

## 4. Read-only Boundary（只读边界）

Research Agent 不能：

- 修改 `context-manifest.yaml`；
- 新增、删除、覆盖或批准 `source_documents`；
- 修改研究决策的 statement、status 或 approver；
- 把 Unknown 自动改为已知；
- 把自己的输出写回 Package 并标为 Human Approved Context；
- 把 Package `APPROVED` 解释为 Capability、Permission、Execution 或 Scientific Truth。

Agent 发现问题时只能输出：

- Context Conflict Report（上下文冲突报告）；
- Missing Source Report（缺失来源报告）；
- Unknown Report（未知报告）；
- Change Request（变更请求）。

这些输出仍需 Human Review，不能自动修改 Package。

## 5. Version and Handoff（版本与交接）

```text
Approved Context Package vN
  -> bounded Agent assistance
  -> Human Review
  -> optional human-authored change decision
  -> new Draft Context Package vN+1
```

已批准版本保持不可变。Human Research Owner 可以基于复核结果创建新 `DRAFT`，再经过 `REVIEWED` 和 `APPROVED`；不允许 Agent 原地演化 Context。

在未来另行实施和授权后，Agent 的执行与输出材料可以形成 DBOS Evidence Reference，受控记录可以进入 SAEE Evaluation。Context Package 本身不创建 DBOS Evidence，也不触发 SAEE。

## 6. Current Status（当前状态）

```text
RESEARCH_CONTEXT_INTEGRATION_MODEL_DEFINED=true
CONTEXT_PACKAGE_CONSUMED=false
AGENT_WRITE_ACCESS_TO_CONTEXT=false
DBOS_EVIDENCE_CREATED=false
SAEE_EVALUATION_TRIGGERED=false
Agent=0
Runtime=0
Entity=0
Permission=0
Execution=0
Research Result=0
```
