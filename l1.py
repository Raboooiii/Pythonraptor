n = int(input("No. of terms needed = "))
sum = 0
count = 0
i=1
while count<n:
    sum+=i
    i+=2
    count+=1
print("The sum of first "+str(n)+"odd numbers is "+str(sum))
