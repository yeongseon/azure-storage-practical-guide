# Azure Storage 実務ガイド

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

📘 ドキュメントサイト: <https://yeongseon.github.io/azure-storage-practical-guide/>

[![Docs](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/docs.yml)
[![CI](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/validate-content-sources.yml/badge.svg)](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/validate-content-sources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

MS Learn ドキュメントに基づいた Azure Storage の 데이터アクセス、耐久性、運用、およびトラブルシューティングに関する実務ガイドです。

## 主な内容

| セクション | 説明 | ステータス |
|---------|-------------|--------|
| [ここから開始](https://yeongseon.github.io/azure-storage-practical-guide/start-here/) | ストレージの概要、サービス選択ガイド、および一般的な使用シナリオ | Comprehensive |
| [プラットフォーム](https://yeongseon.github.io/azure-storage-practical-guide/platform/) | アカウント、Blob, File, Queue, および Table サービスと冗長性モデルに関する詳細な解説 | Comprehensive |
| [ベストプラクティス](https://yeongseon.github.io/azure-storage-practical-guide/best-practices/) | セキュリティ、ネットワーク、パフォーマンス、およびライフサイクル管理のための本番環境向け設計 | Comprehensive |
| [運用](https://yeongseon.github.io/azure-storage-practical-guide/operations/) | コンテナ、共有、プライベートエンドポイント、およびデータ移動を管理するための運用ガイド | Comprehensive |
| [チュートリアル](https://yeongseon.github.io/azure-storage-practical-guide/tutorials/) | ライフサイクルポリシー、AD 統合、および CDN を使用した静的ウェブサイトのハンズオンラボ | Comprehensive |
| [トラブルシューティング](https://yeongseon.github.io/azure-storage-practical-guide/troubleshooting/) | アクセス拒否、スロットリング、およびレプリケーション遅延の問題に関する診断プレイブック | Published |
| [リファレンス](https://yeongseon.github.io/azure-storage-practical-guide/reference/) | サービス選択、冗長性オプション、およびアクセスチートシートのクイックルックアップ | Comprehensive |

**ステータス凡例**: **Lab-validated** = 包括的かつ再現可能なラボによってガイダンスが証明されている · **Comprehensive** = MSLearn で検証済みの本番環境向けフルセクション · **Published** = コアコンテンツが配置済みで現在拡張中 · **In progress** = 一部のコンテンツが含まれ現在開発中 · **Planned** = プレースホルダーでコンテンツ未着手

## ストレージサービス

Azure Storage サービスの詳細な解説です。
- **Blob Storage**: 非構造化データと静的ウェブサイトのためのスケーラブルなオブジェクトストレージ
- **Azure Files**: AD 統合と SMB/NFS をサポートする管理型ファイル共有
- **Queue Storage**: ワークフロー処理と通信のためのメッセージングストア
- **Table Storage**: 迅速な開発のための NoSQL キー属性ストア
- **冗长性**: データの耐久性のための LRS, ZRS, GRS, および GZRS の実装

## クイックスタート

```bash
git clone https://github.com/yeongseon/azure-storage-practical-guide.git
cd azure-storage-practical-guide

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt

mkdocs serve
```

`http://127.0.0.1:8000` にアクセスしてドキュメントをローカルで閲覧できます。

## 貢献

貢献を歓迎します。以下の事項については、[貢献ガイド](https://yeongseon.github.io/azure-storage-practical-guide/contributing/)を参照してください。

- リポジトリの構造とコンテンツの構成
- ドキュメントテンプレートと執筆標準
- ローカル開発のセットアップとビルド検証
- プルリクエストプロセス

## 関連プロジェクト

| リポジトリ | 説明 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 実務ガイド |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 実務ガイド |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 実務ガイド |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 実務ガイド |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 実務ガイド |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services 実務ガイド |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 実務ガイド |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service 実務ガイド |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture 実務ガイド |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 実務ガイド |

## 免責事項

これは独立したコミュニティプロジェクトです。Microsoft との提携や承認を受けたものではありません。Azure および Azure Storage は Microsoft Corporation の商標です。

## ライセンス

[MIT](LICENSE)
