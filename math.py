''''import math
x=int(input("enter a value:-"))
y=math.sqrt(x)
print("squr root of {}={}".format(x,y))
'''
'''def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return n*fact(n-1)
x=int(input("enter no:-"))
y=fact(x)
print("factorial of {}={}".format(x,y))'''

n = int(input("Enter Value : "))
fact_n = 1 
for i in range(1,n+1) :
	fact_n = fact_n * i


print("Factorial of {} = {}".format(n,fact_n))
