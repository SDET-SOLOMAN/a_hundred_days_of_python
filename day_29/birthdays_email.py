import smtplib
from random import choice, shuffle
import datetime as dt
import pandas

my_email = "solomansdet@gmail.com"
key_pass = ""

with open("./password") as pass_word:
    key_pass = pass_word.read()

month = dt.datetime.now().month
day = dt.datetime.now().day
list_of_letters = choice(["./letter_templates/letter_1.txt",
                          "./letter_templates/letter_2.txt",
                          "./letter_templates/letter_3.txt"])

birthdays = pandas.read_csv("./birthdays.csv")
new_birthdays = {(v.month, v.day): {'name': v['name'], 'email': v.email} for k, v in birthdays.iterrows()}

if new_birthdays.get((month, day)):

    print("EMAIL SENT")

    with open(list_of_letters, mode='r') as letter:
        content = letter.read()
        name = new_birthdays[(month, day)]['name']
        email = new_birthdays[(month, day)]['email']
        text_name = content.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
            connect.starttls()
            connect.login(user=my_email, password=key_pass)
            connect.sendmail(from_addr=my_email, to_addrs=email,
                             msg=f"Subject:Happy Birthday {name}\n\n"
                                 f"{text_name}")







# my_email = ""
# key_pass = ""
#
# with open("./password") as pass_word:
#     key_pass = pass_word.read()
#
# birthdays = pandas.read_csv("./birthdays.csv").to_dict(orient='records')
# print(birthdays)


# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=key_pass)
# connection.sendmail(from_addr=my_email, to_addrs="kavkazus@hotmail.com",
#                     msg="Subject:Hello\n\n"
#                         "This is the body of the email")
# connection.close()


# day = dt.datetime.now().weekday()
#
# current_day = 1
#
# if day == current_day:
#     my_list = None
#     with open("./quotes.txt", mode='r') as quotes:
#         # my_list = list(quotes)
#         quote = quotes.readlines()
#         my_list = choice(quote)
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
#         connect.starttls()
#         connect.login(user=my_email, password=key_pass)
#         connect.sendmail(from_addr=my_email, to_addrs="kavkazus@hotmail.com",
#                          msg=f"Subject:Hello\n\n"
#                              f"{my_list}")
