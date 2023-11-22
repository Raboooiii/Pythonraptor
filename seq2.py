a = float(input("Enter a value = "))
b = float(input("Enter a value = "))
c = float(input("Enter a value = "))
s= (a+b+c)/2
per=(a+b+c)
area = ((s*(s-a)*(s-b)*(s-c))**(1/2))
print("The perimeter is " + str(float(per)))
print("The area is " + str(float(area)))