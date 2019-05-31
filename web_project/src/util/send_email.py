# 发送带附件的邮件
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import os.path


def send_email(latest_report):
    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()
    # 发送邮件主题和内容
    subject = "按不出的法国"
    content = open(latest_report, "rb").read()
    main_msg.attach(MIMEText(content, "html", "utf-8"))
    # 构造附件内容
    send_file = open(latest_report, "rb").read()
    text = MIMEText(send_file, "base64", "utf-8")
    text["Content-Type"] = "application/octet-stream"
    text["Content-Disposition"] = "attachment;filename='report.html'"

    sender = "songqianqian@jiandan100.cn"
    receives = ["779446928@qq.com", "songqianqian@jiandan100.cn"]
    cc = ["1220688565@qq.com", "1220688565@qq.com"]
    smtpserver = "mail.jiandan100.cn"
    server = smtplib.SMTP(smtpserver)
    # 向服务器标识用户身份
    server.helo(smtpserver)
    # 服务器返回结果确认
    server.ehlo(smtpserver)
    server.login("songqianqian@jiandan100.cn", "Mm9842")  # 仅smtp服务器需要验证时

    # 设置根容器属性
    main_msg["From"] = sender
    main_msg["To"] = ",".join(receives)
    main_msg["Cc"] = ",".join(cc)
    main_msg["Subject"] = Header(subject, "utf-8")
    main_msg["Date"] = formatdate()
    main_msg.attach(text)

    # 得到格式化后的完整文本
    fullText = main_msg.as_string()

    # 用smtp发送邮件
    try:
        # 发送给多人、同时抄送给多人，发送人和抄送人放在同一个列表中
        server.sendmail(sender, receives + cc, fullText)
        print("发送成功！")
    except:
        print("发送失败！")
    finally:
        server.quit()


if __name__ == "__main__":
    report_dir = "../../report"
    lists = os.listdir(report_dir)
    lists.sort(key=lambda x: os.path.getatime(report_dir))  # 按文件时间排序
    latest_report = os.path.join(report_dir, lists[-1])
    send_email(latest_report)
