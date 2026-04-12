# Azure Storage 실무 가이드

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

MS Learn 문서를 기반으로 한 Azure Storage 데이터 접근, 내구성, 운영 및 트러블슈팅을 다루는 실무 가이드입니다.

## 범위

- ✅ 포함: 스토리지 계정, Blob, Files, Queue, Table, 중복성, 보안, 네트워킹, 수명 주기 관리
- ❌ 제외: Azure Data Lake Analytics, Synapse 심화 분석, Cosmos DB

## 주요 내용

| 섹션 | 목적 |
|---------|---------|
| 시작하기 (Start Here) | 스토리지 개요, 서비스 선택, 학습 경로 |
| 플랫폼 (Platform) | Azure Storage 작동 원리 — 계정, 서비스, 중복성, 접근 |
| 베스트 프랙티스 (Best Practices) | 운영 환경에 적합한 스토리지 설계 및 운영 가이드라인 |
| 운영 (Operations) | 단계별 스토리지 구성 및 데이터 관리 절차 |
| 트러블슈팅 (Troubleshooting) | 증상 기반 스토리지 진단 및 해결 |
| 참조 (Reference) | 빠른 조회 선택 가이드 및 치트시트 |

## 콘텐츠 소스

모든 콘텐츠는 공식 [Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/) 문서를 기반으로 합니다.

## 로컬 빌드

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build --strict
mkdocs serve
```

## 관련 프로젝트

| 저장소 | 설명 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 실무 가이드 |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 실무 가이드 |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 실무 가이드 |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 실무 가이드 |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 실무 가이드 |
| [azure-aks-practical-guide](https://github.com/yeongseon/azure-aks-practical-guide) | Azure Kubernetes Service 실무 가이드 |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 실무 가이드 |
