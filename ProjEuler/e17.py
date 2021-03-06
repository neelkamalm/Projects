
def countLetters(num):
    units = ["zero","one","two","three","four","five","six","seven","eight","nine","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty","forty", "fifty", "sixty", "seventy","eighty", "ninety"]
    hundreds = "hundred"
    thousand = "thousand"

    number_map = {}
    for i in range(0,20):
        number_map[i] = units[i]
    
    for i in range(2,10):
        number_map[10 * i] = tens[i - 2]

    number_map[100] = "hundred"
    number_map[1000] = "thousand"

    
    numLetters = 0
    if num < 20:
        numLetters = len(number_map[num])
        num -= num
    else:
        # first get the right most digits
        tens_pos = num % 100
        if (tens_pos > 0) and (number_map.has_key(tens_pos) == True):
            numLetters += len(number_map[tens_pos])
            num = num - tens_pos
        
    i = 0
    while num > 0:
        digit = num % 10
        if (digit > 0):
            if i == 0:
                numLetters += len(number_map[digit])
            elif i == 1:
                numLetters += len(number_map[digit * 10])
            elif i == 2:
                if numLetters > 0:
                    numLetters += 3
                numLetters += len(number_map[100])
                numLetters += len(number_map[digit])
            elif i == 3:
                numLetters += len(number_map[1000])
                numLetters += len(number_map[digit])
                
        i  = i + 1
        num = num / 10
    
    return numLetters

def countAllLetters(lim):
    s = 0
    for i in range(1,lim+1):
        s += countLetters(i)

    return s    

if __name__ == "__main__":
    print(" Num letters in 0 = %d "%(countLetters(342)))
    print(" Num letters in 0 = %d "%(countAllLetters(1000)))








