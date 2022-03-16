@echo off

call %~dp0tgBot\venv\Scripts\activate

cd %~dp0tgBot

set TOKEN=5150149062:AAGWhhdcohn2qfnne2RNEHnVf6Xrf8Ik_FA

python bot_tg.py

pause 