@echo off
echo parse_video �򵥲��� 2.bat 0.py
set /p url=������ URL: 

%1 parsev --output-easy --make-ffmpeg-list %url%

pause


