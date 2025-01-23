'''#Module Handling 
import time


#Recursion Method
def fact(x):
	if x == 0 or x == 1 :
		return 1 
	else :
		return x *fact(x-1)

n = int(input("Enter no of Iterations : "))
for i in range(n) : 
	rec_start_time = time.time()		
	n = int(input("enter value :"))
	result = fact(n)
	print("fact : ",result)
	rec_end_time = time.time()
	req_rec_time = rec_end_time - rec_start_time

	print("Recursion Time Data")
	print("Start Time : ",rec_start_time)
	print("End Time : ",rec_end_time)
	print("Required Time : ",req_rec_time)
	print()

	#iterative

	

	ite_start = time.time()
	
	fact_n = 1 
	for i in range(1,n+1) :
		fact_n = fact_n * i
	print("Fact: ", fact_n) 
	ite_end = time.time()
	req_ite_time = ite_end - ite_start

	print("Iteration Time Data")
	print("Start Time : ",ite_start)
	print("End Time : ",ite_end)
	print("Required Time : ",req_ite_time)	'''


'''a = [2, 4, 6, 8, 10]

# Calcuate the sum of list
# and divide it by length of list
avg = sum(a) / len(a)
print(avg)'''

"""new=input("Enter how many values :")
a=[]
for i in new:
	num=int(input("enter values:"))
	a.append(num)
print(a)

total_sum = 0
for i in a:
    total_sum += i
avg = total_sum / len(a)
print(avg)"""

'''num=int(input("enter number::"))
a=[]
for i in range(0,num):
	add=int(input("enter number::"))
	a.append(add)
print(a)
total_sum = 0
for i in a:
    total_sum += i
avg = total_sum / len(a)
print("total average ",avg)
	'''

'''
n = int(input("Enter no of elements : "))
shubh = []
for i in range(n):
	a = int(input("Enter no: "))
	shubh.append(a)
sum = sum(shubh)
print("total of elements :",sum )

Average = sum(shubh)/(n)	

print ("Average  of elements is ", Average)
Average = sum(shubh)/(n)	

print ("Average = ", Average)'''

'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list1 = []
for i in a :
	if i in b and i not in list1 :

		list1.append(i)
print(list1)

'''
'''x = "shubham"
y = x[::-1]
print(x)
print(y)


x= "aman"
for i in range(len(x)-1,-1,-1):
	print(x[i])
'''
'''a = [2, 4, 5, 6, 7, 7, 8, 10, 38, 23, 23, 8, 2]
def unique(a):
	myset = set(a)
	return myset

print(unique(a))
'''

'''def f1():
	print("hello world")
f1()

def f2(name):
	print(name)
f2('shubham')'''

'''def f3(x):
	return x**3
x = int(input("Enter a number :"))
print(f3(x))'''
'''
file = "the an a "
article_count = 0
temp = file.split()
print(temp)
for i in temp:
	if i.lower() == "a" or i.lower() == "an" or i.lower() == "the":
		article_count += 1
print ("The no. of articles = ", article_count)'''
'''
def f1(player_1,player_2):
	player_1 = "rock"
	if player_2 =="rock":
		return ("its a draw")
	elif player_2 == "paper":
		return ("player_2 wins")
	elif player_2 == "scissor":
		return ("player_1 wins")


def f2(player_1,player_2):
	player_1 = "paper"
	if player_2 =="paper":
		return ("its a draw")
	elif player_2 == "scissor":
		return ("player_2 wins")
	elif player_2 == "rock":
		return ("player_1 wins")

def f3(player_1,player_2):
	player_1 = "scissor"
	if player_2 =="scissor":
		return ("its a draw")
	elif player_2 == "rock":
		return ("player_2 wins")
	elif player_2 == "paper":
		return ("player_1 wins")

player_1 = input(" Player_1, select option : ")
player_2 = input("Player_2, select option : ")

i = True
while i>=7:
	if player_1== "rock":
		print(" result of game is {} ".format(f1(player_1,player_2)))
		#print("result count ")
	elif player_1 == "paper":
		print(" result of game is {} ".format(f2(player_1,player_2)))
	elif player_1== "scissor":
		print(" result of game is {} ".format(f3(player_1,player_2)))
	break

'''

'''string = "i am a good "
a = string.split()
print(a)
list1 = []
for i in a:
	var = i.capitalize()
	print(var)
	list1.append(var)
print(list1)
'''


'''string = input("Enter character :")
var = string.split() #("i","am","a","good")
print(var)
list1 =[]
for i in range(0,len(var)):
	#print(i)
	if i != 3 :
		#print(i)
		
		#a = i.upper()
		list1.append(var[i])
	else:
		a = var[i].upper()
		list1.append(a)
print(str(list1))
'''

'''var = "i am a good student"
x = var.split()
z = int(input("Enter index :"))
for i in range (len(x)):
	z = x[i]
	print(z)
	x[i] = z[0].upper()+z[1:].lower()
	print(x)
'''

'''string = input("Enter strings :")
var = string.split()
list1=['a','an','the']
cnt = 0
count_total=0
ansList =[]
for ele in list1:
	cnt = 0
	for ele1 in var:
		if ele == ele1:
			cnt+=1
			count_total+=1

	ansList.append(cnt)
	
for i in range(len(list1)):
	print(list1[i],"=",ansList[i])
print("Total artical=",count_total)
'''


a = 10
b =3
r = a//b
print(r)



	





	
