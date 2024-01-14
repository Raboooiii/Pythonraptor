a = int(input("Enter a number = "))
a1 = a
k = 0
i = 0
while a1 > 0:
    n = a1 % 10
    a1 = a1 // 10
    i = i + 1
a1 = a
while a1 > 0:
    n = a1 % 10
    a1 = a1 // 10
    k = k + (n ** i)
if k == a:
    print(str(a) + " is an Armstrong number.")
else:
    print(str(a) + " is not an Armstrong number.")
