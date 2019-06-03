# 发送带附件的邮件
from email import encoders
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
import smtplib
import os.path


class EmailUtil:
    def __init__(self, From, To, Cc):
        self.From = From
        self.To = To
        self.Cc = Cc

    def email_func(self, file_name):
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
        file_msg.set_payload(data.read())
        data.close()
        encoders.encode_base64(file_msg)

        # 设置附件头
        basename = os.path.basename(file_name)
        # 解决中文附件名乱码问题
        file_msg.add_header('Content-Disposition', 'attachment', filename=('gbk', '', basename))
        main_msg.attach(file_msg)

        # 设置根容器属性
        main_msg['From'] = self.From
        main_msg['To'] = self.To
        main_msg['Cc'] = self.Cc
        main_msg['Subject'] = Header("邮件", "utf-8")
        main_msg['Date'] = formatdate()

        # 得到格式化后的完整文本
        fullText = main_msg.as_string()
        return fullText

    def main(self, fullText):
        try:
            server = smtplib.SMTP("mail.jiandan100.cn")
            server.login("songqianqian@jiandan100.cn", "Mm9842")
            # 发送给多人、同时抄送给多人，发送人和抄送人放在同一个列表中
            server.sendmail(self.From, self.To.split(',') + self.Cc.split(','), fullText)
            print("发送成功！")
            server.quit()
        except Exception as e:
            print("发送失败！\n", e)


if __name__ == '__main__':
    From = "songqianqian@jiandan100.cn"
    To = "779446928@qq.com, songqianqian@jiandan100.cn"  # 多个收件人用逗号隔开
    Cc = '1220688565@qq.com, 1220688565@qq.com'
    em_util = EmailUtil(From, To, Cc)
    file_name = "2019_06_02 17_37_51-report.html"
    # file_name = "中文.avi"
    fullText = em_util.email_func(file_name)
    em_util.main(fullText)
