from catalog import catalog

cart=[]
def print_header(text):
    print("="*60)
    print(text)
    print("="*60)

def print_menu():
    print("Menu:")
    print("1. -View Catalog")
    print("2. -Search Product")
    print("3. -View Cart")
    print("4. -Clear Cart")
    # More options can be added here
    print("Q - Quit")

def print_catalog():
    print("-Our Product Catalog:-")
    for prod in catalog:
        print(f"ID: {prod['id']} | Title: {prod['title'].ljust(15)} | Price: ${prod['price']:.2f}|")  
    answer = input("Type ID to add to cart (N to close) ")
    if answer != "N" and answer != "n":
        add_to_cart(answer)

def add_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod['id']) == str(prod_id):
            found = True
            cart.append(prod)
            print(f"Product with ID {prod_id} added to cart.")
            print(f"ID: {prod['id']} | Title: {prod['title'].ljust(15)} | Price: ${prod['price']:.2f}|")
            break
    if not found:
        print(f"ERROR: Product with ID {prod_id} not found.")

def search_product():
    search_term = input("Enter product name to search: ").lower()
    results = []
    for prod in catalog:
        if search_term in prod['title'].lower():
            results.append(prod)
    if results:
        print("Search Results:")
        for prod in results:
            print(f"ID: {prod['id']} | Title: {prod['title'].ljust(15)} | Price: ${prod['price']:.2f}|")
        choice = input("Do you want to add an item to your cart? (y/n): ")
        if choice.lower() == "y":
            prod_id = input("Enter the ID of the product to add: ")
            add_to_cart(prod_id)
    else:
        print("No products found matching your search.")

# Main program loop for the store
def main():
    options = ""
    while options != "q" and options != "Q":
        print_header("WELCOME TO THE ONLINE STORE")
        print_menu()
        options = input("Select an option: ")
        if options == "1":
            print_catalog()
        elif options == "2":
            search_product()
        elif options == "3":
            view_cart()
        elif options == "4":
            clear_cart()
        elif options.lower() == "q":
            print("Exiting the store. Thank you for visiting!")
        else:
            print("Invalid option. Please try again.")

def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your Cart:")
        for prod in cart:
            print(f"ID: {prod['id']} | Title: {prod['title'].ljust(15)} | Price: ${prod['price']:.2f}|")
        total = sum(item['price'] for item in cart)
        print(f"Total Amount: ${total:.2f}")
        cart_total()

def cart_total():
    total=0
    for prod in cart:
        total += prod['price']
    print(f"Total Amount: ${total:.2f}")


def clear_cart():
    cart.clear()
    print("Cart has been cleared.")
    input("Press Enter to return to the main menu.")
   
if __name__ == "__main__":
    main()    
