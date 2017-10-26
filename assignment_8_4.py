#8.4 Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
x = 0
y = 0
oneword = list()
emptylist = list()
newlist = list()
for line in fh:
    x = x + 1
    line = line.rstrip()
    splitline = line.split()
    for element in splitline:
        if element in emptylist : continue
        emptylist.append(element)
        emptylist = sorted(emptylist)
print(emptylist)

#newlist = sorted(n)




#sorts the new list in A B C order


#print("line.rstrip()", line.rstrip())
#print("lst", lst)
#print("lst[1:]", lst[1:])
    #splitlst = lst.split()
#print("splitlst", splitlst)


#print(lst.rstrip(lst))
#print(line)
#print(line.rstrip())
