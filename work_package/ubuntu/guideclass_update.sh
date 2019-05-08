#!/bin/sh

echo =============1==============

rm -r GuideClass

echo $?  rm project

# -q 隐藏解压日志
unzip -q GuideClass-*.zip && rm GuideClass-*.zip

echo $?  unzip project 

mv GuideClass-* GuideClass

echo $?  rename project

echo =============2==============  

#cd GuideClass/ && npm811 i
cp -rf node_modules/ ./GuideClass/

echo $? npm811 install

echo =============3==============  
#替换的内容有/时，用?分割
sudo sed -i "s?172.16.0.166/guideclass?172.16.0.166/guideclass_ceshi?" ./GuideClass/config/index.js

echo $? update defaultMongodb 

sudo sed -i "s/port: 9211/port: 9212/" ./GuideClass/config/index.js

echo $?  update uplandService port at 9212
#s前加行号，只替换该行的内容
#sed -i "44s?http://172.16.0.131:3100/?https://as.jd100.com/?" ./GuideClass/config/index.js

#echo $? update kpTestServer 

echo =============5==============  

echo $? update time:
date +"%Y-%m-%d %T"
