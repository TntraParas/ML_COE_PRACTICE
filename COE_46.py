from datetime import datetime

def printStars(func):
    def preety_answer_printer():
        print("\n*******************\n")
        func()
        print("\n*******************\n")
    return preety_answer_printer

@printStars
def que1():
    question = """ Q.1 Print current date and time in Python"""
    print(question)
    print(datetime.now())

@printStars
def que2():
    question = """Q.2 Convert string into date time object in python"""
    print(question)
    date_str1: str = "2023-10-05"
    date_str2: str = "05 Oct 2023"
    date_str3: str = "2023-10-05 22:15:00"

    print(f"string format = {date_str1} & datetime format = {datetime.strptime(date_str1,'%Y-%m-%d')}")

    print(f"string format = {date_str2} & datetime format = {datetime.strptime(date_str2,'%d %b %Y')}")

    print(f"string format = {date_str3} & datetime format = {datetime.strptime(date_str3,'%Y-%m-%d %H:%M:%S')}")

@printStars
def que3():
    question = """Subtract a week (7 days)  from a given date in Python"""
    print(question)

que1()
que2()
