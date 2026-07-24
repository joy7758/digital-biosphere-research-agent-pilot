---
reference_registry_status: empty
approved_references: 0
chat_history_sources: 0
---

# Source References（来源引用）

本目录用于未来登记进入 Context Package 的显式来源引用。当前没有已登记或已批准来源。

空记录结构见 [`source-document-template.yaml`](source-document-template.yaml)。该文件只定义字段，不读取来源、不创建 Source Record，也不能加入 `source_documents` 充当真实来源。

## Source Admission（来源准入）

每项未来来源至少应记录：

- 稳定的 `source_reference`；
- Source Type（来源类型）；
- Title / Description（题名或描述）；
- Author / Owner（作者或所有者）；
- Version / Date（版本或日期）；
- Access Constraint（访问限制）；
- Human Review Status（人工复核状态）；
- Known Limitation（已知限制）。

## Source Rules（来源规则）

1. 只有 Human Research Owner 明确选择的来源才能进入 `source_documents`；
2. Chat History（聊天历史）、浏览记录、剪贴板、模型记忆和未声明目录扫描默认不属于来源；
3. 派生摘要必须引用其原始来源，并标明由人类还是工具生成；
4. 版本变化必须创建新引用或新 Package 版本，不得静默覆盖；
5. 来源之间发生冲突时应并列保留并登记 Unknown；
6. `APPROVED` 只批准来源用于特定上下文，不认证来源内容为 Scientific Truth；
7. 受限、私人或敏感来源不得因为能够访问就被自动纳入。

```text
REFERENCES_REGISTERED=0
REFERENCES_APPROVED=0
SOURCE_RECORD_TEMPLATE_DEFINED=true
CHAT_HISTORY_IMPORTED=false
AUTOMATIC_SOURCE_DISCOVERY=false
```
