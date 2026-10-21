import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(today.year, 4, 9)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_away = next_birthday - today

if next_birthday == today:
    print(bday_messages.random_message)
else:
    print(f"My birthday is {days_away.days} days away!")
