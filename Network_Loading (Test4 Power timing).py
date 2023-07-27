import math
import time


start_time1 = time.time()
for i in range(10000000):
	a=math.pow(1.5,3)
print("%s seconds math.pow" % (time.time() - start_time1))




start_time2 = time.time()
for i in range(10000000):
	a=1.5**3
print("%s seconds built-in pow **" % (time.time() - start_time2))



start_time3 = time.time()
for i in range(10000000):
	a=pow(1.5,3)
print("%s seconds built-in pow func. " % (time.time() - start_time3))
