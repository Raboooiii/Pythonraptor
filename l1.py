n = int(input("No. b/w 1 and = "))
sum = 0
count = 0
for i in range (1,2*n+1,2):
    sum+=i
    count+=1
    if count == n:
        print("The sum of first odd numbers is "+str(i))
