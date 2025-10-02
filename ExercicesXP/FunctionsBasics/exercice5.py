#Write a function print_days that prints the days of the week (Sunday, Monday, Tuesday, etc.) using a loop.

weekdays = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def print_days():
    global weekdays
    for i in weekdays:
        print(i)

print_days()