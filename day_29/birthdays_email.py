import smtplib
import datetime as dt

my_email = "solomansdet@gmail.com"
key_pass = "bgfezzjcczjevpis"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=key_pass)
connection.sendmail(from_addr=my_email, to_addrs="kavkazus@hotmail.com",
                    msg="Subject:Hello\n\n"
                        "This is the body of the email")
connection.close()