# SDK/Adapter Guide（SDK/适配器接入说明）

## Design Philosophy（设计理念）
TITMAS 的 SDK（软件开发工具包）和 Adapter（适配器）采用 **Reference-oriented（面向引用）** 设计。这意味着客户端代码操作的是状态、标识符和引用的快照，而不是直接操作底层的可信数据库。

## Core Components（核心组件）
1. **Context Reader（上下文读取器）**：
   提供对 Research Context Package（研究上下文包）的只读访问。
2. **Evidence Submitter（证据提交器）**：
   按照 Data Contract（数据契约）封装观测到的 Execution（执行）状态，然后提交到记录队列。
3. **Identity Manager（身份管理器）**：
   处理 Owner Reference（所有者引用）与 Runtime（运行时）之间的授权绑定。

## Best Practices（最佳实践）
- **Do not cache mutable state（不要缓存可变状态）**。
- **Always handle Validation Failures（始终处理验证失败）**，因为 Evidence（证据）在被证实为合规之前属于不可信状态。
- **Ensure traceability（确保可追溯性）**：每一次调用都应携带唯一的 Trace ID（追踪标识）。
