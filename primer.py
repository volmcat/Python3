# This program takes in a number, preferably large and prime, and checks if its actually prime. 
import time

num1 = int(input('Give me a number to check for prime: '))
if num1 % 10 == 1 or num1 % 10 == 3 or num1 % 10 == 7 or num1 %10 == 9:
    start = time.time()
    factors = 0
    num2 = 3
    while(num2 < num1):
        if(num1 % num2 == 0):
            factors += 1
            num2 += 2
        else:
            num2 = num2 + 2
    if(factors > 0):
        print("Not prime, found %.0f  factors" % (factors))
    else:
        print("you found a prime!")
    end = time.time()
    print("Cracked in %.2f ms" % ((end - start)*1000.0))
else:
    print ("Definately not a prime number, prime numbers end with a 1, 3, 7, or 9")
