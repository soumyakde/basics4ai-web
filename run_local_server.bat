@echo off
cd /d C:\Users\soumy\basics4ai_web
call conda activate b4ai_v0
set PORT=8700
python server.py
