---
unknown_register_status: initialized-with-examples
unknowns_resolved: 0
automatic_completion_allowed: false
---

# Unknowns（未知事项）

本目录用于显式保留尚未获得充分来源、验证或人工决定的信息。示例包括：

- `clinical validation unavailable`（临床验证不可用）；
- `external validation unavailable`（外部验证不可用）；
- `deployment status unknown`（部署状态未知）。

这些是 Unknown 示例，不是本项目已经执行验证或部署检查后形成的结果。

## Rules（规则）

- Unknown must remain Unknown（未知必须保持未知）；
- Agent 不得根据相似项目、聊天记忆、常识或概率自动补全 Unknown；
- `null`、空值、缺失来源和冲突来源不能被自动解释为肯定或否定；
- 只有带有可定位来源和 Human Approval（人工确认）的新记录才能解决 Unknown；
- 解决 Unknown 应保留原记录、解决依据、决定者、时间和后继状态；
- 无法解决的 Unknown 必须进入 Human Review，不得从输出中省略；
- Unknown 的存在不能被当作失败隐藏，也不能被当作 Permission 拒绝或授予的自动依据。

## Suggested Future Record（建议的未来记录）

未来 Unknown Record（未知记录）至少应包括：`unknown_id`、`statement`、`source_references`、`impact_scope`、`status`、`resolution_reference`、`approved_by`、`introduced_at` 和 `resolved_at`。本文件不创建这些 Record 实例或 Schema。

空记录结构见 [`unknown-record-template.yaml`](unknown-record-template.yaml)。复制模板后仍必须由人类填写独立 ID、陈述、影响和来源；模板本身不是 Unknown Record。

```text
AUTOMATIC_UNKNOWN_COMPLETION=false
UNKNOWN_INFERENCE_ALLOWED=false
UNKNOWN_RECORD_TEMPLATE_DEFINED=true
UNKNOWN_RECORD_INSTANCES=0
```
