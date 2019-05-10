# 发送带附件的邮件
from email import encoders
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
import smtplib
import os.path

From = "songqianqian@jiandan100.cn"

# 多个收件人用逗号隔开
To = "779446928@qq.com, 1220688565@qq.com"

cc = '1220688565@qq.com, 1220688565@qq.com'
# file_name = "report.html"
file_name = "output.avi"


server = smtplib.SMTP("mail.jiandan100.cn")
server.login("songqianqian@jiandan100.cn","Mm9842")   # 仅smtp服务器需要验证时

# 构造MIMEMultipart对象做为根容器
main_msg = MIMEMultipart()

# 构造MIMEText对象做为邮件显示内容并附加到根容器
text_msg = MIMEText("this is a test text to text mime")
main_msg.attach(text_msg)

# 构造MIMEBase对象做为文件附件内容并附加到根容器
contype = 'application/octet-stream'
maintype, subtype = contype.split('/', 1)

# 读入文件内容并格式化
data = open(file_name, 'rb')
file_msg = MIMEBase(maintype, subtype)
file_msg.set_payload(data.read( ))
data.close( )
encoders.encode_base64(file_msg)

# 设置附件头
basename = os.path.basename(file_name)
# 解决中文附件名乱码问题
file_msg.add_header('Content-Disposition', 'attachment', filename=('gbk', '', basename))
main_msg.attach(file_msg)

# 设置根容器属性
main_msg['From'] = From
main_msg['To'] = To

main_msg['Cc'] = cc
main_msg['Subject'] = Header("邮件","utf-8")
main_msg['Date'] = formatdate( )

# 得到格式化后的完整文本
fullText = main_msg.as_string( )

# 用smtp发送邮件
try:
    # 发送给多人、同时抄送给多人，发送人和抄送人放在同一个列表中
    server.sendmail(From, To.split(',') + cc.split(','), fullText)
    print("发送成功！")
except:
    print("发送失败！")
finally:
    server.quit()
