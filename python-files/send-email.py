# smtplib module send mail

import smtplib

TO = 'samsonitto@gmail.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'

# Gmail Sign In
gmail_sender = 'iot.ttv18s@gmail.com'
gmail_passwd = 'askarisamson'
print('1')
#server = smtplib.SMTP('smtp.gmail.com', 587)
server = smtplib.SMTP_SSL('smtp.gmail.com','465')
print('2')

#server.starttls()
print('3')
server.ehlo()
print('4')
server.login(gmail_sender, gmail_passwd)
print('5')

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()