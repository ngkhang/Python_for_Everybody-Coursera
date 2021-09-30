"""
Assignment 5.2

    Write a program that repeatedly prompts a user for integer numbers until\
        the user enters 'done'. Once 'done' is entered, print out the largest
        and smallest of the numbers. If the user enters anything other than a
        valid number catch it with a try/except and put out an appropriate
        message and ignore the number. Enter 7, 2, bob, 10, and 4 and match
        the output below.

"""

largest = None
smallest = None
tmp = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num1 = int(num)
    except:
        print('Invalid input')
    if largest is None:
        largest = num1
        continue
    elif smallest is None:
        smallest = num1
        continue


    if largest < smallest:
        tmp = largest
        largest = smallest
        smallest = tmp

    if num1 > largest:
        largest = num1
    elif num1 < smallest:
        smallest = num1

print("Maximum is", largest)
print("Minimum is", smallest)