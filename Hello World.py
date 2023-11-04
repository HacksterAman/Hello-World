import time
import random
import string

result = ""
for char in "Hello World!":
    	for _ in range(5):
    	   print(result + random.choice(string.ascii_letters), end='\r')
    	   time.sleep(0.1)
    	result += char
    	time.sleep(0.1)
    	print(result,end='\r')
