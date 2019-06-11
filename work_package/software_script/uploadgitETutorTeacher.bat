@echo off

 cd /d D:/AutomaticPublish/AutomaticPublishETutorTeacher 
git pull && git add * && git commit -m "upload publish file ETutorTeacher 2.0.27.1905" && git push -u origin master 
