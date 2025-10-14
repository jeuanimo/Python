# Shopping List Challenge

# Create a shopping list
shopping_list = ["apples", "bread", "milk", "eggs", "bananas"]

print("Jeuan's shopping list:", shopping_list)
print()

# Print the first and last item from the list
print("First item:", shopping_list[0])
print("Last item:", shopping_list[-1])
print()

# Replace the second item in list with something else
print("Before replacement - Second item:", shopping_list[1])
shopping_list[1] = "cheese"
print("After replacement - Second item:", shopping_list[1])
print("Updated shopping list:", shopping_list)
print()

# Add a new item called "ice cream" to the end of the list
shopping_list.append("ice cream")
print("After adding my big back snack ice cream:", shopping_list)
print()

# Remove one item of your choice from the list
removed_item = shopping_list.remove("eggs")
print("After removing those expensive eggs:", shopping_list)
print()

# Print how many items are in the list
print("Number of items in Jeuan's shopping list:", len(shopping_list))
print("Final shopping list:", shopping_list)
