#
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['sword', 'rope', 'book', 'scroll', 'gold coin', 'ruby', 'gold coin']

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print("Total number of items: " + str(item_total) + "\n")
	
#not an effective way of doing this 35 steps
def add_to_inventory(given_list, given_dictionary):
	new = given_dictionary.copy()
	for k, v in given_dictionary.items():
		for key in given_list:
			if key == k:
				new[k] += 1
			else:
				new.setdefault(key, 1)
			print(new)
	return new

displayInventory(stuff)
stuff = add_to_inventory(dragon_loot, stuff)
displayInventory(stuff)
