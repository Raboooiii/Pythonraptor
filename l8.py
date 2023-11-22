a = int(input("Enter a number = "))
if a==0:
    print("All integers are factors")
else:
    if a>0:
        i=1
        k=0
        while i<=a:
            if a%i==0:
                k=k+i
                i=i+1
            else:
                i=i+1
        if i>a:
            print("Sum of factors is "+str(k))
    else:
        a=(-a)
        i=1
        k=0
        while i<=a:
            if a%i==0:
                k=k+1
                i=i+1
            else:
                i=i+1
        if i>a:
            print("Sum of factors is "+str(-k))