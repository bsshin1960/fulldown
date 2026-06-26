@echo off
:: 깃허브 페이지에 배포된 온라인 동적 메뉴를 주소창, 탭, 즐겨찾기 없이 앱 형태로 실행합니다.
where chrome >nul 2>nul
if %errorlevel% equ 0 (
    start chrome --app="https://bsshin1960.github.io/fulldown/index_dynamic.html"
) else (
    start msedge --app="https://bsshin1960.github.io/fulldown/index_dynamic.html"
)
