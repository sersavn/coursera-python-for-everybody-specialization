fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    #print("pieces", pieces)
    email = pieces[1]
    #print("email", email)
    email = line.split("@")
    #print("email2",email)
    email = email[1]
    email = email.split("\n")
    email = email[0]
    print(email)
