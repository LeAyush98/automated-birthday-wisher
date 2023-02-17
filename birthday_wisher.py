import pandas
import smtplib
import datetime
import random

# load the csv, get the dictionary

data = pandas.read_csv("data.csv")
main_dict = {value.date:{"name":value.names,"email":value.email} for (key,value) in data.iterrows()}
# get the birthday letter as a string, save in a list. random.random.random.random.choice(list)

bday_list = []
for letter_number in range(1,4):
    file = open(f"birthday_letter{letter_number}.txt", "r")
    string = file.read()
    bday_list.append(string)

bday_text_choice = random.choice(bday_list)
    
# make the final message, use the name in dictionary and add it to the random selected letter from list

now = datetime.datetime.now()
month = now.date().month
day = now.date().day
hour = now.time().hour
minute = now.time().minute
second = now.time().second
time = now.strftime("%H:%M:%S")


for key,value in main_dict.items():
    if key == f"{day}-{month}":
        name = main_dict[key]['name']
        bday_text_choice = bday_text_choice.replace("name", name)

# when date is same as dictionary date, start smtp and send the message to the email in dictionary

EMAIL = "ayu.sharma798@gmail.com"
PASSWORD = "abcde"

for key, value in main_dict.items():
    if key == f"{day}-{month}":
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=f"{main_dict[key]['email']}",
            msg=f"Subject:Happy Birthday!!\n\n{bday_text_choice}"
        )
        connection.close()