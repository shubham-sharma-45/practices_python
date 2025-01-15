def circle_area(x):
	rs = 3.14
	area = 2*rs*x
	return area

n = int(input("Enter No. of Iteration : "))
for i in range(n) : 
	r = int(input("Enter radius :"))
	a = circle_area(r)
	print ("circumference with radius {} = {}".format(r,a))