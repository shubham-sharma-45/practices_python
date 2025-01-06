print("Make can calculator :")
add = True
while add :
	choice = int(input("Enter 1 value addtion \n Enter 2 value substraction \n Enter 3  value multiplition \n Enter  4 value division \n please Enter value :"))
	num1 = int(input("Enter  first value :"))
	num2  = int(input("Enter second value :"))

	if choice == 1 :
		result = num1 + num2
		print("{} + {}={}".format(num1,num2,result))
	elif choice == 2:
		result = num1 - num2
		print("{} - {}={}".format(num1,num2,result))
	elif choice == 3:
		result = num1 * num2
		print("{} * {}={}".format(num1,num2,result))
	elif choice == 4:
		result = num1 / num2
		print("{} / {}={}".format(num1,num2,result))
	else :
		print("invalid input")

	value = input("return use ?, (yes/no) : ")

	if value =="no":
		add=False

	

