#6.5 Write code using find() and string slicing (see section 6.10)
#to extract the number at the end of the line below.
#Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
digit0 = text.find('0')
digit5 = text.find('5')
number = text[digit0 : digit5+1]
numberfloat = float(number)
print(numberfloat)
