
import math    
def is_prime(num):
    if num < 2 :
        return False
    
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3,int(math.sqrt(num)+1),2):
        if num % i == 0:
            return False
    return True
def under_limit_prime(limit):
    primes=[]
    for num in range (2 , limit):
        if is_prime(num):
            primes.append(num)
    return primes

limit=int(input("Enter any PRIME INTEGER LIMIT : " ))  
prime_number= under_limit_prime(limit)
for prime in prime_number:
    print(prime , end=" ")      
        


        



    