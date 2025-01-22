def fibonacci():
	n = int(input("Enter values :"))
	fib = []
	i = 1

	if n == 0:
		fib=[]
	elif n == 1:
		fib =[1]
	elif n == 2:
		fib=[5,9]

	elif n > 2 :
		fib=[5,9]
		while i < (n-1):
			fib.append(fib[i]+fib[i-1])
			i+=1

		return fib 	

print(fibonacci())
