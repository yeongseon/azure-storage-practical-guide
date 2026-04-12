# Azure Storage 実務ガイド

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

MS Learn ドキュメントに基づいた、Azure Storage のデータアクセス、耐久性、運用、およびトラブルシューティングに関する実務ガイドです。

## スコープ

- ✅ 含まれるもの: ストレージアカウント、Blob、Files、Queue、Table、冗長性、セキュリティ、ネットワーク、ライフサイクル管理
- ❌ 含まれないもの: Azure Data Lake Analytics、Synapse の詳細分析、Cosmos DB

## 主な内容

| セクション | 目的 |
|---------|---------|
| ここから開始 (Start Here) | ストレージ概要、サービス選択、学習パス |
| プラットフォーム (Platform) | Azure Storage の仕組み — アカウント、サービス、冗長性、アクセス |
| ベストプラクティス (Best Practices) | 本番環境に対応したストレージ設計と運用ガイドライン |
| 運用 (Operations) | ステップバイステップのストレージ構成とデータ管理手順 |
| トラブルシューティング (Troubleshooting) | 症状ベースのストレージ診断と解決 |
| リファレンス (Reference) | クイックルックアップ選択ガイドとチートシート |

## コンテンツソース

すべてのコンテンツは、公式 [Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/) ドキュメントに基づいています。

## ローカルビルド

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build --strict
mkdocs serve
```

## 関連プロジェクト

| リポジトリ | 説明 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 実務ガイド |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 実務ガイド |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 実務ガイド |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 実務ガイド |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 実務ガイド |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service 実務ガイド |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 実務ガイド |
