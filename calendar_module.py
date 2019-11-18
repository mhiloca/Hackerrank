import calendar

weeknames = (
    'MONDAY', 'TUESDAY', 'WEDNESDAY',
    'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'
)

d = input()
date = list(map(int, d.split()))
print(weeknames[calendar.weekday(date[2], date[0], date[1])])