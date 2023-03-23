import smtplib



# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year= 1995, month = 12, day= 15, hour=4)
# print(date_of_birth)


import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()
# print(day_of_week)

filename = "quotes.txt"
with open(filename, encoding="utf-8") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)


my_email = "mathieu993@hotmail.com"
password = "Brochet14?"


def sendmail(my_email, password, quote):
    """send email for quote

    Parameters
    ----------
    my_email : string
        email
    password : string
        secret password
    quote : string
        une quote stylée
    """
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mathieu993@hotmail.com",
            msg=f"Subject:Quote of Thursday\n\n{quote}"
        )
if day_of_week == 3:
    sendmail(my_email, password, quote)