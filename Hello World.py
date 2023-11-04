import time
import random
import string

colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[31m",  # Light Red
    "\033[32m",  # Light Green
    "\033[33m",  # Light Yellow
    "\033[34m",  # Light Blue
    "\033[35m",  # Light Magenta
    "\033[36m"   # Light Cyan
]
random.shuffle(colors)

result = ""
text="Hello World!"
for i in range(12):
    	for _ in range(5):
    	   print(f"{result}{random.choice(colors)}{random.choice(string.ascii_letters)}", end='\r')
    	   time.sleep(0.1)
    	result+=colors[i]+text[i]
    	time.sleep(0.1)
print(result)
