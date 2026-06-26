@echo off
:: 크롬 브라우저가 있으면 크롬의 app 모드로 실행, 없으면 엣지 브라우저의 app 모드로 실행합니다.
:: (app 모드는 주소창, 탭, 즐겨찾기 창 없이 깔끔하게 웹페이지를 보여주는 모드입니다.)

where chrome >nul 2>nul
if %errorlevel% equ 0 (
    start chrome --app="%~dp0index.html"
) else (
    start msedge --app="%~dp0index.html"
)
