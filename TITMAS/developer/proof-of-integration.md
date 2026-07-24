# Proof-of-Integration（集成证明）

## Purpose（目的）
Proof-of-Integration (PoI，集成证明) 是 TITMAS 社区中验证一个外部系统、Agent（智能体）或工具是否正确、安全地接入可信架构的关键标准。

## Requirements（要求）
- **Interface Conformance（接口合规）**：
  必须证明接入方完全遵守了 Interface & Data Contract（接口与数据契约）。
- **Traceability（可追溯性）**：
  所有与基础设施交互的操作，必须产生可追溯的 Evidence Reference（证据引用）。
- **Boundary Respect（边界尊重）**：
  禁止未授权的写操作，严禁在没有 Human Authorization（人工授权）的情况下覆盖 DBOS/SAEE 中的状态。

## Artifacts（交付物）
进行集成验证时，开发者需要提交：
1. Integration Test Record（集成测试记录）；
2. Validated Evidence Package（验证通过的证据包）；
3. Code/Adapter Manifest（代码/适配器清单），指明遵守的协议版本。
