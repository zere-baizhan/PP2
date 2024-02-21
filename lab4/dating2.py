#ex1
"""import datetime

x = datetime.datetime.now()
z = x - datetime.timedelta(days=5)

print(z)"""

#ex2
"""import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow=today + datetime.timedelta(days=1)

print("today= ",today)
print("yesterday= ",yesterday)
print("tomorrow= ",tomorrow)"""

#ex3
"""from datetime import date
today=date.today()
print(today)"""

#ex4
from datetime import * 


year1 = int(input('Enter a year: '))
month1 = int(input('Enter a month: '))
day1 = int(input('Enter a day: '))

date1 = date(year1, month1, day1)

year2 = int(input('Enter a year: '))
month2 = int(input('Enter a month: '))
day2 = int(input('Enter a day: '))

date2 = date(year2, month2, day2)

difference = date2 - date1

byseconds = difference.total_seconds()
print(byseconds)