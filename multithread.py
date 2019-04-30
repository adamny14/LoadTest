import urllib2; 
from multiprocessing.dummy import Pool as ThreadPool 

pool = ThreadPool(8)
def my_function( i):
	print( i*i)

numbers = []
for i in range(100000000):
	numbers.append(i)


pool.map(my_function, numbers)


