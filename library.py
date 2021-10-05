import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os


def mail(from_user,from_password,to,subject,text):
    msg = MIMEMultipart()
    msg["From"] = from_user
    msg["To"] = to 
    msg["Subject"] = subject

    msg.attach(MIMEText(text))

    mailServer = smtplib.SMTP("smtp.gmail.com",587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(from_user, from_password)
    mailServer.sendmail(from_user, to, msg.as_string())
    mailServer.close() 
