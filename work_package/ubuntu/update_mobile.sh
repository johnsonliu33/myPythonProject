#!/bin/sh

rm -rf /usr/ET/project/web-mobile
unzip /usr/ET/project/web-mobile-*.zip
rm /usr/ET/project/web-mobile-*.zip
mv /usr/ET/project/web-mobile-* web-mobile
#mv mobileweb /usr/public/
chown -R ubuntu /usr/ET/project/web-mobile/
chmod -R 777 /usr/ET/project/web-mobile/
#chmod -R 777 /usr/public/mobileweb
