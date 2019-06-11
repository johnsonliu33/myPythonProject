@echo off

 cd /d D:/AutomaticPublish/AutomaticPublishEClassStudent 
git pull && git add * && git commit -m "upload publish file EClassStudent 1.18.21.1905" && git push -u origin master 
