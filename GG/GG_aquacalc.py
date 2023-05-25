from datetime import date
#import datatime

import sys
args = sys.argv

date_str = args[1]

y = date_str[0:4]
m = date_str[4:6]
d = date_str[6:8]

y = int(y)
m = int(m)
d = int(d)


dt = date(y, m, d)
# print(y)
# print(m)
# print(d)
# print(date_str[1:5])

# dt = date(int(args[1]))
# #dt = datetime.date(2022, 6, 4)

# print(dt.strftime("%a"))

# dtlist = [args[1]]


# y = dtlist[1:4]
# m = dt[5:6]
# d = dt[7:8]

# dt = date(int(y, m, d))

# print(dt.strftime("%a"))

adult = int(args[2])
child = int(args[3])

weekday = dt.strftime("%a")
# dt.strftime("Sat") # => "Sat"
# dt.strftime("%a")
if weekday == "Sat" or weekday == "Sun":
    sum = 2400 * adult + 1500 * child
    print(sum)
else:
    sum = 2000 * adult + 1200 * child
    print(sum)