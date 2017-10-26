#Write a program to prompt for a score between 0.0 and 1.0.
#If the score is out of range, print an error.
#If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit.
#For the test, enter a score of 0.85.
score = input("Enter Score:")
scorefloat = float(score)
if scorefloat > 1 or scorefloat < 0 :
    print("Out of range, pidor")
elif scorefloat >= 0.9 :
    print("A")
elif scorefloat >= 0.8 :
    print("B")
elif scorefloat >= 0.7 :
    print("C")
elif scorefloat >= 0.6 :
    print("D")
elif scorefloat < 0.6 :
    print("F")
