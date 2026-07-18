# Azure Storage 实操指南

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

📘 文档站点: <https://yeongseon.github.io/azure-storage-practical-guide/>

[![Docs](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/docs.yml)
[![CI](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/validate-content-sources.yml/badge.svg)](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/validate-content-sources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

基于 MS Learn 文档的 Azure Storage 数据访问、持久性、运营和故障排除实操指南。

## 主要内容

| 章节 | 说明 | 状态 |
|---------|-------------|--------|
| [从这里开始](https://yeongseon.github.io/azure-storage-practical-guide/start-here/) | 存储概述、服务选择指南和常见使用场景 | Comprehensive |
| [平台](https://yeongseon.github.io/azure-storage-practical-guide/platform/) | 深入分析账户、Blob、File、Queue 和 Table 服务及其冗余模型 | Comprehensive |
| [最佳实践](https://yeongseon.github.io/azure-storage-practical-guide/best-practices/) | 面向生产环境的安全性、网络、性能和生命周期管理设计 | Comprehensive |
| [运营](https://yeongseon.github.io/azure-storage-practical-guide/operations/) | 管理容器、共享、专用端点和数据移动的运营指南 | Comprehensive |
| [教程](https://yeongseon.github.io/azure-storage-practical-guide/tutorials/) | 生命周期策略、AD 集成以及使用 CDN 的静态网站实操实验室 | Comprehensive |
| [故障排除](https://yeongseon.github.io/azure-storage-practical-guide/troubleshooting/) | 针对访问被拒绝、限制和复制延迟问题的诊断手册 | Published |
| [参考](https://yeongseon.github.io/azure-storage-practical-guide/reference/) | 服务选择、冗余选项和访问速查表的快速查询 | Comprehensive |

**状态说明**: **Lab-validated** = 包含证明指南的全面且可重复的实验室 · **Comprehensive** = 经过 MSLearn 验证的完整生产级章节 · **Published** = 核心内容已就绪，仍持续扩展中 · **In progress** = 包含部分内容，正在积极开发中 · **Planned** = 占位符，内容尚未开始

## 存储服务

Azure Storage 服务产品详细介绍：
- **Blob Storage**: 用于非结构化数据和静态网站的可扩展对象存储
- **Azure Files**: 支持 AD 集成和 SMB/NFS 的托管文件共享
- **Queue Storage**: 用于工作流处理和通信的消息传递存储
- **Table Storage**: 用于快速开发的 NoSQL 键-属性存储
- **冗余**: 用于数据持久性的 LRS、ZRS、GRS 和 GZRS 实现

## 快速开始

```bash
git clone https://github.com/yeongseon/azure-storage-practical-guide.git
cd azure-storage-practical-guide

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt

mkdocs serve
```

访问 `http://127.0.0.1:8000` 在本地浏览文档。

## 贡献

欢迎贡献！有关以下内容，请参阅我们的[贡献指南](https://yeongseon.github.io/azure-storage-practical-guide/contributing/)：

- 仓库结构和内容组织
- 文档模板和编写标准
- 本地开发设置和构建验证
- 拉取请求流程

## 相关项目

| 仓库 | 描述 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 实操指南 |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 实操指南 |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 实操指南 |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 实操指南 |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 实操指南 |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services 实操指南 |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 实操指南 |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service 实操指南 |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture 实操指南 |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 实操指南 |

## 免责声明

这是一个独立的社区项目。与 Microsoft 无关，也不受其认可。Azure 和 Azure Storage 是 Microsoft Corporation 的商标。

## 许可证

[MIT](LICENSE)
