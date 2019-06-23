import os
import glob
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

# 基本情報を入力（gmailをベース）
FROM_ADDRESS = '(from mail_address)'
MY_PASSWORD = '(your gmail password)'
TO_ADDRESS = '(to mail_address)'
BCC = '(bcc mail_address)'
SUBJECT = '(mail subject)'
BODY = '(mail body)'

# メール作成部分
def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg

# メール送信部分
def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


if __name__ == '__main__':
    # 変数準備
    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY
    # 変数準備（ファイルパス）
    file_search_dir = "(file download path)"
    file_search_keyword = "LogSearchResults*.csv"

    # メールログファイル確認
    os.chdir(file_search_dir)
    target_file_list = glob.glob(file_search_keyword)

    # 実メール送信部分
    #
    # ファイルリストが戻って来ている場合は何もしない
    if len(target_file_list) == 0:
        msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
        send(FROM_ADDRESS, to_addr, msg)
