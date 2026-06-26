---
title: Cursor Dynamic Menu
emoji: 🎛️
colorFrom: blue
colorTo: purple
sdk: static
pinned: false
---

# 🎛️ Cursor Style Pulldown Menu Launcher

[![Hugging Face Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/deploy-to-spaces-lg.svg)](https://huggingface.co/spaces/bsshin/fulldown1)

이 프로젝트는 **Cursor IDE 스타일의 드롭다운 메뉴**를 웹(HTML/JS)과 데스크톱 애플리케이션(PyQt6, Tkinter) 환경 모두에서 동일하게 체험하고 사용할 수 있도록 제작된 메뉴 런처 프로젝트입니다.

---

## 📂 주요 파일 구성 및 역할

### 🌐 웹 애플리케이션 (Web Application)
* **index.html**: 하드코딩된 정적 형태의 Cursor 스타일 웹 메뉴판 페이지입니다.
* **index_dynamic.html**: 동일 디렉토리의 `menu_config.json`을 읽어와서 메뉴바 및 드롭다운/서브메뉴를 동적으로 생성하는 동적 웹 메뉴판 페이지입니다.
* **menu_config.json**: 메뉴의 구조, 단축키, 서브메뉴 트리, 비활성화 여부를 정의하는 공통 설정 파일입니다.
* **run_local_webserver.bat**: 파이썬의 임시 내장 웹서버(`http.server`)를 8000 포트로 띄워 브라우저로 웹 메뉴판을 바로 여는 배치 파일입니다.

### 💻 데스크톱 애플리케이션 (Desktop Application)
* **menu_pyqt6.py**: PyQt6를 사용하여 네이티브 스타일로 빌드한 글로벌 드롭다운 메뉴 런처(정적 버전)입니다.
* **menu_pyqt6_dynamic.py**: `menu_config.json`을 동적으로 파싱하여 GUI 메뉴를 빌드하는 PyQt6 메뉴 런처입니다.
* **menu_tkinter.py**: 의존성을 줄이고 파이썬 내장 라이브러리인 Tkinter를 활용하여 빌드한 메뉴 런처입니다.
* **convert_icon.py**: 앱 아이콘을 다양한 규격으로 변환해주는 파이썬 헬퍼 스크립트입니다.
* **build_global_menu.bat**: PyInstaller를 통해 파이썬 스크립트를 단독 실행 파일(`.exe`)로 패키징하는 배치 파일입니다.

---

## 🚀 사용법 및 실행 안내

### 1. 로컬 웹 서버로 HTML 실행하기
브라우저 환경에서 동적으로 JSON 설정을 로드하려면 로컬 웹 서버가 필요합니다.
1. `run_local_webserver.bat` 또는 `실행_HTML메뉴.bat`을 실행합니다.
2. 웹 브라우저를 열고 `http://localhost:8000/index_dynamic.html`로 접속합니다.

### 2. 데스크톱 앱 실행하기 (Python)
파이썬 환경이 설치되어 있는 경우 다음과 같이 스크립트를 직접 실행할 수 있습니다.
```bash
# PyQt6 의존성 설치 (PyQt6 버전 실행 시 필요)
pip install PyQt6

# PyQt6 동적 메뉴 실행
python menu_pyqt6_dynamic.py

# Tkinter 메뉴 실행
python menu_tkinter.py
