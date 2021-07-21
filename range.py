import random

range(3)#[0, 1, 2]

for i in range(100):
	r = random.randint(1, 1000)
	print('this is the', i + 1, 'random number:', r)
