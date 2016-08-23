import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import utils

msg = MIMEMultipart()

att = MIMEText(open(utils.get_config('zippath','ZIPDIR'), 'rb').read(), 'base64', 'gb2312')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="example.zip"'
msg.attach(att)

msg['to'] = utils.get_config('mail_msg', 'MSG_TO')
msg['from'] = utils.get_config('mail_msg', 'MSG_FROM')
msg['subject'] = utils.get_config('mail_msg', 'MSG_SUBJECT')

try:
    server = smtplib.SMTP()
    server.connect(utils.get_config('mail_pri', 'SERV_CONN'))
    server.login(utils.get_config('mail_pri', 'LOGIN_ID'),
                utils.get_config('mail_pri', 'LOGIN_PWD'))
    server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.quit()
    print 'all send successful'
except Exception, e:  
    print str(e) 