a = int(input("Enter a binary value = "))
d=0
i=0
while a>0:
    k=a%10
    d=d+((2**i)*k)
    i=i+1
    a=a//10
if a==0:
    print("Decimal number is "+str(d))