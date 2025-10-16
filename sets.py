# Sets are unordered collections of unique NO Duplicates elements in Python. They are defined using curly braces {} or the set() function.
# Creating a set
fruit_set = {"apple", "banana", "cherry"}
print("Fruit set:", fruit_set)

# Checking for existence of an item
if "banana" in fruit_set:
    print("Banana is in the set.")
# Adding an item to the set
fruit_set.add("orange")
print("After adding orange:", fruit_set)

# Adding multiple items to the set
fruit_set.update({"kiwi", "grape"})
print("After adding kiwi and grape:", fruit_set)

# Removing an item from the set
fruit_set.remove("apple")  # Raises KeyError if item not found  
print("After removing apple:", fruit_set)
fruit_set.discard("banana")  # Does not raise an error if item not found
print("After discarding banana:", fruit_set)

# If you are not sure if the item is in the set, use discard() to avoid errors
fruit_set.discard("pineapple")  # No error even though pineapple is not in the set
print("After trying to discard pineapple:", fruit_set)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
set_union = set_a | set_b
print("Union:", set_union)
print(set_a.union(set_b))  # Alternative way to do union    

# Intersection
set_intersection = set_a & set_b
print("Intersection:", set_intersection)
print(set_a.intersection(set_b))  # Alternative way to do intersection

# Difference
set_difference = set_a - set_b
print("Difference:", set_difference)
print(set_a.difference(set_b))  # Alternative way to do difference

print("\n" + "="*60)
print("PARTY ORGANIZATION CHALLENGE")
print("="*60)

# Create two sets for party organization
invited_friends = {"alex", "sam", "Leo", "Mina"}
rsvped = {"Mina", "sam", "Jordan"}

print("Invited friends:", invited_friends)
print("RSVPed guests:", rsvped)

# Print everyone who was invited as a union (all people involved)
all_people = invited_friends.union(rsvped)
print("\nEveryone involved (union):", all_people)

# Print everyone who RSVPed
print("Everyone who RSVPed:", rsvped)

# Those who haven't replied yet (difference)
havent_replied = invited_friends - rsvped
print("Those who haven't replied yet:", havent_replied)

# Add two new names to invited_friends
invited_friends.add("sarah")
invited_friends.add("mike")
print("\nAfter adding Sarah and Mike to invited list:", invited_friends)

# One person canceled - remove them from rsvped
rsvped.discard("Jordan")  # Jordan canceled
print("After the GOAT Michael Jordan canceled:", rsvped)

# Print how many total confirmed guests are attending
print(f"\nTotal confirmed guests attending: {len(rsvped)}")

# Check if Leo is coming
if "Leo" in rsvped:
    print("Great! Leo confirmed attendance.")
else:
    print("Leo hasn't confirmed yet or isn't coming.")
