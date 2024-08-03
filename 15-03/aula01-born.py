
import datetime

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute



year_user = int(input("Digite seu ano de nascimento: "))
month_user = int(input("Digite seu mês de nascimento: "))
day_user = int(input("Digite seu dia de nascimento: "))
hour_user = float(input("Digite sua hora de nascimento: "))
minute_user = float(input("Digite seu minuto de nascimento: "))


age = year - year_user

if month < month_user:
    age -= 1
else:
    if month == month_user:
        if day < day_user:
            if hour < hour_user:
                if minute < minute_user:
                    age -= 1


print(f"A sua idade é {age}")



