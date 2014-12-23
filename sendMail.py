import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import utils

msg = MIMEMultipart()

att2 = MIMEText(open(utils.get_config('zippath','ZIPDIR'), 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="example.zip"'
msg.attach(att2)

msg['to'] = '983999589@qq.com'
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