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
    ###########################################
    # ### 发送邮件主题和内容
    subject = "按不出的法国"
    main_msg.attach(MIMEText("【邮件自动发送，无需回复】\n", "html", "utf-8"))
    with open(latest_report, "rb")as file:
        content = file.read()
    main_msg.attach(MIMEText(content, "html", "utf-8"))
    ###########################################
    # ### 构造附件内容
    with open(latest_report, "rb")as file:
        send_file = file.read()
    text = MIMEText(send_file, "base64", "utf-8")
    # 附件设置内容类型，方便起见，设置为二进制流
    text["Content-Type"] = "application/octet-stream"
    # 设置附件头，添加文件名
    text["Content-Disposition"] = "attachment;filename={}".format("report.html")
    main_msg.attach(text)
    ###########################################
    sender = "songqianqian@jiandan100.cn"
    receives = ["779446928@qq.com", "songqianqian@jiandan100.cn"]
    cc = ["1220688565@qq.com", "1220688565@qq.com"]
    smtpserver = "mail.jiandan100.cn"

    #############################################
    # 设置根容器属性
    main_msg["From"] = sender
    main_msg["To"] = ",".join(receives)
    main_msg["Cc"] = ",".join(cc)
    main_msg["Subject"] = Header(subject, "utf-8")
    main_msg["Date"] = formatdate()

    # 得到格式化后的完整文本
    fullText = main_msg.as_string()

    # ###用smtp发送邮件
    try:
        server = smtplib.SMTP(smtpserver)
        server.login("songqianqian@jiandan100.cn", "Mm9842")
        # 发送给多人、同时抄送给多人，发送人和抄送人放在同一个列表中
        server.sendmail(sender, receives + cc, fullText)
        print("发送成功！")
        server.quit()
    except Exception as e:
        print("发送失败！\n", e)


if __name__ == "__main__":
    report_dir = "../../report"
    lists = os.listdir(report_dir)
    lists.sort(key=lambda x: os.path.getatime(report_dir))  # 按文件时间排序
    latest_report = os.path.join(report_dir, lists[-1])
    send_email(latest_report)
