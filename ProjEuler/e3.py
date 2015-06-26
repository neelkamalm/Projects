import math

# Returns if a given number is a prime
# Uses all the previous primes to identify
# is num is prime
# principle : if a number is prime, it is
#indivisble by all the previous primes
def isPrime(num, known_primes):

    if len(known_primes) > 0:
        for i in known_primes:
            if (num % i) == 0:
                return False
    else:
        return True

    check_until = int(math.sqrt(num)) + 1

    #print "check_until = " + str(check_until)

    for i in xrange(2, check_until):
        if (num % long(i)) == 0:
            return False
     
    return True

# Returns the largest prime factor of num
# Principle: if x is a prime factor of num
# the next largest primefactor can be found in num/x
def LargestPrimeFactor(num):
    
    known_primes =[2L]
    prime_factors = []

    i = 3L
    largestPrimeFactor = 1

    while i <= num:
        if isPrime(i, known_primes) == True:
            known_primes.append(i)

            #is it a factor of num

            if (num %i) == 0:
                prime_factors.append(i)
                print prime_factors
                largestPrimeFactor = i

                #Remove all the i's in num
                while (num % i) == 0:
                    num = num / i
                    print("i = %d, num = %d"%(i,num))
        i += 1L

#    lim = num
#    while i < lim:
#        if isPrime(i, known_primes) == True:
#            known_primes.append(long(i))
#            if ((num % i)  == 0):
#                prime_factors.append(i)
#                print prime_factors
#                while (num % i) == 0:
#                    num = num / i
#                largestPrimeFactor = i
#                lim = num / i
#                if (lim < largestPrimeFactor):
#                    print num
#                    break

#        i += 1L

    #print primes_list        
    #for factor in known_primes: 
        #print "div = " + str(num % factor)
   #     if (num % factor) == 0:
   #         largestPrimeFactor = factor
    #largestPrimeFactor = num / i
    
   # if largestPrimeFactor < i:
   #     largestPrimeFactor = i*/
    
    #print known_primes
    print prime_factors
    return largestPrimeFactor        

# Finda primeIndex num of primes
# starting from 2
def findAllPrimes(primeIndex):
    known_primes = [2L]
    count = 0
    i = 3L
    while count < primeIndex: 
        if isPrime(i, known_primes) == True:
            known_primes.append(long(i))
            count += 1
        i += 1    

    print known_primes[10000]
    return known_primes


def primeSum(maxPrime):
    known_primes = [2L]
    count = 0
    i = 3L
    s = 0
    while  s < sumPrime: 
        if isPrime(i, known_primes) == True:
            known_primes.append(long(i))
            s += i 
        i += 1    
    
    print "Num terms = " + str(len(known_primes))

    #print known_primes[10000]
    
if __name__ == "__main__":
    #print("20 is %s"%(str(isPrime(20,[1,2]))))
    #print("20 is %s"%(str(isPrime(17,[1,2]))))
    #print("21 is %s"%(str(LargestPrimeFactor(13195))))
    #print("Largest prime factor is : %s"%(str(LargestPrimeFactor(600851475143L))))
    primeSum(1000000)

