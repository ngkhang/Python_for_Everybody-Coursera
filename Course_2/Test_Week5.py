'''
Assignment 9.4

    Write a program to read through the mbox-short.txt and figure out who has sent the\
        greatest number of mail messages. The program looks for 'From ' lines and takes
        the second word of those lines as the person who sent the mail. The program
        creates a Python dictionary that maps the sender's mail address to a count of
        the number of times they appear in the file. After the dictionary is produced,
        the program reads through the dictionary using a maximum loop to find the most
        prolific committer.

    ----Example:
        cwen@iupui.edu 5
'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if(line.startswith('From ')):
        raw_str = line.split()
        person = raw_str[1]
        counts[person] = counts.get(person,0) + 1

big_person = None
big_count = None
for key, val in counts.items():
    if big_count is None or val > big_count:
        big_count = val
        big_person = key

print(big_person, big_count)