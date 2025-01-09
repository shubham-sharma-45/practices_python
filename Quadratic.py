import math

a = int(input("enter value a :"))
b = int(input("enter value b :"))
c = int(input("enter value c :"))

"""num1 =((-b)+(math.sqrt((b**2)-4*a*c)))/(2*a)
num2 =((-b)-(math.sqrt((b**2)-4*a*c)))/(2*a)

print(num1)
print(num2)"""

temp=(b**2)-(4*a*c)
if temp>0:
	num1 =((-b)+(math.sqrt((b**2)-4*a*c)))/(2*a)
	num2 = ((-b)-(math.sqrt((b**2)-4*a*c)))/(2*a)
	print("root are real and diffrent ")
	print(num1)
	print(num2)

elif temp==0:
	x1=((-b)+(math.sqrt((b**2)-4*a*c)))/(2*a)
	x2=((-b)-(math.sqrt((b**2)-4*a*c)))/(2*a)
	print("Roots are real and same")
	print("x1 is::",x1)
	print("x2 is::",x2)
elif temp<0:
	print("complex number is not solutions")
	

