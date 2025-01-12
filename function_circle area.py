def circle_area(x):
	rs = 3.14
	area = rs*x*x
	return area

n = int(input("Enter No. of Iteration : "))
for i in range(n) : 
	r = int(input("Enter radius :"))
	a = circle_area(r)
	print ("Area of Cricle with radius {} = {}".format(r,a))