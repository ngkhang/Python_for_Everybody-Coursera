'''
Assignment 7.1

    You'll complete this item using the course's autograders. Open the tool\
        using the button below.

    Write a program that prompts for a file name, then opens that file and\
        reads through the file, and print the contents of the file in upper
        case. Use the file words.txt to produce the output below.
    You can download the sample data at http://www.py4e.com/code3/words.txt
'''
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    text  = line.rstrip()
    print(text.upper())