## string exercise
from helper import print_stars


@print_stars
def que1():
    question = """Q. Create a string made of the first, middle and last character"""
    print(question)
    string = input("input any string: ")
    n = len(string)
    if n == 0:
        print("don't just hit enter,please enter an actual string")
        return
    first, last = 0, n - 1
    middle = (n // 2) - 1
    if n % 2 == 1:
        # handle odd number of characters in string
        middle += 1

    ans = string[first] + string[middle] + string[last]
    print(f"the string after joining first,middle and last is = {ans}")


@print_stars
def que2():
    question = """Q. Create a string made of the middle three characters"""
    print(question)
    string = input("input any string: ")
    n = len(string)
    if n == 0:
        print("don't just hit enter,please enter an actual string")
        return
    first, middle, last = 0, (n // 2), n
    ans = string[first] + string[middle] + string[last]
    print(f"the string after joining first,middle and last is = {ans}")


if __name__ == "__main__":
    que1()
