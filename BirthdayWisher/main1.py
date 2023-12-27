import smtplib
import datetime as dt
import random

MY_EMAIL = "amitgoswami@gmail.com"
MY_PASSWORD = "mraftyarwcvpfdrm"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("C:\Storage\AmitGoswami\Github\PythonCodePractice\BirthdayWisher\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls()
#    connection.login(user=my_email,password=password)
#    connection.sendmail(from_addr=my_email,
#                        to_addrs="amitgoswami1027@gmail.com", 
#                        msg ="Hello")
#    connection.close()

#now = dt.datetime.now()
#year = now.year
#month = now.month
#day_of_week = dt.datetime(year=2020,month=12,day=25)
#print(day_of_week)




