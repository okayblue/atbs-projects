import random

numberOfStreaks = 0

for experimentNumber in range(10000):
	# 100 values
	coinList = []
	for i in range(100):
		coinList.append(random.randint(0, 1))
	
	# check for streak of 6 in a row
	counter = 0
	# Start at index 1 as we're checking previous number
	for coin in range(1, len(coinList)): 
		if counter == 5: 
			numberOfStreaks += 1
			break
		elif coinList[coin] == coinList[coin - 1]:
			counter += 1
		else:
			counter = 0 
				
print('Chance of streak:  %s%%' % (numberOfStreaks / 100))
	
	
