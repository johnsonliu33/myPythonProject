@echo off

 cd /d D:/AutomaticPublish/AutomaticPublishEClassTeacher 
git pull && git add * && git commit -m "upload publish file EClassTeacher 1.18.19.1905" && git push -u origin master 
