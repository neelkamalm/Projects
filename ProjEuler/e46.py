
def isPrime(primes, num):
    for i in primes:
        if num % i == 0:
            return False
            
    primes.append(num)        
    return True
    
                    
def isOdd(num):
    return num % 2 != 0
    
def satisfiesFormula(primes, num):
    if not isPrime(primes, num) and isOdd(num):
        for j in primes:
            for k in xrange(1, num):
                n = j + 2 * ( k ** 2)
                if num == n:
                    print " %d satisfies GoldBach's formula (%d, %d)"%(num, j, k)
                    return True
                elif num < n:
                    break  
    else:
        return True                
                    
    return False                
     
 
if __name__ == "__main__":
    primes_list = [2,3,5,7,11,13,17,19,23]
    
    i = 24
    
    found = True
    
    while found:
        i += 1
        found = satisfiesFormula(primes_list, i)
        
    print "i = %d"%(i)     
        
    
  
            
    
                                                                                           
            