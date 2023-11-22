a = int(input("Enter a number = "))
b= int(input("Enter a number = "))
if a>b:
    while b!=0:
        k= a%b
        a=b
        b=k
    if b==0:
        if a>0:
            print("GCD = "+str(a))
        else:
            a=(-a)
            print("GCD = "+str(a))
else:
    while a!=0:
        k= b%a
        b=a
        a=k
    if a==0:
        if b>0:
            print("GCD = "+str(b))
        else:
            print("GCD = "+str(-b))