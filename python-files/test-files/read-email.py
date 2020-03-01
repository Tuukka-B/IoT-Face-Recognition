import imaplib
#import credentials

imap_ssl_host = 'imap.gmail.com'
imap_ssl_port = 993
username = 'iot.ttv18s@gmail.com'
password = 'askarisamson'
server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)

server.login(username, password)
server.select('INBOX')

data = server.uid('search',None, '(SUBJECT "2fa")')
server.select('Inbox')
status, data = server.search(None, 'ALL')
for num in data[0].split():
    status, data = server.fetch(num, '(BODY[HEADER.FIELDS (SUBJECT DATE FROM TO)])')
    email_msg = data[0][1]
#print(str(email_msg, 'utf-8'))
e = str(email_msg, 'utf-8')
z = e.split('Subject:')
y = z[1].split('\r')
email_subject = y[0].strip()
print(email_subject)