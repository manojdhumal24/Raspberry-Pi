import time
import os
import glob
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText
import subprocess
import sys
import raspberry

gmail_user = raspberry.gmail_user
gmail_pwd = raspberry.gmail_pwd
FROM = raspberry.gmail_user
TO = ['raspberrypi4b@gmail.com','raspberry@iotmail.com'] #must be a list
message = "Hello Raspberry Pi and IOT, welcome u all"
time.sleep(1)
msg = MIMEMultipart()
time.sleep(1)
msg['Subject'] ="Welcome Message"
body=message
msg.attach(MIMEText(body,'plain'))
time.sleep(1)
try:
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        print ("smtp.gmail")
        server.ehlo()
        print ("ehlo")
        server.starttls()
        print ("starttls")
        server.login(gmail_user, gmail_pwd)
        print ("reading mail & password")
        server.sendmail(FROM, TO, msg.as_string())
        print ("from")
        server.close()
        print ('successfully sent the mail')
except:
        print ("failed to send mail")


