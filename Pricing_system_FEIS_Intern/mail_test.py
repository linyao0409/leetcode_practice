#import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_emails(email, subject, body, attachment_path=None):
    # 你的邮件配置
    sender_email = 'r12723024@g.ntu.edu.tw'
    sender_password = 'Neil19980409'
    smtp_server = 'smtp.example.com'
    smtp_port = 587  # 根据你的邮件提供商设置
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        #for recipient_email in email_series:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email#recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        if attachment_path:
            with open(attachment_path, 'rb') as file:
                part = MIMEApplication(file.read(), Name=attachment_path)
            part['Content-Disposition'] = f'attachment; filename={attachment_path}'
            msg.attach(part)

        server.sendmail(sender_email, email, msg.as_string())
        print(f"Email sent to {email}")

        server.quit()
    except Exception as e:
        print("An error occurred:", str(e))

# 从Excel文件读取邮件地址
#df = pd.read_excel('linyao.xlsx')
#email_series = df['Email']  # 假设Excel文件中的邮箱地址列名为'Email'
target_email = "neil04090409@gmail.com"

subject = '這是一個標題'
body = '這是郵件正文:您好,副檔案是報價單'
attachment_path = 'linyao_number.xlsx'  # 如果有附件，设置附件路径

send_emails(target_email, subject, body, attachment_path)