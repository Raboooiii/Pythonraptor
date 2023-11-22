a = int(input("No. for terms needed = "))
if a<=0:
    print("Please try again")
else:
    sum=0
    x=1
    i=0
    k=0
    n=1
    while k>=0:
        k=k+1
        sum=sum+(x*((-1)**i))
        if k==a:
            print("Sum of the series is "+str(sum))
        else:
            n=n+1
            x=x+((2*n)-1)
            i=i+1