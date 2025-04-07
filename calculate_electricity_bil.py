units = int(input("Enter the number of units:-"))
bill = 0 

if units<=100 :
	bill = units * 5
	print(bill)

elif units <= 200 :
	bill = (100 * 5) + ((units - 100) * 7)
	print(bill)
elif units <=300:
	bill = (100 * 5) + (100 * 7) + ((units - 200) * 9)
	print(bill)

else:
	bill = (100 * 5) + (100 * 7) + (100 * 9) + ((units - 300) * 10)
	print(bill)
