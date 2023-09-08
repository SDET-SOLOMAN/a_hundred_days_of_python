import requests
from datetime import datetime
import smtplib
from random import choice, shuffle
import pandas
from numpy import arange

from my_password import my_pass

# This app finds if ISS is over your head and emails you notification to LOOK UP
# It uses API call to ISS and API call to your long and latit location to find out Sunset and Sunrise
# Then it converts it to 24 hr, and uses daytime to match with ur PC/LAPTOP current time
# and then uses conditional logic to email you if your position is within +5 or -5 degrees of the ISS position.

MY_LAT = 35.7915
MY_LONG = -78.781120

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_longitude, iss_latitude)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunrise"].split("T")[1].split(":")[0])

time_now = datetime.now()


def check_time():
    if time_now.hour >= sunset or sunrise < time_now.hour:
        return True
    return False


def check_distance():
    if iss_latitude in arange(MY_LAT - 5, MY_LAT + 6) and iss_longitude in arange(MY_LONG - 5, MY_LONG + 6):
        return True
    return False


def run_until():

    while check_time() and check_distance():

        if datetime.now().second in range(30, 32):
            my_email = "solomansdet@gmail.com"
            key_pass = my_pass
            with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
                connect.starttls()
                connect.login(user=my_email, password=key_pass)
                connect.sendmail(from_addr=my_email, to_addrs="SuperFakeEMail2918282881@hotmail.com",
                                 msg=f"Subject:Look UP \n\n"
                                     f"ISS is right on top of you!!!")
                print("Email Sent")

run_until()
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
