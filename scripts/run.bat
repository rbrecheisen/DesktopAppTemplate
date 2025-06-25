@echo off

setlocal

set /p VERSION=<desktopapptemplate\src\desktopapptemplate\resources\VERSION

set START_DIR=%CD%

if /I "%~1"=="" (

    cd desktopapptemplate
    call briefcase dev

) else if /I "%~1"=="--help" (

    echo "Usage: run.bat [--help|--test|--build|--package]"
    echo ""
    echo "--help    Shows help information"
    echo "--test    Runs tests"
    echo "--build   Builds .exe or .app"
    echo "--package Creates .msi or .dmg installer"
    exit /b 1

) else if /I "%~1"=="--test" (

    cd desktopapptemplate
    call briefcase dev --test

) else if /I "%~1"=="--exe" (

    cd desktopapptemplate
    call briefcase run

) else if /I "%~1"=="--build" (

    rmdir /s /q desktopapptemplate\build
    call python scripts\python\updatetomlversion.py %VERSION%
    call python scripts\python\updatetomlrequirements.py
    cd desktopapptemplate
    call briefcase create
    call briefcase build

) else if /I "%~1"=="--package" (

    cd castoradesktopapptemplatenalytics
    call briefcase package --adhoc-sign
    
)

cd %START_DIR%


endlocal