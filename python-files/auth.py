import smtplib
import imaplib
import random


def key(): 
    key = ''
    for x in range(10):
      key += str(random.randint(0,9))
    return key

def sendEmail(email, key):
    print(("Authenticating user of the address {}...").format(email))
    TO = email
    SUBJECT = 'IOT 2FA'
    TEXT = key

    # Gmail Sign In
    gmail_sender = 'iot.ttv18s@gmail.com'
    gmail_passwd = 'askarisamson'
    #print('1')
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    server = smtplib.SMTP_SSL('smtp.gmail.com','465')
    #print('2')

    #server.starttls()
    #print('3')
    server.ehlo()
    #print('4')
    server.login(gmail_sender, gmail_passwd)
    #print('5')

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        #print ('email sent')
    except:
        pass
        #print ('error sending mail')
    server.quit()

def readEmail(key):
    imap_ssl_host = 'imap.gmail.com'
    imap_ssl_port = 993
    username = 'iot.ttv18s@gmail.com'
    password = 'askarisamson'
    server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)

    server.login(username, password)
    
    counter = 0
    while True:
        server.select('INBOX')

        data = server.uid('search',None, ('SUBJECT {}').format(key))
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
        #print(email_subject)
        if email_subject==str(key):
            print('Authentication confirmed')
            return True
        elif counter > 9:
            print('Authentication failed')
            print(counter)
            return False
            
        counter += 1
        print("counter: ",counter)

#key = key()
#sendEmail('samsonitto@gmail.com', key)

#lol = input("Done?")

#readEmail(key)
