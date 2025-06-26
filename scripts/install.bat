@echo off

setlocal

pip install --upgrade pip
pip install -r requirements.txt
cd desktopapptemplate
call briefcase create

endlocal