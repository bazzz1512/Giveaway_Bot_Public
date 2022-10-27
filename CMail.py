import requests
import imaplib
import re
import time


class CMailResponseBot:
    SMTP_PORT = 993

    def __init__(self, username, password):
        self.mail = imaplib.IMAP4_SSL("imap.gmail.com")
        self.username = username
        self.password = password

    def login(self):
        """
        Login to gmail
        :return: None
        """
        self.mail.login(self.username, self.password)

    def search_and_click(self):
        """
        Find all the emails that have verification link and go to that link,
        use VPN, because proxy isnt used to visit verification links
        :return: None
        """
        self.mail.select('inbox')
        # Find mails by Hartbeach and with title for verification
        typ, data = self.mail.search(None, '(FROM "The Hart Beach team" SUBJECT "Verify your email address" UNSEEN)')

        if typ != 'OK':
            raise ValueError("Didn't get my mails back")

        data_ids = data[0].decode("UTF-8").split()

        # Iterate trough all the mails that fit the search criteria and click the link for verification
        for id in data_ids:
            mail_text_last = self.mail.fetch((str(id)), '(RFC822)')
            mail_text_last_string = mail_text_last[1][0][1].decode("UTF-8")

            print(mail_text_last_string)

            url_search = re.findall("(?P<url>https?://[^\s]+)", mail_text_last_string)[1]
            requests.get(url_search, verify=False)
            time.sleep(1)


if __name__ == "__main__":
    bot = CMailResponseBot("", "")
    bot.login()
    bot.search_and_click()


