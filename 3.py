num=600851475143 # number to check
l=[]
def factor(number, value=2):
	fin=1 # variable used for checking if product of "l" list = num
	for v in l:
		fin=fin*v
		if fin==num:
			print(l[len(l)-1])
			exit()
	while True:
		if number%value==0:
			l.append(value)
			factor(number/value,value) # recursive induction of factor fcn
			return value
		value+=1
factor(num)
