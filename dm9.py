a = int(input("Enter a value = "))
b = int(input("Enter a value = "))
if a<=0 and b<=0 and a>=b:
    print("Distance b/w the numbers is " + str(-1*(a - b)))
elif a>=0 and b>=0 and a>=b:
    print("Distance b/w the numbers is " +str(a-b))
elif a>=0 and b>=0 and b>=a:
    print("Distance b/w the numbers is " +str(b-a))
elif a<=0 and b>=0:
    print("Distance b/w the numbers is "+str(b-a))
elif a>=0 and b<=0:
    print("Distance b/w the numbers is " +str(a-b))