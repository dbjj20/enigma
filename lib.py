from datetime import datetime, timedelta


def add_days_to_unixtime_and_date(days=1, date_format='%Y-%m-%d'):
    date = (datetime.now() + timedelta(days=days)).strftime(date_format)
    unix_time = int(datetime.strptime(date, date_format).strftime("%s"))
    return date, unix_time


def ensure_two_digits(n):
    if len(str(n)) == 2:
        return n
    return "0{n}".format(n=n)
