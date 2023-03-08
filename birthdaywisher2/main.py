import pandas
import datetime as dt
import smtplib

data = pandas.read_csv("birthdays.csv")
data = data.to_dict(orient="records")
print(data)

current_date = dt.datetime.now()

for item in data:
    if current_date.month == item["Month"] and current_date.day == item["Day"]:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="freshmark320@gmail.com", password="jzunuyfbtqauqonp")
            connection.sendmail(from_addr="freshmark320@gmail.com",
                                to_addrs="guluzade.muhammad@metu.edu.tr",
                                msg=f"Subject: Birthday\n\nIt's {item['Name']}'s birthday today")