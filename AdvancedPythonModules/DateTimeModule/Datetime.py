
# import datetime

from datetime import date, datetime

# from datetime import date
# from datetime import time

now = datetime.now()
now2 = datetime.today()

result = datetime.now()
result = now.year
result = now.month
result = now.day
result = now.hour
result = now.minute
result = now.second
result = datetime.ctime(now) # Fri Aug 19 10:33:18 2022
result = datetime.strftime(now,'%Y')
result = datetime.strftime(now,'%X')
result = datetime.strftime(now,'%d') #19
result = datetime.strftime(now,'%A') #Friday

t = '21 Nisan 2019'

gun, ay, yil = t.split()
print(gun, ay, yil)

t2 = '15 April 2019 hour 10:12:30'

dt = datetime.strptime(t2, '%d %B %Y hour %H:%M:%S')

print(dt)


birthday = datetime(2001, 10, 7,12,30,24)

result2 = datetime.timestamp(birthday)

print(result2)

print(birthday)

print(result)


















