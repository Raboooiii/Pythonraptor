a = int(input("Enter a value = "))
b = int(input("Enter a value = "))
c = int(input("Enter a value = "))
x=(-b+((b*b)-(4*a*c))**(1/2))/(2*a)
y=(-b-((b*b)-(4*a*c))**(1/2))/(2*a)
if int(x)>0 and int(y)>0:
    print("Both roots are positive")
elif int(x)<0 and int(y)<0:
    print("Both roots are negative")
elif int(x)>0 and int(y)<0:
    print("Root X is positive and Root Y is negative")
elif int(x)<0 and int(y)>0:
    print("Root Y is positive and Root X is negative")