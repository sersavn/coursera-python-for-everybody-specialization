#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except
#and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.
#Invalid input
#Maximum is 10
#Minimum is 2
    #elif num != int or float : break
    #print("Enter number, not a word!")

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done' :
        break
    try:
        numint = int(num)
        if smallest is None :
            smallest = numint
        elif numint < smallest :
            smallest = numint
        if largest is None :
            largest = numint
        elif numint > largest :
            largest = numint
    except:
         print("Invalid input")
    continue
print("Maximum is", largest)
print("Minimum is", smallest)
