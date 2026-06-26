---
title: Cursor Dynamic Menu
emoji: 🎛️
colorFrom: dark-blue
colorTo: purple
sdk: static
pinned: false
---

# 🚀 Hugging Face Spaces용 Cursor 스타일 동적 메뉴

[![Hugging Face Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/deploy-to-spaces-lg.svg)](https://huggingface.co/spaces/bsshin1960/fulldown)

이 저장소는 Hugging Face Spaces의 **Static HTML SDK**를 사용하여 배포되는 정적 웹 서비스 프로젝트입니다.

## 📂 파일 구성 및 업로드 안내
Hugging Face Space를 생성한 후 아래 파일들을 업로드하세요.

1. **`index.html`**: 로컬의 `index_dynamic.html` 파일을 복사하여 `index.html` 이름으로 업로드합니다.
2. **`menu_config.json`**: 로컬의 `menu_config.json` 파일을 그대로 업로드합니다.
3. **`README.md`**: 이 `hf_readme.md` 파일의 내용을 저장소의 `README.md` 파일로 업로드합니다. (상단 YAML 설정 필수)

## ⚙️ 작동 방식
* `index.html`은 동일한 디렉토리에 있는 `menu_config.json`을 브라우저 `fetch`로 동적으로 호출하여 메뉴와 서브메뉴를 실시간으로 빌드합니다.
* 사용자는 별도의 웹 백엔드 서버 없이 브라우저 환경에서 즉시 완전 작동하는 드롭다운 메뉴 런처를 체험할 수 있습니다.
