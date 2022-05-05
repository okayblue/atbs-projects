# game inventory!

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
	print('Inventory:')
	
	itemTotal = 0
	
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		itemTotal += v
	print('Total number of items: ' + str(itemTotal))

def addToInventory(inventory, addedItems):
	for item in addedItems:
		inventory.setdefault(item, 0)
		inventory[item] += 1
	
displayInventory(stuff)
addToInventory(stuff, dragonLoot)
displayInventory(stuff)


