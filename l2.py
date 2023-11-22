a = int(input("Enter a value = "))
org=a
rev=0
while a>0:
    rem=a%10
    rev=rev*(10)+rem
    a=a//10
if  org==rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")