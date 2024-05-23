import datetime as dt
import os
import smtplib
import random

my_email = os.environ.get("my_email")
password = os.environ.get("password")

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quotes:
        all_quote = quotes.readlines()
        quote = random.choice(all_quote)
        print(quote)
    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="janhavi.rewdekar.t21028@sophiacollege.edu.in",
                            msg=f"Subject: MONDAY MOTIVATION\n\n{quote}"
                            )
