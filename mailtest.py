import imaplib
import re
import time

import requests

ORG_EMAIL= "@gmail.com"
FROM_EMAIL= "" + ORG_EMAIL
FROM_PWD= ""
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT= 993

API_KEY = ""
proxies = {
    "http": f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',
    "https": f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001'
}

mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL, FROM_PWD)
mail.select('inbox')
typ, data = mail.search(None, '(FROM "The Hart Beach team" SUBJECT "Verify your email address" UNSEEN)')

if typ != 'OK':
    raise ValueError("Didn't get my mails back")

data_ids = data[0].decode("UTF-8").split()

for id in data_ids:
    mail_text_last = mail.fetch((str(id)), '(RFC822)')
    mail_text_last_string = mail_text_last[1][0][1].decode("UTF-8")

    print(mail_text_last_string)


    url_search = re.findall("(?P<url>https?://[^\s]+)", mail_text_last_string)[1]
    requests.get(url_search)
    time.sleep(1)

mail.close()
print(url_search)
