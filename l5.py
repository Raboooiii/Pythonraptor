a = int(input("Enter a number = "))
n=a
rev=0
rem=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if n==0:
    print("Reverse is "+str(rev))