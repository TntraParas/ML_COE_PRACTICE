from datetime import datetime,timedelta
from helper import print_stars

@print_stars
def que1():
    question = """ Q.1 Print current date and time in Python"""
    print(question)
    print(datetime.now())

@print_stars
def que2():
    question = """Q.2 Convert string into date time object in python"""
    print(question)
    date_str1: str = "2023-10-05"
    date_str2: str = "05 Oct 2023"
    date_str3: str = "2023-10-05 22:15:00"

    print(f"string format = {date_str1} & datetime format = {datetime.strptime(date_str1,'%Y-%m-%d')}")

    print(f"string format = {date_str2} & datetime format = {datetime.strptime(date_str2,'%d %b %Y')}")

    print(f"string format = {date_str3} & datetime format = {datetime.strptime(date_str3,'%Y-%m-%d %H:%M:%S')}")

@print_stars
def que3():
    question = """Q.3 Subtract a week (7 days)  from a given date in Python"""
    print(question)
    try:
        date_str = input("enter date in format of 'yyyy-mm-dd': ")
        date = datetime.strptime(date_str,"%Y-%m-%d")
        ans = date - timedelta(days=7)
        print(f"7 days subtracted = {ans:%Y-%m-%d}")
    except ValueError:
        print("please only enter date in specified format")

@print_stars
def que4():
    question = """Q.4 Find the day of the week of a given date"""
    print(question)
    try:
        date_str = input("enter date in format of 'yyyy-mm-dd': ")
        date = datetime.strptime(date_str,"%Y-%m-%d")
        day_of_the_week = date.strftime("%A")
        print(f"It was {day_of_the_week} on {date:%Y-%m-%d}")
    except ValueError:
        print("please only enter date in specified format")

if __name__ == "__main__":
    que1()
    que2()
    que3()
    que4()
