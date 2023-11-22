a = int(input("Enter a number = "))
if a%10==0:
    print("It is automorphic")
else:
    sqr=a**2
    a1=a
    i=0
    while a1>0:
        a1=a1//10
        i=i+1
        if a1==0:
            k=0
            sqr1=sqr%(10**i)
            if sqr1==a:
                print(str(a)+" is automorphic")
            else:
                print(str(a)+" is not automorphic")
