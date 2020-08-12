def fib(n):     #fibonacci series using while loop
	f = 0
	i = 1
	nextf = 0
	while n >= 1
		print ("Fibonacci no.", f)
		nextf = f + i
		f = i
		i = nextf
		n -= 1

def fib1(n):    #fibonacci series using for loop with additional checks
	f = 0
	i = 1
	nextf = 1
	if n <= 0:
		print('Positive non-zero value needed')
	else:
		if n == 1:
			print("Fibonacci no.", f)
		else:
			print("Fibonacci no.", f)
			for j in range(1,n):
				print("Fibonacci no.", nextf)
				nextf = f + i
				f = i
				i = nextf
				#print("Fibonacci no.", nextf)
fib1(10)

