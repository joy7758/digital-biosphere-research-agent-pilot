# Initial Access Tokens Registry Draft（初始试用凭证注册表草案）

## Context（上下文）
此凭证草案用于 TITMAS（可信多智能体基础设施标准社区）商业试点的第一阶段。由于当前原型和验证环境还未完全通过审批闸门，此清单记录均为 `PENDING_APPROVAL`（等待审批）状态，不可用于生产。

## Token Inventory（凭证清单）

```yaml
tokens:
  - token_id: TOKEN-TRIAL-001
    assigned_role: OBSERVER
    developer_reference: dev-external-alpha
    permissions:
      - READ_ONLY_CONTEXT
      - SUBMIT_TRIAL_EVIDENCE
    status: PENDING_APPROVAL
    issued_at: null
    expires_at: null

  - token_id: TOKEN-TRIAL-002
    assigned_role: INDEPENDENT_REVIEWER
    developer_reference: dev-external-auditor
    permissions:
      - READ_ONLY_CONTEXT
      - READ_ALL_EVIDENCE
      - SUBMIT_REVIEW_DECISION
    status: PENDING_APPROVAL
    issued_at: null
    expires_at: null
```

## Security Rule（安全规则）
- 不得在 `PROTOTYPE_AUTHORIZED=false` 时激活任何 Token（凭证）。
- 凭证信息严禁存储在明文代码库中，此清单仅为身份模型草案。
