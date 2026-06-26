#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cursor IDE Style Pulldown Menu  —  Python / tkinter Version
동영상 참조 완전 재현: File, Edit, Selection, View, Go, Run, Terminal, Help
단축키 표시 / 구분선 / 서브메뉴(▶) / 비활성 항목 포함
"""

import tkinter as tk
import sys

# ═══════════════════════════ COLOR PALETTE ═══════════════════════════
BG      = '#1e1e1e'   # 앱 배경
TBG     = '#252526'   # 타이틀바 / 드롭다운 배경
MBG     = '#3c3c3c'   # 메뉴바 배경
MHOV    = '#505050'   # 메뉴 버튼 호버
MFG     = '#cccccc'   # 메뉴바 텍스트
MFG_HI  = '#ffffff'   # 메뉴바 텍스트 선택
DBG     = '#252526'   # 드롭다운 배경
DBD     = '#454545'   # 드롭다운 테두리 / 구분선
IHOV    = '#04395e'   # 항목 호버 (파란색)
IFG     = '#cccccc'   # 항목 텍스트
IDIS    = '#555555'   # 비활성 항목 텍스트
SFG     = '#888888'   # 단축키 텍스트
STBG    = '#007acc'   # 상태바 배경
STFG    = '#ffffff'   # 상태바 텍스트
BTNBG   = '#2d2d30'   # 액션 버튼 배경
BTNBD   = '#454545'   # 액션 버튼 테두리
BTNHOV  = '#37373d'   # 액션 버튼 호버
RECHOV  = '#2a2d2e'   # 최근 항목 호버

FN   = ('Segoe UI', 9)
FNS  = ('Segoe UI', 8)
FLG  = ('Segoe UI', 18, 'bold')
FLOGO = ('Segoe UI', 11)

# ═══════════════════════════ MENU DEFINITIONS ═══════════════════════
# 포맷: (label, shortcut)  or  (label, shortcut, submenu_list)  or  (label, shortcut, submenu, disabled)
# None = 구분선

FILE_MENU = [
    ('New Text File',               'Ctrl+N'),
    ('New Window',                  'Ctrl+Shift+N'),
    ('New Agents Window',           ''),
    ('New Window with Profile',     '', [
        ('Default Profile',             ''),
        ('Create New Profile...',       ''),
    ]),
    None,
    ('Open File...',                'Ctrl+O'),
    ('Open Folder...',              'Ctrl+M Ctrl+O'),
    ('Open Workspace from File...', ''),
    ('Open Recent',                 '', [
        ('test1',    'D:\\Temp\\Cursor'),
        ('html',     'D:\\Temp'),
        None,
        ('More...', ''),
    ]),
    None,
    ('Add Folder to Workspace...',  ''),
    ('Save Workspace As...',        ''),
    ('Duplicate Workspace',         ''),
    None,
    ('Save',                        'Ctrl+S',        None, True),
    ('Save As...',                  'Ctrl+Shift+S',  None, True),
    ('Save All',                    'Ctrl+M S',      None, True),
    None,
    ('Share',                       '', [
        ('Copy Link to Selection',      ''),
        ('Share via Live Share',        ''),
    ]),
    None,
    ('Auto Save',                   ''),
    ('Preferences',                 '', [
        ('Settings',                    'Ctrl+,'),
        ('Keyboard Shortcuts',          'Ctrl+K Ctrl+S'),
        None,
        ('Color Theme',                 ''),
        ('File Icon Theme',             ''),
    ]),
    None,
    ('Revert File',                 '',              None, True),
    ('Close Editor',                'Ctrl+F4',       None, True),
    ('Close Window',                'Alt+F4'),
    None,
    ('Exit',                        ''),
]

EDIT_MENU = [
    ('Undo',                        'Ctrl+Z'),
    ('Redo',                        'Ctrl+Y'),
    None,
    ('Cut',                         'Ctrl+X'),
    ('Copy',                        'Ctrl+C'),
    ('Paste',                       'Ctrl+V'),
    None,
    ('Find',                        'Ctrl+F',        None, True),
    ('Replace',                     'Ctrl+H',        None, True),
    None,
    ('Find in Files',               'Ctrl+Shift+F'),
    ('Replace in Files',            'Ctrl+Shift+H'),
    None,
    ('Toggle Line Comment',         'Ctrl+/'),
    ('Toggle Block Comment',        'Shift+Alt+A'),
    ('Emmet: Expand Abbreviation',  'Tab'),
]

SELECTION_MENU = [
    ('Select All',                   'Ctrl+A'),
    ('Expand Selection',             'Shift+Alt+\u2192'),
    ('Shrink Selection',             'Shift+Alt+\u2190'),
    None,
    ('Copy Line Up',                 'Shift+Alt+\u2191'),
    ('Copy Line Down',               'Shift+Alt+\u2193'),
    ('Move Line Up',                 'Alt+\u2191'),
    ('Move Line Down',               'Alt+\u2193'),
    ('Duplicate Selection',          ''),
    None,
    ('Add Cursor Above',             'Ctrl+Alt+\u2191'),
    ('Add Cursor Below',             'Ctrl+Alt+\u2193'),
    ('Add Cursors to Line Ends',     'Shift+Alt+I'),
    ('Add Next Occurrence',          'Ctrl+D'),
    ('Select All Occurrences',       'Ctrl+Shift+L'),
    None,
    ('Switch to Column Selection Mode', ''),
]

VIEW_MENU = [
    ('Command Palette...',           'Ctrl+Shift+P'),
    ('Open View...',                 ''),
    None,
    ('Appearance',                   '', [
        ('Full Screen',                  'F11'),
        ('Zen Mode',                     'Ctrl+K Z'),
        None,
        ('Show Menu Bar',                ''),
        ('Show Side Bar',                'Ctrl+B'),
        ('Show Status Bar',              ''),
        ('Show Activity Bar',            ''),
    ]),
    ('Editor Layout',                '', [
        ('Split Up',     ''),
        ('Split Down',   ''),
        ('Split Left',   ''),
        ('Split Right',  ''),
    ]),
    None,
    ('Explorer',                     'Ctrl+Shift+E'),
    ('Search',                       'Ctrl+Shift+F'),
    ('Source Control',               'Ctrl+Shift+G'),
    ('Run',                          'Ctrl+Shift+D'),
    ('Extensions',                   'Ctrl+Shift+X'),
    None,
    ('Problems',                     'Ctrl+Shift+M'),
    ('Output',                       'Ctrl+Shift+U'),
    ('Debug Console',                'Ctrl+Shift+Alt+Y'),
    ('Terminal',                     'Ctrl+`'),
    None,
    ('Word Wrap',                    'Alt+Z',         None, True),
]

GO_MENU = [
    ('Back',                         'Alt+\u2190',    None, True),
    ('Forward',                      'Alt+\u2192',    None, True),
    ('Last Edit Location',           'Ctrl+M Ctrl+Q', None, True),
    None,
    ('Switch Editor',                '', [
        ('Next Editor',                  'Ctrl+PageDown'),
        ('Previous Editor',              'Ctrl+PageUp'),
    ]),
    ('Switch Group',                 '', [
        ('Group 1',  'Ctrl+1'),
        ('Group 2',  'Ctrl+2'),
    ]),
    None,
    ('Go to File...',                'Ctrl+P'),
    ('Go to Symbol in Workspace...', 'Ctrl+T'),
    None,
    ('Go to Symbol in Editor...',    'Ctrl+Shift+O'),
    ('Go to Definition',             'F12'),
    ('Go to Declaration',            ''),
    ('Go to Type Definition',        ''),
    ('Go to Implementations',        'Ctrl+F12'),
    ('Add Symbol to Current Chat',   ''),
    ('Go to References',             'Shift+F12'),
    ('Add Symbol to New Chat',       ''),
    None,
    ('Go to Line/Column...',         'Ctrl+G'),
    ('Go to Bracket',                'Ctrl+Shift+\\'),
    None,
    ('Next Problem',                 'F8'),
    ('Previous Problem',             'Shift+F8'),
    None,
    ('Next Change',                  'Alt+F3'),
    ('Previous Change',              'Shift+Alt+F3'),
]

RUN_MENU = [
    ('Start Debugging',              'F5'),
    ('Run Without Debugging',        'Ctrl+F5'),
    ('Stop Debugging',               'Shift+F5',      None, True),
    ('Restart Debugging',            'Ctrl+Shift+F5', None, True),
    None,
    ('Open Configurations',          ''),
    ('Add Configuration...',         ''),
    None,
    ('Step Over',                    'F10',           None, True),
    ('Step Into',                    'F11',           None, True),
    ('Step Out',                     'Shift+F11',     None, True),
    ('Continue',                     'F5',            None, True),
    None,
    ('Toggle Breakpoint',            'F9'),
    ('New Breakpoint',               ''),
    None,
    ('Enable All Breakpoints',       '',              None, True),
    ('Disable All Breakpoints',      '',              None, True),
    ('Remove All Breakpoints',       ''),
]

TERMINAL_MENU = [
    ('New Terminal',                 'Ctrl+`'),
    ('Split Terminal',               'Ctrl+Shift+5'),
    None,
    ('Run Task...',                  ''),
    ('Run Build Task...',            'Ctrl+Shift+B'),
    ('Run Active File',              ''),
    ('Run Selected Text',            ''),
    None,
    ('Show Running Tasks...',        ''),
    ('Restart Running Task...',      '',              None, True),
    ('Terminate Task...',            '',              None, True),
    None,
    ('Configure Tasks...',           ''),
    ('Configure Default Build Task...', ''),
]

HELP_MENU = [
    ('Welcome',                      ''),
    ('Show All Commands',            'Ctrl+Shift+P'),
    ('Documentation',                ''),
    ('Editor Playground',            ''),
    None,
    ('Show Release Notes',           ''),
    ('Keyboard Shortcuts Reference', ''),
    ('Video Tutorials',              ''),
    ('Tips and Tricks',              ''),
    None,
    ('Join Us on X (Twitter)',       ''),
    ('Request Feature',              ''),
    ('Report Issue',                 ''),
    None,
    ('View License',                 ''),
    ('Privacy Statement',            ''),
    None,
    ('Toggle Developer Tools',       ''),
    None,
    ('About',                        ''),
]

MENU_DEFS = [
    ('File',       FILE_MENU,      260),
    ('Edit',       EDIT_MENU,      280),
    ('Selection',  SELECTION_MENU, 280),
    ('View',       VIEW_MENU,      260),
    ('Go',         GO_MENU,        320),
    ('Run',        RUN_MENU,       260),
    ('Terminal',   TERMINAL_MENU,  280),
    ('Help',       HELP_MENU,      260),
]


# ═══════════════════════════ DROPDOWN CLASS ══════════════════════════
class DropDown:
    """Floating dropdown panel (overrideredirect Toplevel)"""

    def __init__(self, root, items, x, y, app, min_width=260):
        self.root    = root
        self.app     = app
        self.items   = items
        self.sub_dd  = None
        self.highlighted_widgets = None

        # Outer window (acts as 1px border)
        self.win = tk.Toplevel(root)
        self.win.overrideredirect(True)
        self.win.configure(bg=DBD)
        self.win.lift()
        self.win.focus_set()

        # Inner content frame
        self.inner = tk.Frame(self.win, bg=DBG)
        self.inner.pack(padx=1, pady=1)

        self._min_w  = min_width
        self._build(self.inner, items)

        # Update and position
        self.win.update_idletasks()
        w = max(self.win.winfo_reqwidth(),  min_width)
        h = self.win.winfo_reqheight()
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        if x + w > sw: x = sw - w - 4
        if y + h > sh: y = sh - h - 4
        self.win.geometry(f'{w}x{h}+{x}+{y}')

    # ── Build items ─────────────────────────────────────────────────
    def _build(self, parent, items):
        tk.Frame(parent, bg=DBG, height=4).pack(fill='x')

        for item in items:
            if item is None:
                tk.Frame(parent, bg=DBD, height=1).pack(
                    fill='x', padx=0, pady=2)
                continue

            label    = item[0]
            shortcut = item[1] if len(item) > 1 else ''
            sub      = item[2] if len(item) > 2 else None
            disabled = item[3] if len(item) > 3 else False

            fg  = IDIS if disabled else IFG
            sfg = IDIS if disabled else SFG

            # Row
            row = tk.Frame(parent, bg=DBG)
            row.pack(fill='x')

            # Left indent
            tk.Label(row, width=2, bg=DBG, fg=DBG).pack(side='left')

            # Main text
            name_lbl = tk.Label(row, text=label, font=FN,
                                bg=DBG, fg=fg, anchor='w', pady=3)
            name_lbl.pack(side='left', fill='x', expand=True)

            # Right: arrow or shortcut
            if sub is not None:
                rt = tk.Label(row, text='\u25b6', font=FNS,
                              bg=DBG, fg=sfg, padx=8)
            elif shortcut:
                rt = tk.Label(row, text=shortcut, font=FNS,
                              bg=DBG, fg=sfg, padx=12)
            else:
                rt = tk.Label(row, text='', bg=DBG, padx=12)
            rt.pack(side='right')

            if not disabled:
                wgts = [row, name_lbl, rt]
                self._bind_hover(row, wgts, sub)

        tk.Frame(parent, bg=DBG, height=4).pack(fill='x')

    # ── Hover binding ────────────────────────────────────────────────
    def _bind_hover(self, row, wgts, sub_items):
        def on_enter(e):
            # Unhighlight previous row
            if self.highlighted_widgets and self.highlighted_widgets is not wgts:
                for w in self.highlighted_widgets:
                    try:
                        w.configure(bg=DBG)
                        if isinstance(w, tk.Label):
                            w.configure(fg=IFG, activebackground=DBG)
                    except tk.TclError:
                        pass

            # Highlight this row
            self.highlighted_widgets = wgts
            for w in wgts:
                try:
                    w.configure(bg=IHOV)
                    if isinstance(w, tk.Label):
                        w.configure(fg=MFG_HI)
                except tk.TclError:
                    pass

            # Submenu
            if sub_items:
                self._show_sub(row, sub_items)
            else:
                self._close_sub()

        for w in wgts:
            w.bind('<Enter>', on_enter)

    # ── Submenu ──────────────────────────────────────────────────────
    def _show_sub(self, row_widget, sub_items):
        self._close_sub()
        try:
            row_widget.update_idletasks()
            x = self.win.winfo_x() + self.win.winfo_width() - 2
            y = row_widget.winfo_rooty() - 5
        except tk.TclError:
            return
        self.sub_dd = DropDown(self.root, sub_items, x, y,
                               self.app, min_width=200)

    def _close_sub(self):
        if self.sub_dd:
            self.sub_dd.destroy()
            self.sub_dd = None

    # ── Destroy ──────────────────────────────────────────────────────
    def destroy(self):
        self._close_sub()
        try:
            if self.win.winfo_exists():
                self.win.destroy()
        except tk.TclError:
            pass


# ═══════════════════════════ MAIN APPLICATION ═════════════════════════
class CursorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Cursor IDE Style Pulldown Menu — Python')
        self.root.configure(bg=BG)
        self.root.geometry('1100x680')
        self.root.minsize(800, 500)

        # State
        self.active_dd   = None   # open DropDown
        self.active_btn  = None   # currently highlighted menu button label

        self._build()

        # Close menus on click outside
        self.root.bind('<Button-1>', self._on_root_click)
        self.root.bind('<Escape>',   lambda e: self._close_all())
        self.root.protocol('WM_DELETE_WINDOW', self._on_exit)

    # ── Build UI ─────────────────────────────────────────────────────
    def _build(self):
        self._build_titlebar()
        self._build_menubar()
        self._build_workspace()
        self._build_statusbar()

    # -- Title Bar ----
    def _build_titlebar(self):
        tb = tk.Frame(self.root, bg=TBG, height=30)
        tb.pack(fill='x', side='top')
        tb.pack_propagate(False)

        # Logo icon (canvas drawing)
        cv = tk.Canvas(tb, width=18, height=18, bg=TBG,
                       highlightthickness=0)
        cv.pack(side='left', padx=(10, 4), pady=6)
        cv.create_polygon(4, 18, 9, 3, 14, 18, fill='#ffffff', outline='')
        cv.create_polygon(9, 3, 14, 3, 14, 18, fill='#3794ff', outline='')

        # Search bar (centered)
        sf = tk.Frame(tb, bg='#3c3c3c', bd=0)
        sf.place(relx=0.5, rely=0.5, anchor='center',
                 width=300, height=22)
        tk.Label(sf, text='🔍  Search', font=FNS, bg='#3c3c3c',
                 fg='#888888', anchor='w').pack(fill='both', padx=8)

        # Upgrade button
        upg = tk.Label(tb, text='Upgrade to Pro', font=FNS,
                       bg='#0e639c', fg='#ffffff',
                       padx=8, pady=2, cursor='hand2')
        upg.pack(side='right', padx=10, pady=5)
        upg.bind('<Enter>', lambda e: upg.configure(bg='#1177bb'))
        upg.bind('<Leave>', lambda e: upg.configure(bg='#0e639c'))

    # -- Menu Bar ----
    def _build_menubar(self):
        mb = tk.Frame(self.root, bg=MBG, height=30)
        mb.pack(fill='x', side='top')
        mb.pack_propagate(False)

        self.menu_buttons = {}

        for name, items, width in MENU_DEFS:
            lbl = tk.Label(mb, text=name, font=FN,
                           bg=MBG, fg=MFG,
                           padx=8, pady=4, cursor='hand2')
            lbl.pack(side='left')
            self.menu_buttons[name] = (lbl, items, width)

            # Bindings
            lbl.bind('<Button-1>', lambda e, n=name: self._toggle_menu(n))
            lbl.bind('<Enter>',    lambda e, n=name: self._hover_menu(n))

    # -- Workspace ----
    def _build_workspace(self):
        ws = tk.Frame(self.root, bg=BG)
        ws.pack(fill='both', expand=True)

        # Center container
        center = tk.Frame(ws, bg=BG)
        center.place(relx=0.5, rely=0.5, anchor='center')

        # Logo (canvas)
        cv = tk.Canvas(center, width=56, height=56, bg=BG,
                       highlightthickness=0)
        cv.pack(pady=(0, 8))
        # Draw Cursor logo shape
        cv.create_rectangle(0, 0, 56, 56, fill='#1a1a1a',
                            outline='#333333', width=1)
        cv.create_polygon(14, 11, 42, 11, 42, 31, 28, 46, 14, 31,
                         fill='#ffffff', outline='')
        cv.create_polygon(28, 11, 42, 11, 42, 31, 28, 31,
                         fill='#3794ff', outline='')

        # CURSOR text
        tk.Label(center, text='C U R S O R', font=('Segoe UI', 16, 'bold'),
                 bg=BG, fg='#ffffff').pack()

        # Plan line
        plan_f = tk.Frame(center, bg=BG)
        plan_f.pack(pady=(2, 16))
        tk.Label(plan_f, text='Free Plan  ·  ', font=FNS,
                 bg=BG, fg='#777777').pack(side='left')
        upg = tk.Label(plan_f, text='Upgrade', font=FNS,
                       bg=BG, fg='#3794ff', cursor='hand2')
        upg.pack(side='left')

        # Action buttons
        btn_f = tk.Frame(center, bg=BG)
        btn_f.pack(pady=(0, 20))
        for icon, text in [('📁', 'Open project'),
                           ('⎘', 'Clone repo'),
                           ('⊞', 'Connect via SSH')]:
            self._action_btn(btn_f, icon, text)

        # Recent projects
        tk.Label(center, text='RECENT PROJECTS', font=('Segoe UI', 8),
                 bg=BG, fg='#555555').pack(anchor='w', pady=(0, 6))

        for name, path in [('test1', 'D:\\Temp\\Cursor'),
                            ('Cursor', 'D:\\Temp'),
                            ('html', 'D:\\Temp'),
                            ('test2', 'C:\\Users\\SBS\\Documents\\Cursor'),
                            ('test1', 'C:\\Users\\SBS\\Documents\\Cursor')]:
            self._recent_item(center, name, path)

    def _action_btn(self, parent, icon, text):
        f = tk.Frame(parent, bg=BTNBG, bd=1, relief='flat',
                     highlightbackground=BTNBD, highlightthickness=1)
        f.pack(side='left', padx=5)
        inner = tk.Frame(f, bg=BTNBG)
        inner.pack(padx=12, pady=8)
        tk.Label(inner, text=f'{icon}  {text}', font=FN,
                 bg=BTNBG, fg=MFG, cursor='hand2').pack()

        def enter(e):
            f.configure(highlightbackground='#666666')
            inner.configure(bg=BTNHOV)
            for w in inner.winfo_children():
                w.configure(bg=BTNHOV, fg=MFG_HI)
        def leave(e):
            f.configure(highlightbackground=BTNBD)
            inner.configure(bg=BTNBG)
            for w in inner.winfo_children():
                w.configure(bg=BTNBG, fg=MFG)

        for w in [f, inner] + list(inner.winfo_children()):
            w.bind('<Enter>', enter)
            w.bind('<Leave>', leave)

    def _recent_item(self, parent, name, path):
        f = tk.Frame(parent, bg=BG, cursor='hand2')
        f.pack(fill='x', pady=1)
        tk.Label(f, text=name,  font=FN,  bg=BG, fg=MFG,
                 anchor='w').pack(side='left', padx=8)
        tk.Label(f, text=path,  font=FNS, bg=BG, fg='#555555',
                 anchor='e').pack(side='right', padx=8)
        f.bind('<Enter>', lambda e: f.configure(bg=RECHOV))
        f.bind('<Leave>', lambda e: f.configure(bg=BG))

    # -- Status Bar ----
    def _build_statusbar(self):
        sb = tk.Frame(self.root, bg=STBG, height=22)
        sb.pack(fill='x', side='bottom')
        sb.pack_propagate(False)
        tk.Label(sb, text='⌀ 0  △ 0', font=FNS,
                 bg=STBG, fg=STFG).pack(side='left', padx=10)
        tk.Label(sb, text='Cursor Tab', font=FNS,
                 bg=STBG, fg=STFG).pack(side='right', padx=10)

    # ── Menu Logic ────────────────────────────────────────────────────
    def _toggle_menu(self, name):
        if self.active_dd and self.active_btn == name:
            self._close_all()
        else:
            self._open_menu(name)

    def _hover_menu(self, name):
        if self.active_dd and self.active_btn != name:
            self._open_menu(name)

    def _open_menu(self, name):
        self._close_all(clear_btn=False)
        lbl, items, width = self.menu_buttons[name]
        self.active_btn = name

        # Highlight button
        lbl.configure(bg=MHOV, fg=MFG_HI)

        # Position: directly below the button
        lbl.update_idletasks()
        x = lbl.winfo_rootx()
        y = lbl.winfo_rooty() + lbl.winfo_height()

        self.active_dd = DropDown(self.root, items, x, y, self, width)

        # Exit callback: if user clicks an item — handled via on_click below
        # Bind item clicks inside dropdown
        self._bind_dd_clicks(self.active_dd)

    def _bind_dd_clicks(self, dd):
        """Bind click events on all labels in the dropdown to close on click"""
        def on_click(e):
            # Only close if not disabled (check foreground)
            widget = e.widget
            try:
                fg = widget.cget('fg')
                if str(fg) not in (str(IDIS), str(SFG), str(DBD)):
                    self._close_all()
            except tk.TclError:
                pass

        def bind_recursive(widget):
            widget.bind('<Button-1>', on_click, add='+')
            for child in widget.winfo_children():
                bind_recursive(child)

        try:
            bind_recursive(dd.win)
        except tk.TclError:
            pass

    def _close_all(self, clear_btn=True):
        if self.active_dd:
            self.active_dd.destroy()
            self.active_dd = None
        if clear_btn and self.active_btn:
            lbl, _, _ = self.menu_buttons[self.active_btn]
            try:
                lbl.configure(bg=MBG, fg=MFG)
            except tk.TclError:
                pass
            self.active_btn = None

    def _on_root_click(self, e):
        # If click is outside the menubar buttons, close dropdowns
        if self.active_dd:
            widget = e.widget
            # Check if click is inside the dropdown window
            try:
                dd_win = self.active_dd.win
                if widget == dd_win or str(widget).startswith(str(dd_win)):
                    return
            except tk.TclError:
                pass
            # Check if click is on a menu button
            for name, (lbl, _, _) in self.menu_buttons.items():
                if widget == lbl:
                    return
            self._close_all()

    def _on_exit(self):
        self._close_all()
        self.root.destroy()

    # ── Run ──────────────────────────────────────────────────────────
    def run(self):
        self.root.mainloop()


# ════════════════════════════ ENTRY POINT ════════════════════════════
if __name__ == '__main__':
    app = CursorApp()
    app.run()
