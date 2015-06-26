
def isPalindrome(num):
    s = str(num)

    l = len(s)

    i = 0
    j = -1

    while i < (len(s)/2):
        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True        

def largestPalindrome(n):
    largestPalindrome = 0
    for i in xrange(100,n):
        for j in xrange( i + 1, n):
            p = i * j
            if (isPalindrome(p) == True) and (p > largestPalindrome):
                largestPalindrome = p

    return largestPalindrome            
                

if __name__ == "__main__":
    #print("1001 palindrome? %s"%(isPalindrome(1001)))
    #print("1002 palindrome? %s"%(isPalindrome(1002)))
    print("Largest Palindrome among 2 digit products = %d"%(largestPalindrome(1000)))
