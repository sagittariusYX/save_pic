From the very beginning, you should create a configure file named "down_img.conf",
which looks like this:
************************************

[log]
LOG_FILE_NAME = down_img.log
LOG_FILE_PATH = down_img.log

[urladdr]
Config URLSAMPLE with url from which you download pictures.
URLSAMPLE = http://www.dbmeizi.com/?p=%d

[downpath]
Config DOWNDIR with dir in which your image downloaded.
DOWNDIR = ../image/

[zippath]
Config ZIPDIR with name.zip in which your zipfile located.
ZIPDIR = ../example.zip

[mail_msg]
Config the three with your message to, from and subject.
MSG_TO = example1@foobar.com
MSG_FROM = example2@foobar.com
MSG_SUBJECT = example subject

[mail_pri]
Config the three with your mail server, mail id and password.
SERV_CONN = mail.example.com
LOGIN_ID = your_id
LOGIN_PWD = your_password


************************************
This python script provide a function to multi-download pictures from specific webUrl.
=======
