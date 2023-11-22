n = int(input("Enter a number = "))
a=0
b=1
print(a)
print(b)
count=2
while count<=n:
    fn=a+b
    count=count+1
    a=b
    b=fn
    print(fn)
