#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cursor IDE Style Pulldown Menu  ─  PyQt6 Version
동영상 완전 재현: File / Edit / Selection / View / Go / Run / Terminal / Help
단축키 · 구분선 · 서브메뉴(▶) · 비활성 항목 포함
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QMenuBar,
    QMenu, QLabel, QVBoxLayout, QHBoxLayout,
    QFrame, QPushButton, QStatusBar, QSizePolicy,
    QToolBar
)
from PyQt6.QtCore    import Qt, QSize
from PyQt6.QtGui     import (
    QAction, QFont, QPainter, QColor, QLinearGradient,
    QIcon, QPixmap, QPen, QBrush, QPolygon
)
from PyQt6.QtCore    import QPoint

# ═══════════════════════════ QSS STYLESHEET ══════════════════════════
QSS = """
/* ─── 전체 앱 ────────────────────────────────────────────── */
QMainWindow, QWidget#central {
    background-color: #1e1e1e;
}

/* ─── 메뉴바 ─────────────────────────────────────────────── */
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

/* ─── 드롭다운 메뉴 ──────────────────────────────────────── */
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
/* 서브메뉴 화살표 커스텀 */
QMenu::indicator {
    width: 0px;
}

/* ─── 타이틀바 영역 ──────────────────────────────────────── */
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

/* ─── 워크스페이스 ───────────────────────────────────────── */
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

/* ─── 상태바 ─────────────────────────────────────────────── */
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
    """Cursor 로고를 직접 그리는 캔버스 위젯"""
    def __init__(self, size=56):
        super().__init__()
        self.sz = size
        self.setFixedSize(size, size)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        sz = self.sz

        # 배경 라운드 사각형
        p.setBrush(QColor('#1a1a1a'))
        p.setPen(QColor('#333333'))
        p.drawRoundedRect(0, 0, sz, sz, sz * 0.18, sz * 0.18)

        # 흰색 육각형 (왼쪽)
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

        # 파란색 오른쪽 절반
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
        self.setWindowTitle('Cursor IDE Style Pulldown Menu — PyQt6')
        self.resize(1100, 700)
        self.setMinimumSize(800, 500)

        self._build_ui()

    # ── UI 구성 ──────────────────────────────────────────────────────
    def _build_ui(self):
        # 중앙 위젯
        central = QWidget()
        central.setObjectName('central')
        self.setCentralWidget(central)

        root_lay = QVBoxLayout(central)
        root_lay.setContentsMargins(0, 0, 0, 0)
        root_lay.setSpacing(0)

        # 1. 타이틀바 (메뉴바 위)
        root_lay.addWidget(self._make_titlebar())

        # 2. 메뉴바
        self._build_menubar()

        # 3. 워크스페이스
        root_lay.addWidget(self._make_workspace(), stretch=1)

        # 4. 상태바
        self._build_statusbar()

    # ── 타이틀바 ─────────────────────────────────────────────────────
    def _make_titlebar(self):
        tb = QWidget()
        tb.setObjectName('titlebar')
        tb.setFixedHeight(34)
        lay = QHBoxLayout(tb)
        lay.setContentsMargins(10, 0, 10, 0)
        lay.setSpacing(8)

        # 작은 로고 아이콘
        logo_sm = LogoWidget(size=18)
        lay.addWidget(logo_sm)

        lay.addStretch()

        # 검색창
        search = QLabel('🔍  Search')
        search.setObjectName('searchbar')
        search.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        lay.addWidget(search)

        lay.addStretch()

        # Upgrade 버튼
        upg = QPushButton('Upgrade to Pro')
        upg.setObjectName('upgbtn')
        upg.setCursor(Qt.CursorShape.PointingHandCursor)
        lay.addWidget(upg)

        return tb

    # ── 메뉴바 ───────────────────────────────────────────────────────
    def _build_menubar(self):
        mb = self.menuBar()

        # ── File ──────────────────────────────────────────
        file_m = mb.addMenu('File')
        self._add(file_m, 'New Text File',               'Ctrl+N')
        self._add(file_m, 'New Window',                  'Ctrl+Shift+N')
        self._add(file_m, 'New Agents Window')
        sub_prof = file_m.addMenu('New Window with Profile  ▶')
        self._add(sub_prof, 'Default Profile')
        self._add(sub_prof, 'Create New Profile...')
        file_m.addSeparator()
        self._add(file_m, 'Open File...',                'Ctrl+O')
        self._add(file_m, 'Open Folder...',              'Ctrl+M Ctrl+O')
        self._add(file_m, 'Open Workspace from File...')
        sub_rec = file_m.addMenu('Open Recent  ▶')
        self._add(sub_rec, 'test1',  'D:\\Temp\\Cursor')
        self._add(sub_rec, 'html',   'D:\\Temp')
        sub_rec.addSeparator()
        self._add(sub_rec, 'More...')
        file_m.addSeparator()
        self._add(file_m, 'Add Folder to Workspace...')
        self._add(file_m, 'Save Workspace As...')
        self._add(file_m, 'Duplicate Workspace')
        file_m.addSeparator()
        self._add(file_m, 'Save',       'Ctrl+S',       dis=True)
        self._add(file_m, 'Save As...', 'Ctrl+Shift+S', dis=True)
        self._add(file_m, 'Save All',   'Ctrl+M S',     dis=True)
        file_m.addSeparator()
        sub_shr = file_m.addMenu('Share  ▶')
        self._add(sub_shr, 'Copy Link to Selection')
        self._add(sub_shr, 'Share via Live Share')
        file_m.addSeparator()
        self._add(file_m, 'Auto Save')
        sub_pref = file_m.addMenu('Preferences  ▶')
        self._add(sub_pref, 'Settings',              'Ctrl+,')
        self._add(sub_pref, 'Keyboard Shortcuts',    'Ctrl+K Ctrl+S')
        sub_pref.addSeparator()
        self._add(sub_pref, 'Color Theme')
        self._add(sub_pref, 'File Icon Theme')
        file_m.addSeparator()
        self._add(file_m, 'Revert File',    '',         dis=True)
        self._add(file_m, 'Close Editor',   'Ctrl+F4', dis=True)
        self._add(file_m, 'Close Window',   'Alt+F4')
        file_m.addSeparator()
        act_exit = self._add(file_m, 'Exit')
        act_exit.triggered.connect(self.close)

        # ── Edit ──────────────────────────────────────────
        edit_m = mb.addMenu('Edit')
        self._add(edit_m, 'Undo',   'Ctrl+Z')
        self._add(edit_m, 'Redo',   'Ctrl+Y')
        edit_m.addSeparator()
        self._add(edit_m, 'Cut',    'Ctrl+X')
        self._add(edit_m, 'Copy',   'Ctrl+C')
        self._add(edit_m, 'Paste',  'Ctrl+V')
        edit_m.addSeparator()
        self._add(edit_m, 'Find',    'Ctrl+F', dis=True)
        self._add(edit_m, 'Replace', 'Ctrl+H', dis=True)
        edit_m.addSeparator()
        self._add(edit_m, 'Find in Files',    'Ctrl+Shift+F')
        self._add(edit_m, 'Replace in Files', 'Ctrl+Shift+H')
        edit_m.addSeparator()
        self._add(edit_m, 'Toggle Line Comment',        'Ctrl+/')
        self._add(edit_m, 'Toggle Block Comment',       'Shift+Alt+A')
        self._add(edit_m, 'Emmet: Expand Abbreviation', 'Tab')

        # ── Selection ─────────────────────────────────────
        sel_m = mb.addMenu('Selection')
        self._add(sel_m, 'Select All',      'Ctrl+A')
        self._add(sel_m, 'Expand Selection','Shift+Alt+\u2192')
        self._add(sel_m, 'Shrink Selection','Shift+Alt+\u2190')
        sel_m.addSeparator()
        self._add(sel_m, 'Copy Line Up',    'Shift+Alt+\u2191')
        self._add(sel_m, 'Copy Line Down',  'Shift+Alt+\u2193')
        self._add(sel_m, 'Move Line Up',    'Alt+\u2191')
        self._add(sel_m, 'Move Line Down',  'Alt+\u2193')
        self._add(sel_m, 'Duplicate Selection')
        sel_m.addSeparator()
        self._add(sel_m, 'Add Cursor Above',        'Ctrl+Alt+\u2191')
        self._add(sel_m, 'Add Cursor Below',        'Ctrl+Alt+\u2193')
        self._add(sel_m, 'Add Cursors to Line Ends','Shift+Alt+I')
        self._add(sel_m, 'Add Next Occurrence',     'Ctrl+D')
        self._add(sel_m, 'Select All Occurrences',  'Ctrl+Shift+L')
        sel_m.addSeparator()
        self._add(sel_m, 'Switch to Column Selection Mode')

        # ── View ──────────────────────────────────────────
        view_m = mb.addMenu('View')
        self._add(view_m, 'Command Palette...', 'Ctrl+Shift+P')
        self._add(view_m, 'Open View...')
        view_m.addSeparator()
        sub_app = view_m.addMenu('Appearance  ▶')
        self._add(sub_app, 'Full Screen', 'F11')
        self._add(sub_app, 'Zen Mode',    'Ctrl+K Z')
        sub_app.addSeparator()
        self._add(sub_app, 'Show Menu Bar')
        self._add(sub_app, 'Show Side Bar',   'Ctrl+B')
        self._add(sub_app, 'Show Status Bar')
        self._add(sub_app, 'Show Activity Bar')
        sub_lay = view_m.addMenu('Editor Layout  ▶')
        self._add(sub_lay, 'Split Up')
        self._add(sub_lay, 'Split Down')
        self._add(sub_lay, 'Split Left')
        self._add(sub_lay, 'Split Right')
        view_m.addSeparator()
        self._add(view_m, 'Explorer',      'Ctrl+Shift+E')
        self._add(view_m, 'Search',        'Ctrl+Shift+F')
        self._add(view_m, 'Source Control','Ctrl+Shift+G')
        self._add(view_m, 'Run',           'Ctrl+Shift+D')
        self._add(view_m, 'Extensions',    'Ctrl+Shift+X')
        view_m.addSeparator()
        self._add(view_m, 'Problems',      'Ctrl+Shift+M')
        self._add(view_m, 'Output',        'Ctrl+Shift+U')
        self._add(view_m, 'Debug Console', 'Ctrl+Shift+Alt+Y')
        self._add(view_m, 'Terminal',      'Ctrl+`')
        view_m.addSeparator()
        self._add(view_m, 'Word Wrap',     'Alt+Z', dis=True)

        # ── Go ────────────────────────────────────────────
        go_m = mb.addMenu('Go')
        self._add(go_m, 'Back',              'Alt+\u2190', dis=True)
        self._add(go_m, 'Forward',           'Alt+\u2192', dis=True)
        self._add(go_m, 'Last Edit Location','Ctrl+M Ctrl+Q', dis=True)
        go_m.addSeparator()
        sub_se = go_m.addMenu('Switch Editor  ▶')
        self._add(sub_se, 'Next Editor',     'Ctrl+PageDown')
        self._add(sub_se, 'Previous Editor', 'Ctrl+PageUp')
        sub_sg = go_m.addMenu('Switch Group  ▶')
        self._add(sub_sg, 'Group 1', 'Ctrl+1')
        self._add(sub_sg, 'Group 2', 'Ctrl+2')
        go_m.addSeparator()
        self._add(go_m, 'Go to File...',                'Ctrl+P')
        self._add(go_m, 'Go to Symbol in Workspace...', 'Ctrl+T')
        go_m.addSeparator()
        self._add(go_m, 'Go to Symbol in Editor...', 'Ctrl+Shift+O')
        self._add(go_m, 'Go to Definition',           'F12')
        self._add(go_m, 'Go to Declaration')
        self._add(go_m, 'Go to Type Definition')
        self._add(go_m, 'Go to Implementations',      'Ctrl+F12')
        self._add(go_m, 'Add Symbol to Current Chat')
        self._add(go_m, 'Go to References',           'Shift+F12')
        self._add(go_m, 'Add Symbol to New Chat')
        go_m.addSeparator()
        self._add(go_m, 'Go to Line/Column...', 'Ctrl+G')
        self._add(go_m, 'Go to Bracket',        'Ctrl+Shift+\\')
        go_m.addSeparator()
        self._add(go_m, 'Next Problem',     'F8')
        self._add(go_m, 'Previous Problem', 'Shift+F8')
        go_m.addSeparator()
        self._add(go_m, 'Next Change',     'Alt+F3')
        self._add(go_m, 'Previous Change', 'Shift+Alt+F3')

        # ── Run ───────────────────────────────────────────
        run_m = mb.addMenu('Run')
        self._add(run_m, 'Start Debugging',        'F5')
        self._add(run_m, 'Run Without Debugging',  'Ctrl+F5')
        self._add(run_m, 'Stop Debugging',         'Shift+F5',       dis=True)
        self._add(run_m, 'Restart Debugging',      'Ctrl+Shift+F5',  dis=True)
        run_m.addSeparator()
        self._add(run_m, 'Open Configurations')
        self._add(run_m, 'Add Configuration...')
        run_m.addSeparator()
        self._add(run_m, 'Step Over',  'F10',        dis=True)
        self._add(run_m, 'Step Into',  'F11',        dis=True)
        self._add(run_m, 'Step Out',   'Shift+F11',  dis=True)
        self._add(run_m, 'Continue',   'F5',         dis=True)
        run_m.addSeparator()
        self._add(run_m, 'Toggle Breakpoint',       'F9')
        self._add(run_m, 'New Breakpoint')
        run_m.addSeparator()
        self._add(run_m, 'Enable All Breakpoints',  '', dis=True)
        self._add(run_m, 'Disable All Breakpoints', '', dis=True)
        self._add(run_m, 'Remove All Breakpoints')

        # ── Terminal ──────────────────────────────────────
        term_m = mb.addMenu('Terminal')
        self._add(term_m, 'New Terminal',   'Ctrl+`')
        self._add(term_m, 'Split Terminal', 'Ctrl+Shift+5')
        term_m.addSeparator()
        self._add(term_m, 'Run Task...')
        self._add(term_m, 'Run Build Task...', 'Ctrl+Shift+B')
        self._add(term_m, 'Run Active File')
        self._add(term_m, 'Run Selected Text')
        term_m.addSeparator()
        self._add(term_m, 'Show Running Tasks...')
        self._add(term_m, 'Restart Running Task...', '', dis=True)
        self._add(term_m, 'Terminate Task...',       '', dis=True)
        term_m.addSeparator()
        self._add(term_m, 'Configure Tasks...')
        self._add(term_m, 'Configure Default Build Task...')

        # ── Help ──────────────────────────────────────────
        help_m = mb.addMenu('Help')
        self._add(help_m, 'Welcome')
        self._add(help_m, 'Show All Commands',            'Ctrl+Shift+P')
        self._add(help_m, 'Documentation')
        self._add(help_m, 'Editor Playground')
        help_m.addSeparator()
        self._add(help_m, 'Show Release Notes')
        self._add(help_m, 'Keyboard Shortcuts Reference')
        self._add(help_m, 'Video Tutorials')
        self._add(help_m, 'Tips and Tricks')
        help_m.addSeparator()
        self._add(help_m, 'Join Us on X (Twitter)')
        self._add(help_m, 'Request Feature')
        self._add(help_m, 'Report Issue')
        help_m.addSeparator()
        self._add(help_m, 'View License')
        self._add(help_m, 'Privacy Statement')
        help_m.addSeparator()
        self._add(help_m, 'Toggle Developer Tools')
        help_m.addSeparator()
        self._add(help_m, 'About')

    def _add(self, menu, label, shortcut='', dis=False):
        """메뉴 액션 추가 헬퍼"""
        act = QAction(label, self)
        if shortcut:
            act.setShortcut(shortcut)
        act.setEnabled(not dis)
        menu.addAction(act)
        return act

    # ── 워크스페이스 ─────────────────────────────────────────────────
    def _make_workspace(self):
        ws = QWidget()
        ws.setObjectName('workspace')
        outer = QVBoxLayout(ws)
        outer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        outer.setSpacing(0)

        # 중앙 컨테이너
        center = QWidget()
        center.setObjectName('workspace')
        c_lay = QVBoxLayout(center)
        c_lay.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        c_lay.setSpacing(0)
        c_lay.setContentsMargins(0, 0, 0, 0)

        # 로고
        logo = LogoWidget(56)
        logo_wrap = QHBoxLayout()
        logo_wrap.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        logo_wrap.addWidget(logo)
        c_lay.addLayout(logo_wrap)
        c_lay.addSpacing(10)

        # CURSOR 텍스트
        lbl_logo = QLabel('CURSOR')
        lbl_logo.setObjectName('logo_text')
        lbl_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        c_lay.addWidget(lbl_logo)
        c_lay.addSpacing(4)

        # Plan 텍스트
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

        # 액션 버튼 3개
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

        # Recent Projects 제목
        rec_title = QLabel('RECENT PROJECTS')
        rec_title.setObjectName('recent_label')
        rec_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        c_lay.addWidget(rec_title)
        c_lay.addSpacing(6)

        # Recent items
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

    # ── 상태바 ───────────────────────────────────────────────────────
    def _build_statusbar(self):
        sb = self.statusBar()
        sb.showMessage('  ⌀ 0  △ 0')
        right = QLabel('Cursor Tab  ')
        right.setStyleSheet('color:#ffffff; font-size:11px;')
        sb.addPermanentWidget(right)


# ═══════════════════════════ ENTRY POINT ════════════════════════════
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(QSS)
    app.setStyle('Fusion')   # 크로스 플랫폼 일관 스타일

    win = CursorWindow()
    win.show()
    sys.exit(app.exec())
