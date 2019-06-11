@echo off

 cd /d D:/AutomaticPublish/AutomaticPublishETClient 
git pull && git add * && git commit -m "upload publish file EasyClient 3.41.10.1902" && git push -u origin master 
