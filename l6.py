n = int(input("Enter a factorial number = "))
if n==0:
    print("The Factorial of 0 is 1")
else:
    i=1
    f=1
    while i<=n:
        f = f * i
        i=i+1
        print("Factorial of "+str(i-1)+ " is "+str(f))