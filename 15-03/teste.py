
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

# Verificando se o aniversário já ocorreu este ano
if month < month_user or (month == month_user and day < day_user):
    age -= 1
elif month == month_user and day == day_user:
    # Se o aniversário for hoje, verificar se já passou da hora e minuto de nascimento
    if hour < hour_user or (hour == hour_user and minute < minute_user):
        age -= 1

# Exibindo a idade calculada

print(f"A sua idade é {age}")