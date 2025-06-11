# TODO: Create a dictionary representing the inventory with vegetables as keys and their quantities as values
vegetables = {'zucchini':2, 'onion':5, 'potato':9}

# TODO: Calculate the maximum number of a single type of vegetable in the inventory
max_veg = max(vegetables, key=vegetables.get)
max_veg_count = max(vegetables.values())
# TODO: Print out the maximum number of any vegetable in the inventory
print(f"{max_veg.title()} has the most number of items with a count of {max_veg_count}.")
