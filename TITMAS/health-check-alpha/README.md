# TITMAS Health Check Alpha MVP

## Overview（概述）
The TITMAS Health Check Alpha MVP provides a minimal verifiable execution certificate pipeline. It demonstrates how external developer events can be admitted, validated structurally, and issued a non-authoritative machine-readable certificate.
（TITMAS 健壮性检查 Alpha MVP 提供了一条最小的可验证执行证书管线。它演示了外部开发者的事件如何被接入、结构验证，以及如何颁发非权威的机器可读证书。）

## Scope & Constraints（范围与约束）

**Must Preserve（必须保留的核心原则）**:
- Evidence is not Truth（证据不是事实）.
- Verification is not Authorization（验证不是授权）.
- Certificate proves execution evidence only（证书仅证明执行证据存在）.
- No security certification claims（无安全认证声明）.
- No compliance certification claims（无合规认证声明）.
- No SAEE core implementation included（不包含 SAEE 核心实现）.

**Out of Scope（超出范围 / 绝对禁止）**:
- Do not build SaaS（不构建 SaaS）.
- Do not build a dashboard（不构建仪表盘）.
- Do not add authentication（不添加身份验证逻辑）.
- Do not add billing（不添加计费）.
- Do not create community features（不创建社区功能）.

## How to Run the Example（如何运行示例）
```bash
python3 example.py
```
This will produce a `validation-report-example.json` containing the verifiable execution certificate.
（此操作将产生一个包含可验证执行证书的 validation-report-example.json 文件。）
