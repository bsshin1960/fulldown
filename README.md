# 🎛️ Cursor Style Pulldown Menu Launcher

[![Hugging Face Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/deploy-to-spaces-lg.svg)](https://huggingface.co/spaces/bsshin1960/fulldown)

이 프로젝트는 **Cursor IDE 스타일의 드롭다운 메뉴**를 웹(HTML/JS)과 데스크톱 애플리케이션(PyQt6, Tkinter) 환경 모두에서 동일하게 체험하고 사용할 수 있도록 제작된 메뉴 런처 프로젝트입니다.

---

## 📂 주요 파일 구성 및 역할

### 🌐 웹 애플리케이션 (Web Application)
* **[`index.html`](index.html)**: 하드코딩된 정적 형태의 Cursor 스타일 웹 메뉴판 페이지입니다.
* **[`index_dynamic.html`](index_dynamic.html)**: 동일 디렉토리의 `menu_config.json`을 읽어와서 메뉴바 및 드롭다운/서브메뉴를 동적으로 생성하는 동적 웹 메뉴판 페이지입니다.
* **[`menu_config.json`](menu_config.json)**: 메뉴의 구조, 단축키, 서브메뉴 트리, 비활성화 여부를 정의하는 공통 설정 파일입니다.
* **[`run_local_webserver.bat`](run_local_webserver.bat)**: 파이썬의 임시 내장 웹서버(`http.server`)를 8000 포트로 띄워 브라우저로 웹 메뉴판을 바로 여는 배치 파일입니다.

### 💻 데스크톱 애플리케이션 (Desktop Application)
* **[`menu_pyqt6.py`](menu_pyqt6.py)**: PyQt6를 사용하여 네이티브 스타일로 빌드한 글로벌 드롭다운 메뉴 런처(정적 버전)입니다.
* **[`menu_pyqt6_dynamic.py`](menu_pyqt6_dynamic.py)**: `menu_config.json`을 동적으로 파싱하여 GUI 메뉴를 빌드하는 PyQt6 메뉴 런처입니다.
* **[`menu_tkinter.py`](menu_tkinter.py)**: 의존성을 줄이고 파이썬 내장 라이브러리인 Tkinter를 활용하여 빌드한 메뉴 런처입니다.
* **[`convert_icon.py`](convert_icon.py)**: 앱 아이콘을 다양한 규격으로 변환해주는 파이썬 헬퍼 스크립트입니다.
* **[`build_global_menu.bat`](build_global_menu.bat)**: PyInstaller를 통해 파이썬 스크립트를 단독 실행 파일(`.exe`)로 패키징하는 배치 파일입니다.

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
```

---

## ☁️ GitHub Pages를 통한 무료 웹 호스팅 (URL 실행)

이 프로젝트는 정적 파일로만 구성되어 있어 **GitHub Pages**를 통해 별도의 서버 호스팅 비용 없이 웹 브라우저에서 실행 가능한 주소를 즉시 만들 수 있습니다.

### 1. 로컬 저장소 업로드 절차
```bash
# 1. Git 초기화
git init

# 2. 파일 추가 및 첫 커밋
git add .
git commit -m "feat: Initialize Cursor Menu Launcher"

# 3. 브랜치명을 main으로 설정 및 원격 저장소 추가
git branch -M main
git remote add origin https://github.com/<사용자명>/<저장소명>.git

# 4. 푸시
git push -u origin main
```

### 2. GitHub Pages 활성화 방법
1. 업로드한 GitHub 저장소 페이지의 우측 상단 **Settings**로 이동합니다.
2. 왼쪽 메뉴에서 **Pages**를 클릭합니다.
3. Build and deployment -> Branch 설정에서 **`main`** 브랜치와 **`/ (root)`** 폴더를 선택한 후 **Save**를 누릅니다.
4. 1분 후 생성되는 URL을 확인합니다.
   * `https://<사용자명>.github.io/<저장소명>/index.html` (정적 버전)
   * `https://<사용자명>.github.io/<저장소명>/index_dynamic.html` (동적 JSON 파싱 버전)
