#!/bin/sh

if [ -n "$1" ]; then
branch="branches/$1"
else 
branch='trunk'
fi
echo $branch

cd /usr/ET/project/upland/src/
rm -R domain
svn export svn://192.168.1.183/web/easyweb/${branch}/src/domain /usr/ET/project/upland/src/domain  --username webpub --password webpub123
rm -R logic
svn export svn://192.168.1.183/web/easyweb/${branch}/src/logic /usr/ET/project/upland/src/logic --username webpub --password webpub123
rm -R lib
svn export svn://192.168.1.183/web/easyweb/${branch}/src/lib /usr/ET/project/upland/src/lib --username webpub --password webpub123
rm -R sqlmap
svn export svn://192.168.1.183/web/easyweb/${branch}/src/sqlmap /usr/ET/project/upland/src/sqlmap --username webpub --password webpub123
rm -R webservice
svn export svn://192.168.1.183/web/easyweb/${branch}/src/webservice /usr/ET/project/upland/src/webservice --username webpub --password webpub123
rm -R tools
svn export svn://192.168.1.183/web/easyweb/${branch}/src/tools /usr/ET/project/upland/src/tools --username webpub --password webpub123

rm -r thriftPackages
svn export svn://192.168.1.183/web/easyweb/${branch}/src/thriftPackages  /usr/ET/project/upland/src/thriftPackages --username webpub --password webpub123

cd /usr/ET/project/upland/src/portal/
rm -R client
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/client /usr/ET/project/upland/src/portal/client --username webpub --password webpub123
rm -R config
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/config /usr/ET/project/upland/src/portal/config --username webpub --password webpub123
rm -R controller
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/controller /usr/ET/project/upland/src/portal/controller --username webpub --password webpub123
rm -R data
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/data /usr/ET/project/upland/src/portal/data --username webpub --password webpub123
rm -R include
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/include /usr/ET/project/upland/src/portal/include --username webpub --password webpub123
rm -R service
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/service /usr/ET/project/upland/src/portal/service --username webpub --password webpub123
rm -R view
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/view /usr/ET/project/upland/src/portal/view --username webpub --password webpub123
rm -R template
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/template /usr/ET/project/upland/src/portal/template --username webpub --password webpub123
rm -R api
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/api /usr/ET/project/upland/src/portal/api --username webpub --password webpub123
rm -R agent
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/agent /usr/ET/project/upland/src/portal/agent --username webpub --password webpub123
rm -R phone
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/phone /usr/ET/project/upland/src/portal/phone --username webpub --password webpub123

cd /usr/ET/project/upland/src/portal/tmp/compile/
rm *

cd /usr/ET/project/upland/src/portal/www/
rm -R templates
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/www/templates /usr/ET/project/upland/src/portal/www/templates --username webpub --password webpub123
rm -R app
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/www/app /usr/ET/project/upland/src/portal/www/app --username webpub --password webpub123
rm -R js
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/www/js /usr/ET/project/upland/src/portal/www/js --username webpub --password webpub123
rm -R popbox
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/www/popbox /usr/ET/project/upland/src/portal/www/popbox --username webpub --password webpub123
rm -R css
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/www/css /usr/ET/project/upland/src/portal/www/css --username webpub --password webpub123
rm -R html
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/www/html /usr/ET/project/upland/src/portal/www/html --username webpub --password webpub123
#rm -R images
svn export --force svn://192.168.1.183/web/easyweb/${branch}/src/portal/www/images/ /usr/ET/project/upland/src/portal/www/images --username webpub --password webpub123
#rm -R data
svn export --force svn://192.168.1.183/web/easyweb/${branch}/src/portal/www/data/ /usr/ET/project/upland/src/portal/www/data --username webpub --password webpub123
rm -R studycenter
svn export svn://192.168.1.183/web/easyweb/${branch}/src/portal/www/studycenter /usr/ET/project/upland/src/portal/www/studycenter --username webpub --password webpub123

cd /usr/ET/project/upland/
rm -r /usr/ET/project/upland/vendorsrc
svn export svn://192.168.1.183/web/easyweb/${branch}/vendorsrc /usr/ET/project/upland/vendorsrc --username webpub --password webpub123


cd /usr/ET/project/upland/src/
#rm -r /usr/ET/project/upland/src/webdatamanager
#svn export ${rev} svn://192.168.1.183/web/easyweb/${branch}/src/webdatamanager /usr/ET/project/upland/src/webdatamanager --username webpub --password webpub123
#修改数据库  开发→测试
sed -i "s/192.168.1.111/192.168.20.156/g" ./webservice/db.config.inc

sed -i "s/192.168.1.111/192.168.20.156/g" ./portal/config/db.config.inc

#mkdir /usr/ET/project/upland/src/portal/tmp/compile

#修改支付宝、微信支付价格为1分钱
cd /usr/ET/project/upland/src/portal/controller/
sed -n '/\"total_fee\"/s/\$total_fee/0.01/p' pay.php
sed -i '/\"total_fee\"/s/\$total_fee/0.01/' pay.php

#网站后台
#chmod -R 777 /usr/ET/project/upland/src/webdatamanager
#cd /usr/ET/project/upland/src/webdatamanager/config
#sed -i '0,/web_app/s/1.111/20.156/' db.config.inc

chown -R ubuntu /usr/ET/project/upland
chmod -R 777 /usr/ET/project/upland
