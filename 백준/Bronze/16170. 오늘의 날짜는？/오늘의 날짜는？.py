from datetime import datetime

now = datetime.now()

date = str(now.date())

year, month, day = date.split('-')

print(year)
print(month)
print(day)