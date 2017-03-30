days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
leap_year = lambda year: bool(year % 4) ^ bool(year % 100)

ly = lambda year: not year % 4 and not (not year % 400) ^ (not year % 100)

def mondays_on_first_of_month(start_year, end_year):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0
    date = {
        'year': start_year,
        'month': 0,
        'day': 0,
        'weekday': 0
    }
    # increment = lambda count, weekday, day: count if weekday+day else count+1
    def next_day():
        months[1] = 29 if ly(date['year']) else 28
        date['weekday'] = (date['weekday'] + 1) % 7
        date['day'] = (date['day'] + 1) % months[date['month']]
        if date['day'] == 0: date['month'] = (date['month'] + 1) % 12
        if date['day'] == 0 and date['month'] == 0: date['year'] += 1
        print(date['year'], date['month'], date['day'], date['weekday'], count)

    while True:
        if date['year'] == end_year: break
        if date['day'] == 0 and date['weekday'] == 0 and date['year'] < end_year: count += 1
        next_day()

    return count

print(mondays_on_first_of_month(1900, 2001) - mondays_on_first_of_month(1900, 1901))
