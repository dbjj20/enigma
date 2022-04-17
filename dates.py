import datetime
import calendar
from lib import add_days_to_unixtime_and_date, ensure_two_digits

year = 2022
day = 1
month = 1

date1 = datetime.date(year, month, day)
days_in_year = int((datetime.date(year, 12, 31)-date1).days)
DAYS_IN_YEAR = int((datetime.date(year, 12, 31)-date1).days)

times_x_in_year = 0  # x = 68
time_computed_date = 0
last_day_in_month = calendar.monthrange(year, month)[1]
main_result = []


def set_month():
    return calendar.monthrange(year, month)[1]


dates = add_days_to_unixtime_and_date(
    date_format=f'{year}-{ensure_two_digits(month)}-{ensure_two_digits(day)}'
    )

inner_exec = 0
while day <= last_day_in_month:
    inner_exec = inner_exec + 1
    result = int(int(str(year)[0:2]) + int(str(year)[2:]) + day + month)

    print('operation', f'{str(year)[0:2]} + {str(year)[2:]} + {day} + {month}')
    print('result', result)
    print('day', day)
    print('last day in month', last_day_in_month)
    print('month', month)
    print('days in year', days_in_year)
    print('year', year)
    print('------------------------------------------------------')

    if result == 68:
        times_x_in_year = times_x_in_year + 1
        main_result.append(f'{str(year)[0:2]}-{str(year)[2:]}-{day}-{month}={result}')

    time_computed_date = time_computed_date + 1

    if last_day_in_month == day:
        month = month + 1
        day = 1
        # print('execute new month')
        if month > 12:
            break
        else:
            last_day_in_month = set_month()
    else:
        day = day + 1

    if days_in_year == 0:
        break
    days_in_year = days_in_year - 1
    # print('inner_exec', inner_exec)

    if inner_exec == DAYS_IN_YEAR:
        break

# print('\n')
print("times_x_in_month ===> ", times_x_in_year)
print("time_computed_date ===> ", time_computed_date)
print("operations with 68 ====>", main_result)