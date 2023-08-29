datav1 = []

# v1 my way
with open('weather_data.csv') as file:
    x = file.read().split("\n")
    datav1.append(x)
print(datav1)

# another way is using.readlines()
# -----------------------------

# csv  way:
import csv

d = []
grab_temp = []

with open('weather_data.csv') as file:
    datas = csv.reader(file)
    for data in datas:
        d.append(data)
    for char in d[1:]:
        grab_temp.append(int(char[1]))
    print(grab_temp)

# ------------------
# using pandas

import pandas

data = pandas.read_csv('weather_data.csv')

# getting average
temp_list = data['temp'].to_list()
print(f"the average temp is {round( sum(temp_list) / len(temp_list), 2)}")

# average panda way
print(data['temp'].mean())

# ------------

a = data.temp.max()

print(data[data.temp == a].day) # or data,temp.max()]
# --------

tuesday = data[data.day == 'Tuesday']
print(tuesday.condition)
# ------

# calculating Monday tempo and converting it from Celsius to F

Monday = data[data.day == 'Monday']
# Monday = (Monday.temp.to_list()[0])
Monday = Monday.temp[0]
print(f'Monday\'s temp in celsius is {Monday} which is equal to {round((Monday * (9/5)) + 32, 3)} in Fahrenheit')
# --------------

# create csv using pandas

just_dict = {
    'students': ["mike", 'sdet', 'solo'],
    'ssalaries': ['120k', '135k', '185k']
}

new_data = pandas.DataFrame(just_dict)
print(new_data)
new_data.to_csv('salaries_csv.csv')