@echo off

 cd /d D:/AutomaticPublish/AutomaticPublishETutorStudent 
git pull && git add * && git commit -m "upload publish file ETutorStudent 2.0.28.1905" && git push -u origin master 
