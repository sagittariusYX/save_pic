import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import utils

msg = MIMEMultipart()

att = MIMEText(open(utils.get_config('zippath','ZIPDIR'), 'rb').read(), 'base64', 'gb2312')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="example.zip"'
msg.attach(att)

msg['to'] = '14210240004@fudan.edu.cn'
msg['from'] = '14210240102@fudan.edu.cn'
msg['subject'] = 'mail test'

try:
    server = smtplib.SMTP()
    server.connect('mail.fudan.edu.cn')
    server.login('14210240102','lmdrxxnmcjkqw')
    server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.quit()
    print 'send successful'
except Exception, e:  
    print str(e) 