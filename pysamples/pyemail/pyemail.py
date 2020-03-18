#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendEmail():
    msg = MIMEText("email content...", "plain", "utf-8")
    msg["From"] = Header("the sender <123456789@qq.com>", "utf-8")
    msg["To"] = Header(
        "the receiver1 <987654321@163.com>, the receiver2 <123456789@qq.com>", "utf-8")
    msg["Subject"] = Header("email subject", "utf-8")

    # the password is the authorization key
    from_addr = "123456789@qq.com"
    password = "********************"
    to_addr1 = "987654321@163.com"
    to_addr2 = "123456789@qq.com"
    smtp_server = "smtp.qq.com"

    # server = smtplib.SMTP(smtp_server, 25)
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr1, to_addr2], msg.as_string())
    server.quit()


def sendHTMLEmail():
    msg = MIMEText("<h1>email head</h1><p>email content</p>", "html", "utf-8")
    msg["From"] = Header("the sender <123456789@qq.com>", "utf-8")
    msg["To"] = Header(
        "the receiver1 <987654321@163.com>, the receiver2 <123456789@qq.com>", "utf-8")
    msg["Subject"] = Header("email subject", "utf-8")

    # the password is the authorization key
    from_addr = "123456789@qq.com"
    password = "********************"
    to_addr1 = "987654321@163.com"
    to_addr2 = "123456789@qq.com"
    smtp_server = "smtp.qq.com"

    # server = smtplib.SMTP(smtp_server, 25)
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr1, to_addr2], msg.as_string())
    server.quit()


def sendAttachmentEmail():
    content = MIMEText(
        '<html><body><h1>email head</h1><p>email content</p><img src="cid:0"></body></html>', "html", "utf-8")
    msg = MIMEMultipart()
    msg.attach(content)
    msg["From"] = Header("the sender <123456789@qq.com>", "utf-8")
    msg["To"] = Header(
        "the receiver1 <987654321@163.com>, the receiver2 <123456789@qq.com>", "utf-8")
    msg["Subject"] = Header("email subject", "utf-8")

    # the password is the authorization key
    from_addr = "123456789@qq.com"
    password = "********************"
    to_addr1 = "987654321@163.com"
    to_addr2 = "123456789@qq.com"
    smtp_server = "smtp.qq.com"

    with open("./timg.jpg", "rb") as f:
        mime = MIMEText(f.read(), "base64", "utf-8")
        mime["Content-Type"] = "text/plain"
        mime["Content-Disposition"] = "attachment; filename=timg.jpg"
        mime["Content-ID"] = "<0>"
        msg.attach(mime)

    # server = smtplib.SMTP(smtp_server, 25)
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr1, to_addr2], msg.as_string())
    server.quit()


if __name__ == "__main__":
    sendEmail()
    sendHTMLEmail()
    sendAttachmentEmail()
