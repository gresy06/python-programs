string = input("enter the string:")
count = 0
for c in string:
    if c.isspace() != True:
        count = count + 1
print("total number of characters :",count)
