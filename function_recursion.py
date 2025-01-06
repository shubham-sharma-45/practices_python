def fact(x):
	if x == 0 or x == 1 :
		return 1 
	else :
		return x *fact(x-1)
n = int(input("enter value :"))
result = fact(n)
print("fact :",result)