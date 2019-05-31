# 发送带附件的邮件
from email import encoders
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
import smtplib
import os.path


def send_email(report_name):
    sender = "songqianqian@jiandan100.cn"

    # 多个收件人用逗号隔开
    receives = ["779446928@qq.com", "songqianqian@jiandan100.cn"]

    cc = ["1220688565@qq.com", "1220688565@qq.com"]
    file_name = report_name

    server = smtplib.SMTP("mail.jiandan100.cn")
    server.login("songqianqian@jiandan100.cn", "Mm9842")  # 仅smtp服务器需要验证时

    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()

    # 构造MIMEText对象做为邮件显示内容并附加到根容器
    with open(file_name, "rb") as file:
        text_msg = file.read()
    main_msg = MIMEText(text_msg, "html", "utf-8")
    # main_msg.attach(text_msg)

    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    contype = "application/octet-stream"
    maintype, subtype = contype.split("/", 1)

    # 读入文件内容并格式化
    data = open(file_name, "rb")
    file_msg = MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()
    encoders.encode_base64(file_msg)

    # 设置附件头
    basename = os.path.basename(file_name)
    # 解决中文附件名乱码问题
    file_msg.add_header("Content-Disposition", "attachment", filename=("gbk", "", basename))
    main_msg.attach(file_msg)

    # 设置根容器属性
    main_msg["From"] = sender
    main_msg["To"] = ",".join(receives)

    main_msg["Cc"] = ",".join(cc)
    main_msg["Subject"] = Header("邮件", "utf-8")
    main_msg["Date"] = formatdate()

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
    report_path = os.path.join(report_dir, lists[-1])
    send_email(report_path)
