# Py script for Factorial
n = int(input("Enter Value : "))
fact_n = 1 
for i in range(1,n+1) :
	fact_n = fact_n * i


print("Factorial of {} = {}".format(n,fact_n)) 

# Premutation => nPr = n!/(n-r)!

n = int(input("Enter Value n : "))
r = int(input("Enter Value r : "))


#Factorial of n

fact_n = 1 
for i in range(1,n+1) :
	fact_n = fact_n * i
print("Factorial of {} = {}".format(n,fact_n))

#Factorial of n-r
fact_nr = 1 
for j in range(1,(n-r)+1) :
	fact_nr = fact_nr * j
print("Factorial of {} = {}".format(n-r,fact_nr))

Permutation = fact_n / fact_nr

print("Permutation of {} over {} = {}".format(n,r,Permutation))



# Combination => n!/(r! * (n-r)!)

n = int(input("Enter Value n : "))
r = int(input("Enter Value r : "))


#Factorial of n

fact_n = 1 
for i in range(1,n+1) :
	fact_n = fact_n * i
print("Factorial of {} = {}".format(n,fact_n))

#Factorial of n-r
fact_nr = 1 
for j in range(1,(n-r)+1) :
	fact_nr = fact_nr * j
print("Factorial of {} = {}".format(n-r,fact_nr))

#Factorial of r 
fact_r = 1 
for k in range(1,r+1) :
	fact_r = fact_r * k
print("Factorial of {} = {}".format(r,fact_r))

combination = fact_n / (fact_r * fact_nr)

print("combination of {} over {} = {}".format(n,r,combination))