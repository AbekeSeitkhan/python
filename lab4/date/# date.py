# date
import datetime

dt_today = datetime.datetime.today()
dt_num = datetime.datetime.isoweekday(dt_today)
dt_subtr = abs(dt_num - 5)

dates = {1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday", 7 : "Sunday"}

for num in dates:
    if dt_subtr == num:
        print(dates[num])

#2
import datetime

dt_today = datetime.datetime.today()
dt_tod = datetime.datetime.isoweekday(dt_today)
dt_yest = abs(dt_tod - 1)
dt_tom = abs(dt_tod + 1)


dates = {0 : "Sunday", 1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday", 7 : "Sunday"}

for num in dates:
    if dt_yest == num:
        print(dates[num])

for num in dates:
    if dt_tod == num:
        print(dates[num])

for num in dates:
    if dt_tom == num:
        print(dates[num])

#3
import datetime

tod = datetime.datetime.now()
tod = tod.replace(microsecond = 0)
print( tod )

#4
import datetime

dt1 = datetime.datetime(2022, 6, 15, 12, 0, 0)
dt2 = datetime.datetime(2022, 6, 16, 15, 30, 0)

diff = dt2 - dt1
seconds = diff.total_seconds()
print(seconds)