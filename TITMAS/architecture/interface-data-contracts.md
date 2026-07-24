# Interface & Data Contract Specification（接口与数据契约规范）

## Overview（概述）
在 TITMAS 架构中，系统组件、Agent（智能体）以及开发者工具之间的通信必须严格遵循 Interface（接口）与 Data Contract（数据契约）。

## Contract Guidelines（契约准则）
- **Explicit Schema（显式模式）**：所有交互数据必须有明确的 Schema 定义，无论是 JSON、YAML 还是其他结构化数据。
- **Immutable References（不可变引用）**：对于已验证的 Evidence（证据）和 Context（上下文），其引用必须是不可变的（通常带有 Hash 校验）。
- **Role-Based Contracts（基于角色的契约）**：不同角色的接口调用（如 Reviewer 接口与 Owner 接口）应有明确的契约分离。

## Interface Boundaries（接口边界）
- **DBOS Interfaces（DBOS 接口）**：仅限于身份和证据的注册与检索，不包含业务逻辑评估。
- **SAEE Interfaces（SAEE 接口）**：基于标准 Contract（契约）接收证据记录，并返回标准格式的 Evaluation（评价）。
- **Agent Interfaces（智能体接口）**：Agent（智能体）只能通过标准契约访问 Research Context Package（研究上下文包），且默认为 Read-Only（只读）模式。
