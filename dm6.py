a = int(input("Enter a value = "))
b = int(input("Enter a value = "))
c = int(input("Enter a value = "))
if a>b:
    if b>c:
        print(str(c)+" is the smallest no.")
    else:
        print(str(b)+" is the smallest no.")
else:
    if c>a:
        print(str(a)+ " is the smallest no.")
    else:
        print(str(c)+" is the smallest no.")