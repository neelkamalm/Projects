def lengthOfSeries(term_1, term_n, diff):
	return ((term_n - term_1)/diff) + 1
			
def ApSum(term_1, term_n, diff):
	series_length = lengthOfSeries(term_1, term_n, diff)
	s = (series_length * ( term_1 + term_n))/2
        print("Series:%d:%d:%d len=%d sum=%d"%(term_1,term_n,diff, series_length,s))
        return s
	
if __name__ == "__main__":
	print "Sum = " + str(ApSum(3,999,3) + ApSum(5,995,5) - ApSum(15,990,15))
