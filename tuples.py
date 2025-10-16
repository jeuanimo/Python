# Tuples are immutable sequences in Python that can store a collection of items. They are similar to lists, but unlike lists, tuples cannot be modified after their creation. Tuples are defined using parentheses ().

# Creating a tuple
my_tuple = ("apple", "banana", "cherry")
print("My tuple:", my_tuple)

# Accessing elements in a tuple
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])
print("Third element:", my_tuple[2])

# Check if an item exists in the tuple
if "banana" in my_tuple:
    print("Banana is in the tuple.")


# Length of the tuple
print("Length of the tuple:", len(my_tuple))

# Single element tuple (note the comma)
single_element_tuple = ("chair",)   
print("Single element tuple:", single_element_tuple)

# Nested tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combined_tuple = (tuple1, tuple2)
print("Combined tuple:", combined_tuple)

# Travel bag tuple challenge
travel_bag = ("shoes", "clothes", "toothbrush", "passport", "sunglasses", "Trinity action figure")
print("\nTravel bag contents:", travel_bag)

# Check if "shoes" is in the travel bag
if "shoes" in travel_bag:
    print("Great! You are ready to walk.")
else:
    print("Neo, you forgot to pack your shoes!")

# Print the second and fourth items in the travel bag
print("\nSecond item in travel bag:", travel_bag[1])
print("Fourth item in travel bag:", travel_bag[3])

# Make a new tuple called "essentials" with 3 must-have items
essentials = ("wallet", "keys", "matrix")
print("\nEssentials tuple:", essentials)

# Combine both tuples into one called "final_bag"
final_bag = travel_bag + essentials
print("\nFinal bag contents:", final_bag)

# Print how many total items you have
print("Total items in final bag:", len(final_bag))

# Print last item in your final bag
print("Last item in final bag:", final_bag[-1])