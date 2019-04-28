#9.4 Write a program to read through the mbox-short.txt
#and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines
#and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the
#sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary
#using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
x = 0
counts = dict()
for line in handle :
    if line.find ('From ') : continue
    x = x + 1
    line = line.split()
    mails = line[1]
    counts[mails] = counts.get(mails, 0) + 1
    print("mails", mails)
#print("counts", counts) prints dictionary with email counts and contacts
mostmails = None
prolificomitter = None
for sender,amount in counts.items():
    if mostmails is None or amount > mostmails:
        print("sender, amount", sender, amount)
        mostmails = amount
        prolificomitter = sender
print(prolificomitter, mostmails)
