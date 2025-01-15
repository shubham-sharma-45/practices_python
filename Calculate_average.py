"""num=int(input("enter number::"))
a=[]
for i in range(0,num):
	add=int(input("enter number::"))
	a.append(add)
print(a)
total_sum = 0
for i in a:
    total_sum += i
avg = total_sum / len(a)
print(avg)"""


n = int(input("Enter no of elements : "))
shubh = []
for i in range(n):
	a = int(input("Enter no: "))
	shubh.append(a)
Add = sum(shubh)
print ("Sum of elements : " ,Add)

Average = sum(shubh)/(n)	

print ("Average of {} elements is {}".format( n, Average,))

