import time
import CBot
import CMail

# Initiate all the bots
# Mail bot
username = "" # Username for email server
password = "" # Password
mail_bot = CMail.CMailResponseBot(username,password)
mail_bot.login()

# Code on where to add tickets for referral to
code = ""
# Bot for sending information to hartbeach page
hartbeach_bot = CBot.CHartbeachBot(code)

# Send 5 requests, accept emails after
for _ in range(5):
    for _ in range(5):
        hartbeach_bot.create_make_request()
    time.sleep(2)
    mail_bot.search_and_click()
