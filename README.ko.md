# Azure Storage 실무 가이드

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

📘 문서 사이트: <https://yeongseon.github.io/azure-storage-practical-guide/>

[![Docs](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/docs.yml)
[![CI](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/validate-content-sources.yml/badge.svg)](https://github.com/yeongseon/azure-storage-practical-guide/actions/workflows/validate-content-sources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

MS Learn 문서를 기반으로 Azure Storage 데이터 접근, 내구성, 운영 및 트러블슈팅을 다루는 실무 가이드입니다.

## 주요 내용

| 섹션 | 설명 | 상태 |
|---------|-------------|--------|
| [시작하기](https://yeongseon.github.io/azure-storage-practical-guide/start-here/) | 스토리지 개요, 서비스 선택 가이드 및 공통 사용 시나리오 | Comprehensive |
| [플랫폼](https://yeongseon.github.io/azure-storage-practical-guide/platform/) | 계정, Blob, File, Queue, Table 서비스와 중복성 모델에 대한 심층 분석 | Comprehensive |
| [베스트 프랙티스](https://yeongseon.github.io/azure-storage-practical-guide/best-practices/) | 보안, 네트워킹, 성능 및 수명 주기 관리를 위한 운영 환경용 설계 | Comprehensive |
| [운영](https://yeongseon.github.io/azure-storage-practical-guide/operations/) | 컨테이너, 공유, 프라이빗 엔드포인트 및 데이터 이동 관리를 위한 운영 가이드 | Comprehensive |
| [튜토리얼](https://yeongseon.github.io/azure-storage-practical-guide/tutorials/) | 수명 주기 정책, AD 통합 및 CDN을 사용한 정적 웹 사이트 실습 | Comprehensive |
| [트러블슈팅](https://yeongseon.github.io/azure-storage-practical-guide/troubleshooting/) | 접근 거부, 스로틀링 및 복제 지연 문제에 대한 진단 플레이북 | Published |
| [참조](https://yeongseon.github.io/azure-storage-practical-guide/reference/) | 서비스 선택, 중복성 옵션 및 접근 치트시트 빠른 조회 | Comprehensive |

**상태 범례**: **Lab-validated** = 가이드를 증명하는 종합적이고 재현 가능한 실습 포함 · **Comprehensive** = MSLearn 검증이 완료된 운영 환경용 전체 섹션 · **Published** = 핵심 콘텐츠 포함 및 확장 중 · **In progress** = 일부 콘텐츠 포함 및 활발히 개발 중 · **Planned** = 콘텐츠 시작 전인 플레이스홀더

## 스토리지 서비스

Azure Storage 서비스에 대한 상세 내용입니다.
- **Blob Storage**: 비정형 데이터 및 정적 웹 사이트를 위한 확장 가능한 객체 스토리지
- **Azure Files**: AD 통합 및 SMB/NFS를 지원하는 관리형 파일 공유
- **Queue Storage**: 워크플로 처리 및 통신을 위한 메시징 저장소
- **Table Storage**: 빠른 개발을 위한 NoSQL 키-속성 저장소
- **중복성**: 데이터 내구성을 위한 LRS, ZRS, GRS 및 GZRS 구현

## 빠른 시작

```bash
git clone https://github.com/yeongseon/azure-storage-practical-guide.git
cd azure-storage-practical-guide

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt

mkdocs serve
```

`http://127.0.0.1:8000`에 접속하여 로컬에서 문서를 확인할 수 있습니다.

## 기여하기

기여를 환영합니다. 다음 사항은 [기여 가이드](https://yeongseon.github.io/azure-storage-practical-guide/contributing/)를 참조해 주세요.

- 저장소 구조 및 콘텐츠 구성
- 문서 템플릿 및 작성 표준
- 로컬 개발 설정 및 빌드 검증
- 풀 리퀘스트 프로세스

## 관련 프로젝트

| 저장소 | 설명 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 실무 가이드 |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 실무 가이드 |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 실무 가이드 |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 실무 가이드 |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 실무 가이드 |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services 실무 가이드 |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 실무 가이드 |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service 실무 가이드 |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture 실무 가이드 |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 실무 가이드 |

## 면책 조항

이 프로젝트는 독립적인 커뮤니티 프로젝트입니다. Microsoft와 관련이 없으며 Microsoft의 승인을 받지 않았습니다. Azure 및 Azure Storage는 Microsoft Corporation의 상표입니다.

## 라이선스

[MIT](LICENSE)
