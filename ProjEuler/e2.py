def fibonnaci_sum(limit):
   num1 = 0
   num2 = 1
   s = 0
   while num2 < limit:
    temp = num2   
    num2 = num1 + num2
    num1 = temp
    print str(num2)
    print str(limit)
    if num2 % 2 == 0:
        s += num2

   return s    


if __name__ == "__main__":
    print("Sum of even Fibonacci's < %d = %d"%(4000000,fibonnaci_sum(4000000)))
