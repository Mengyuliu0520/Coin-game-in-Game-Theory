import math
import random

# Though I can make this program as a function, I'm busy now.
# May be I'll do it later.
a = [0, 0, 1, 1, 0, 1, 1, 1]
i = 0
j = 0
# res was how much A won in the total cycles
res = 0
cycles = 10000
for i in range(cycles):
	for j in range(8):
		b = random.random()
		if(b > 0.5):
			b = 0
		elif(b < 0.5):
			b = 1
		if (a[j] == b):
			if(b == 0):
				res -= 3

			elif(b == 1):
				res -= 1

		elif(a[j] != b):
			res += 2
	j = 0
print (res)


