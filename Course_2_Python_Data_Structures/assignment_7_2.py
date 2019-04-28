#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and
#compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
n = 0 # for amount of lines
n1 = 0 #for summ
xDSPAM = 0
nfloat = float(n)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    n = n + 1
    xDSPAM = line[line.find('0') : ]
    xDSPAMfl = float(xDSPAM)
    n1 = n1 + xDSPAMfl
median = n1 / n
print("Average spam confidence:", median)
