#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cursor IDE Style Pulldown Menu  ─  PyQt6 Dynamic Version
로컬 JSON 설정 또는 GitHub Raw URL 동적 동기화 구현 버전
"""

import sys
import os
import json
import urllib.request
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QMenuBar,
    QMenu, QLabel, QVBoxLayout, QHBoxLayout,
    QFrame, QPushButton, QStatusBar, QSizePolicy,
    QToolBar, QMessageBox
)
from PyQt6.QtCore    import Qt, QSize, QPoint
from PyQt6.QtGui     import (
    QAction, QFont, QPainter, QColor, QLinearGradient,
    QIcon, QPixmap, QPen, QBrush, QPolygon
)

# ═══════════════════════════ QSS STYLESHEET ══════════════════════════
QSS = """
QMainWindow, QWidget#central {
    background-color: #1e1e1e;
}
QMenuBar {
    background-color: #3c3c3c;
    color: #cccccc;
    font-family: "Segoe UI";
    font-size: 13px;
    padding: 2px 4px;
    spacing: 0px;
    border: none;
}
QMenuBar::item {
    background: transparent;
    padding: 4px 10px;
    border-radius: 4px;
    color: #cccccc;
}
QMenuBar::item:selected {
    background-color: #505050;
    color: #ffffff;
}
QMenuBar::item:pressed {
    background-color: #505050;
    color: #ffffff;
}
QMenu {
    background-color: #252526;
    border: 1px solid #454545;
    border-radius: 6px;
    padding: 4px 0px;
    font-family: "Segoe UI";
    font-size: 13px;
    color: #cccccc;
}
QMenu::item {
    padding: 5px 32px 5px 24px;
    color: #cccccc;
    background: transparent;
    min-width: 220px;
}
QMenu::item:selected {
    background-color: #04395e;
    color: #ffffff;
    border-radius: 0px;
}
QMenu::item:disabled {
    color: #555555;
    background: transparent;
}
QMenu::separator {
    height: 1px;
    background-color: #454545;
    margin: 4px 0px;
}
QMenu::right-arrow {
    image: none;
    width: 0px;
}
QMenu::indicator {
    width: 0px;
}
QWidget#titlebar {
    background-color: #252526;
    border-bottom: 1px solid #3c3c3c;
    min-height: 32px;
    max-height: 32px;
}
QLabel#searchbar {
    background-color: #3c3c3c;
    color: #888888;
    border: 1px solid #555555;
    border-radius: 5px;
    padding: 2px 10px;
    font-size: 12px;
    min-width: 280px;
    max-width: 280px;
    min-height: 22px;
    max-height: 22px;
}
QPushButton#upgbtn {
    background-color: #0e639c;
    color: #ffffff;
    border: none;
    border-radius: 3px;
    padding: 3px 10px;
    font-size: 11px;
    font-family: "Segoe UI";
}
QPushButton#upgbtn:hover {
    background-color: #1177bb;
}
QWidget#workspace {
    background-color: #1e1e1e;
}
QLabel#logo_text {
    color: #ffffff;
    font-family: "Segoe UI";
    font-size: 22px;
    font-weight: bold;
    letter-spacing: 4px;
    background: transparent;
}
QLabel#plan_text {
    color: #777777;
    font-size: 12px;
    font-family: "Segoe UI";
    background: transparent;
}
QLabel#link_text {
    color: #3794ff;
    font-size: 12px;
    font-family: "Segoe UI";
    background: transparent;
}
QPushButton#actionbtn {
    background-color: #2d2d30;
    color: #cccccc;
    border: 1px solid #454545;
    border-radius: 6px;
    padding: 8px 18px;
    font-size: 13px;
    font-family: "Segoe UI";
    min-width: 110px;
}
QPushButton#actionbtn:hover {
    background-color: #37373d;
    border-color: #666666;
    color: #ffffff;
}
QLabel#recent_label {
    color: #555555;
    font-family: "Segoe UI";
    font-size: 10px;
    background: transparent;
    letter-spacing: 1px;
}
QStatusBar {
    background-color: #007acc;
    color: #ffffff;
    font-family: "Segoe UI";
    font-size: 11px;
    border: none;
}
QStatusBar::item { border: none; }
"""

# ═══════════════════════════ LOGO WIDGET ════════════════════════════
class LogoWidget(QWidget):
    def __init__(self, size=56):
        super().__init__()
        self.sz = size
        self.setFixedSize(size, size)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        sz = self.sz

        p.setBrush(QColor('#1a1a1a'))
        p.setPen(QColor('#333333'))
        p.drawRoundedRect(0, 0, sz, sz, sz * 0.18, sz * 0.18)

        pts_w = QPolygon([
            QPoint(int(sz*0.25), int(sz*0.20)),
            QPoint(int(sz*0.75), int(sz*0.20)),
            QPoint(int(sz*0.75), int(sz*0.55)),
            QPoint(int(sz*0.50), int(sz*0.82)),
            QPoint(int(sz*0.25), int(sz*0.55)),
        ])
        p.setBrush(QColor('#ffffff'))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawPolygon(pts_w)

        pts_b = QPolygon([
            QPoint(int(sz*0.50), int(sz*0.20)),
            QPoint(int(sz*0.75), int(sz*0.20)),
            QPoint(int(sz*0.75), int(sz*0.55)),
            QPoint(int(sz*0.50), int(sz*0.55)),
        ])
        p.setBrush(QColor('#3794ff'))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawPolygon(pts_b)
        p.end()

# ═══════════════════════════ RECENT ITEM ROW ════════════════════════
class RecentItemRow(QFrame):
    def __init__(self, name, path):
        super().__init__()
        self.setStyleSheet("""
            RecentItemRow {
                background: transparent;
                border-radius: 4px;
            }
            RecentItemRow:hover {
                background-color: #2a2d2e;
            }
        """)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        lay = QHBoxLayout(self)
        lay.setContentsMargins(10, 3, 10, 3)
        lay.setSpacing(60)

        lbl_name = QLabel(name)
        lbl_name.setStyleSheet("color:#cccccc; font-size:13px; font-family:'Segoe UI';")
        lbl_path = QLabel(path)
        lbl_path.setStyleSheet("color:#555555; font-size:11px; font-family:'Segoe UI';")
        lbl_path.setAlignment(Qt.AlignmentFlag.AlignRight)

        lay.addWidget(lbl_name)
        lay.addStretch()
        lay.addWidget(lbl_path)

# ═══════════════════════════ MAIN WINDOW ════════════════════════════
class CursorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cursor IDE Style Pulldown Menu — PyQt6 Dynamic')
        self.resize(1100, 700)
        self.setMinimumSize(800, 500)
        
        # 윈도우 창 아이콘 설정
        if os.path.exists("app_icon.ico"):
            self.setWindowIcon(QIcon("app_icon.ico"))

        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        central.setObjectName('central')
        self.setCentralWidget(central)

        root_lay = QVBoxLayout(central)
        root_lay.setContentsMargins(0, 0, 0, 0)
        root_lay.setSpacing(0)

        # 1. 타이틀바
        root_lay.addWidget(self._make_titlebar())

        # 2. 메뉴바 (동적 로드된 설정에 따라 빌드)
        self._build_menubar()

        # 3. 워크스페이스
        root_lay.addWidget(self._make_workspace(), stretch=1)

        # 4. 상태바
        self._build_statusbar()

    def _make_titlebar(self):
        tb = QWidget()
        tb.setObjectName('titlebar')
        tb.setFixedHeight(34)
        lay = QHBoxLayout(tb)
        lay.setContentsMargins(10, 0, 10, 0)
        lay.setSpacing(8)

        logo_sm = LogoWidget(size=18)
        lay.addWidget(logo_sm)

        lay.addStretch()

        search = QLabel('🔍  Search')
        search.setObjectName('searchbar')
        search.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        lay.addWidget(search)

        lay.addStretch()

        upg = QPushButton('Upgrade to Pro')
        upg.setObjectName('upgbtn')
        upg.setCursor(Qt.CursorShape.PointingHandCursor)
        lay.addWidget(upg)

        return tb

    # ── 동적 메뉴 로드 및 구성 로직 ───────────────────────────────────
    
    def _load_menu_config(self):
        # [중요] 향후 GitHub에 menu_config.json을 올린 후 해당 raw URL 주소로 변경하세요.
        # 예시: "https://raw.githubusercontent.com/사용자이름/저장소이름/main/menu_config.json"
        github_url = "https://raw.githubusercontent.com/username/repo/main/menu_config.json"
        local_path = "menu_config.json"

        # 1. 로컬 개발 환경용 로드 시도
        if os.path.exists(local_path):
            try:
                with open(local_path, "r", encoding="utf-8") as f:
                    print("[INFO] 로컬 설정 파일(menu_config.json) 로드 성공")
                    return json.load(f)
            except Exception as e:
                print(f"[WARNING] 로컬 설정 로드 실패: {e}")

        # 2. 원격 주소 조회 (URL이 수정되었을 때 동작)
        if "username/repo" not in github_url:
            try:
                print(f"[INFO] 원격 서버({github_url}) 설정 로드 시도...")
                with urllib.request.urlopen(github_url, timeout=3) as response:
                    data = response.read().decode('utf-8')
                    print("[INFO] GitHub 원격 설정 동기화 성공!")
                    return json.loads(data)
            except Exception as e:
                print(f"[ERROR] 원격 로드 실패: {e}")

        # 3. 로컬도 없고 원격도 연결 안될 때 내장 기본값 사용 (Fallback)
        print("[INFO] 기본 내장(Fallback) 메뉴 데이터 사용")
        return {
            "File": [
                {"label": "New Text File", "shortcut": "Ctrl+N"},
                {"label": "New Window", "shortcut": "Ctrl+Shift+N"},
                {"separator": True},
                {"label": "Exit"}
            ],
            "Help": [
                {"label": "About"}
            ]
        }

    def _build_menubar(self):
        mb = self.menuBar()
        config = self._load_menu_config()

        for menu_name, items in config.items():
            menu = mb.addMenu(menu_name)
            self._build_submenu(menu, items)

    def _build_submenu(self, parent_menu, items):
        for item in items:
            if item.get("separator"):
                parent_menu.addSeparator()
            elif "submenu" in item:
                # 하위 서브메뉴 재귀적 구성
                sub_menu = parent_menu.addMenu(item["label"] + "  ▶")
                self._build_submenu(sub_menu, item["submenu"])
            else:
                label = item.get("label", "")
                shortcut = item.get("shortcut", "")
                disabled = item.get("disabled", False)
                act = self._add(parent_menu, label, shortcut, dis=disabled)
                
                # 특정 메뉴 아이템 트리거 연동
                if label == "Exit":
                    act.triggered.connect(self.close)
                elif label == "About":
                    act.triggered.connect(self._show_about)

    def _add(self, menu, label, shortcut='', dis=False):
        act = QAction(label, self)
        if shortcut:
            act.setShortcut(shortcut)
        act.setEnabled(not dis)
        menu.addAction(act)
        return act

    def _show_about(self):
        QMessageBox.about(
            self,
            "About Cursor Menu",
            "<h3>Cursor IDE Style Custom Menu Launcher</h3>"
            "<p>이 프로그램은 전 세계 어디서나 웹브라우저 없이 실시간 동기화되는 데스크톱 앱입니다.</p>"
            "<p><b>개발 정보:</b> Python, PyQt6, PyInstaller</p>"
        )

    # ── 워크스페이스 및 상태바 ────────────────────────────────────────
    def _make_workspace(self):
        ws = QWidget()
        ws.setObjectName('workspace')
        outer = QVBoxLayout(ws)
        outer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        outer.setSpacing(0)

        center = QWidget()
        center.setObjectName('workspace')
        c_lay = QVBoxLayout(center)
        c_lay.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        c_lay.setSpacing(0)
        c_lay.setContentsMargins(0, 0, 0, 0)

        logo = LogoWidget(56)
        logo_wrap = QHBoxLayout()
        logo_wrap.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        logo_wrap.addWidget(logo)
        c_lay.addLayout(logo_wrap)
        c_lay.addSpacing(10)

        lbl_logo = QLabel('CURSOR')
        lbl_logo.setObjectName('logo_text')
        lbl_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        c_lay.addWidget(lbl_logo)
        c_lay.addSpacing(4)

        plan_row = QHBoxLayout()
        plan_row.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        plan_row.setSpacing(0)
        plan_lbl = QLabel('Free Plan  ·  ')
        plan_lbl.setObjectName('plan_text')
        upg_lbl = QLabel('Upgrade')
        upg_lbl.setObjectName('link_text')
        upg_lbl.setCursor(Qt.CursorShape.PointingHandCursor)
        plan_row.addWidget(plan_lbl)
        plan_row.addWidget(upg_lbl)
        c_lay.addLayout(plan_row)
        c_lay.addSpacing(20)

        btn_row = QHBoxLayout()
        btn_row.setSpacing(12)
        btn_row.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        for icon, text in [('📁', 'Open project'),
                           ('⎘',  'Clone repo'),
                           ('⊞', 'Connect via SSH')]:
            btn = QPushButton(f'{icon}  {text}')
            btn.setObjectName('actionbtn')
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_row.addWidget(btn)
        c_lay.addLayout(btn_row)
        c_lay.addSpacing(24)

        rec_title = QLabel('RECENT PROJECTS')
        rec_title.setObjectName('recent_label')
        rec_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        c_lay.addWidget(rec_title)
        c_lay.addSpacing(6)

        for name, path in [
            ('test1',  'D:\\Temp\\Cursor'),
            ('Cursor', 'D:\\Temp'),
            ('html',   'D:\\Temp'),
            ('test2',  'C:\\Users\\SBS\\Documents\\Cursor'),
            ('test1',  'C:\\Users\\SBS\\Documents\\Cursor'),
        ]:
            row = RecentItemRow(name, path)
            c_lay.addWidget(row)

        outer.addWidget(center)
        return ws

    def _build_statusbar(self):
        sb = self.statusBar()
        
        # 상태 메시지 설정 (로컬 또는 원격 로드 여부에 따라 자동 안내)
        if os.path.exists("menu_config.json"):
            sb.showMessage('  ⌀ 0  △ 0  [로컬 menu_config.json 설정 로딩됨]')
        else:
            sb.showMessage('  ⌀ 0  △ 0  [기본 Fallback 메뉴 사용 중]')
            
        right = QLabel('Cursor Tab  ')
        right.setStyleSheet('color:#ffffff; font-size:11px;')
        sb.addPermanentWidget(right)

# ═══════════════════════════ ENTRY POINT ════════════════════════════
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(QSS)
    app.setStyle('Fusion')

    win = CursorWindow()
    win.show()
    sys.exit(app.exec())
