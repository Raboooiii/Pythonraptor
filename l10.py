a = int(input("Enter a number = "))
a1=a
k=0
i=0
while a1>0:
    n=a1%10
    a1=a1//10
    i=i+1
    if a1==0:
        a1=a
        while k<=a1:
           n=a1%10
           a1=a1//10
           k=k+(n**i)
        if a1==0:
            if k==a:
                print(str(a)+" is an armstrong no.")
            else:
                print(str(a)+" is not an armstrong no.")
