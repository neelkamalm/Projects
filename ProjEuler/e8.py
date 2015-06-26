#!/usr/bin/python

def calculateProduct(s):
    i = 0
    product = 1
    index = 0
    
    if len(s) == 0:
        return [product, index]
    
    while (i < 13):
        num = int(s[i])
        if num != 0:
            product *= num
            i += 1
        else:

            if s[i+1:] == '':
                print "string empty"
                product = 1
                break
                
            product = 1
            s = s[i + 1:]   
                
            index = index + i + 1     
            i = 0    
            
    #ret = [product, index]        
    
    return [product, index]
    

def bruteForce(string):
    maxProduct = 1
    product = 1
    
    i = 0
    index = 0
    
    while i < 987:
        for j in xrange(0,13):
            product *= int(string[i + j])
            
        if product > maxProduct:
            maxProduct = product
            index = i
                
	i += 1
	product = 1
	
     		
    #print "maxProduct = %d"%(maxProduct)
    print "index = " + str(index)
    return maxProduct
    

def findSubStringWithout0(string):
    subStr = string[0:13]
    shift = 0
    
    while len(subStr) == 13:
        zeroIndex = subStr.rfind('0')
        #print "zIndex = " + str(zeroIndex)
        if zeroIndex == -1:
            break
            
        shift = shift + zeroIndex +1 
        #print "shift = " + str(shift)
        subStr = string[shift:shift+13]
        #print "subStr = " + subStr
        
    return shift        
            
def computeProduct(string):
    product = 1
    for i in string:
        product *= int(i)    
        
    return product    
        
            
# first find if there is a zero in the string of 13 characters
#if found discard that entire set 
    
def findMaxProduct(string):
    i = findSubStringWithout0(string)
    
    product = computeProduct(string[i::13])
    maxProduct = product
    index = 0
    
    while i < 986:
        if  string[i+13] == '0':
            i = i+ 1 + findSubStringWithout0(string[i+1:])
            product = computeProduct(string[i:i + 13])
            #print "cp: i = " + str(i) + " product = " + str(product)
        else:
            product = (product * int(string[i+13]))/int(string[i])
            #print "i = " + str(i) + " product = " + str(product)
            i += 1 
            
        if product > maxProduct:
            index = i
            maxProduct = product
         
    
    #print "fmp : index = " + str(index)                
    return maxProduct    
        
    
    
    
if __name__ == "__main__":
    string = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

    #print"index of non-zero string = %d" %(findSubStringWithout0("12456789012345678901234567891234"))
    
    print "Max Product = %d"%(bruteForce(string))
    print "Max Product = %d"%(findMaxProduct(string))
    print "Max Prod String = " + string[197:197+13]
     		
    
#    [product, i] = calculateProduct(string)
    
#    #print len(string)
         
#    print product    
#    maxProduct = product    
    
#    stIndex = 0
#    while i < 987:
#        #print " i = %d"%(i)
#        val = int(string[i + 12])
#        if val == 0:
#            [product, index] = calculateProduct(string[i + 13:]) 
#            #print " index = %d"%(index)
#            i = i + 13 + index 
#            continue
                       
#        product = (product / int(string[i]) * val)
#        print "product = " + str(product)
#        
#        if product > maxProduct :
#            stIndex = i
#            maxProduct = product
#            
#        i += 1    
            
#    print "maxProduct = %d stIndex = %d st=%s"%(maxProduct, stIndex, string[stIndex:stIndex+13])    
            
        
    

