def sentence(theList):
	string = ''
	for i in range(len(theList)):
		if i < len(theList) -1:
			string += theList[i] + ', '
		else:	
			string += 'and ' + theList[i]
	print(string)
		 
inputList = []

while True:
	print('add a list item, or leave blank to stop!')
	listItem = input()
	if listItem:
		inputList.append(listItem)
	else:
		break;

if inputList == []:
	print('You did not make a list :(')
else:		
	sentence(inputList)
