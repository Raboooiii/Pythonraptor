x = int(input("X = "))
n = int(input("n = "))
r=1
count=1
if n==0:
    print(str(x)+"^"+str(n)+" = 1")
else:
    if n>0:
        while count<=n :
            r=r*x
            count=count+1
        if n==count:
                print(str(x)+"^"+str(n)+" = "+str(r))
    else:
        while count<=n:
            r=r/x
            count=count+1
        if n==-(count):
            print(str(x)+"^"+str(n)+" = "+str(r))