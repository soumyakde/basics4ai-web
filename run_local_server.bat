@echo off
cd /d C:\Users\soumy\basics4ai_web
call conda activate b4ai_v0
python -m http.server 8700
