# ugly AF solution
from time import time
start = time()
counter = 0

day_index = 1
weekdays_index = 3 # jan 1st 1901 was tuesday,  "my week" starts with sunday hence 3
month_index = 1
year_index = 1901

while year_index < 2001:
    # new year
    if day_index == 32 and month_index == 12:
        year_index += 1
        month_index = 1
        day_index = 1

    # new month
        # 31
    if month_index in [1, 3, 5, 7, 8, 10, 12] and day_index == 32:
        month_index += 1
        day_index = 1

        # 30
    if month_index in [4, 6, 9, 11] and day_index == 31:
        month_index += 1
        day_index = 1

        # feb exceptions
    if month_index == 2:
        if year_index % 4 == 0:
            if day_index == 30:
                month_index += 1
                day_index = 1
        else:
            if day_index == 29:
                month_index += 1
                day_index = 1

    # counter check
    if weekdays_index == 1 and day_index == 1:
        counter += 1

    day_index += 1
    weekdays_index += 1

    # new week
    if weekdays_index == 8:
        weekdays_index = 1
stop = time()
print(counter, stop - start)

