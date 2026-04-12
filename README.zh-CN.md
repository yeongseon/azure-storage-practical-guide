# Azure Storage 实操指南

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

基于 MS Learn 文档的 Azure Storage 数据访问、持久性、运营和故障排除实操指南。

## 范围

- ✅ 包含: 存储账户、Blob、Files、Queue、Table、冗余、安全、网络、生命周期管理
- ❌ 不包含: Azure Data Lake Analytics、Synapse 深入分析、Cosmos DB

## 主要内容

| 章节 | 目的 |
|---------|---------|
| 从这里开始 (Start Here) | 存储概述、服务选择、学习路径 |
| 平台 (Platform) | Azure Storage 工作原理 — 账户、服务、冗余、访问 |
| 最佳实践 (Best Practices) | 面向生产的存储设计和运营指南 |
| 运营 (Operations) | 分步存储配置和数据管理流程 |
| 故障排除 (Troubleshooting) | 基于症状的存储诊断和解决 |
| 参考 (Reference) | 快速查询选择指南和速查表 |

## 内容来源

所有内容基于官方 [Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/) 文档。

## 本地构建

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build --strict
mkdocs serve
```

## 相关项目

| 仓库 | 描述 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 实操指南 |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 实操指南 |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 实操指南 |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 实操指南 |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 实操指南 |
| [azure-aks-practical-guide](https://github.com/yeongseon/azure-aks-practical-guide) | Azure Kubernetes Service 实操指南 |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 实操指南 |
