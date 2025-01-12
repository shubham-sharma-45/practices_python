#module_handling
import time 


#recursion 
def fact(x):
	if x == 0 or x == 1 :
		return 1 
	else :
		return x *fact(x-1)
rec_start_time = time.time()		
n = int(input("enter value :"))
result = fact(n)
print("fact :",result)
rec_end_time = time.time()
req_rec_time = rec_end_time - rec_start_time
print("Recursion Time Data")
print("Start Time : ",rec_start_time)
print("End Time : ",rec_end_time)
print("Required Time : ",req_rec_time)


#iterative
ite_start = time.time()
n = int(input("Enter Value : "))
fact_n = 1 
for i in range(1,n+1) :
	fact_n = fact_n * i
print("Factorial of {} = {}".format(n,fact_n)) 
ite_end = time.time()
req_ite_time = ite_end - ite_start
print("Iteration Time Data")
print("Start Time : ",ite_start)
print("End Time : ",ite_end)
print("Required Time : ",req_ite_time)
