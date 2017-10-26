#10.2 Write a program to read through the mbox-short.txt
#and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time
#and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
x = 0
counts = dict()
for line in handle :
    if line.find ('From ') : continue
    x = x + 1
    line = line.split()
    line = line[5]
    line = line.split(':')
    line = line[0]
    counts[line] =  counts.get(line, 0) + 1#Hystagramm growth by 1 block
print("counts unsorted", counts)# hystagramm result unsorted
counts = sorted(counts.items())
print("counts sorted", counts)# hystagramm result sorted by str
for hours, times in counts:
    print(hours,times)
