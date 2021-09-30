'''
Assignment 7.2

    You'll complete this item using the course's autograders. Open the tool using the button below.

    Write a program that prompts for a file name, then opens that file and reads through the file,\
        looking for lines of the form: X-DSPAM-Confidence:    0.8475

    Count these lines and extract the floating point values from each of the lines and compute the\
        average of those values and produce an output as shown below. Do not use the sum() function
        or a variable named sum in your solution.

    You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are\
        testing below enter mbox-short.txt as the file name.
'''
# Use the file name mbox-short.txt as the file name
count = 0
average = 0
number = 0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        word_num = line.split(' ')
        number += float(word_num[1])

average = number/count
print("Average spam confidence:", average)