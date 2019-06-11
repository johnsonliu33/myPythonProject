@echo off

cd /d D:\AutomaticPublishTest
git pull && git add * && git commit -m "%1%" && git push 
