class Product:
    def __init__(self, name, category, price, stock): # A class to represent the product and it's elements
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self): # A string to print out a product (inspired and learned from ChatGPT)
        return f"{self.name} ({self.category}) - Price: AED {self.price:.2f}, Stock: {self.stock}"

class VendingMachine:
    def __init__(self): # Initializes the vending machine and adds products, cart, and balance (connected to class product)
        self.products = {
            0: Product("Coca Cola", "Beverages", 3.00, 5),
            1: Product("Pepsi", "Beverages", 3.00, 4),
            2: Product("Water", "Beverages", 1.50, 10),
            3: Product("Lays", "Snacks", 2.50, 8),
            4: Product("Chocolate Bar", "Snacks", 5.00, 3),
            5: Product("Fanta", "Bevarages", 3.00, 6),
            6: Product("Oman Chips", "Snacks", 2.00, 15),
            7: Product("Pocari Sweat", "Bevarages", 3.50, 5),
            8: Product("Milk Tea", "Bevarages", 5.00, 6),
            9: Product("Doritos", "Snacks", 5.00, 6),
        }
        self.balance = 0
        self.cart = []
    
    def display_menu(self): # Defines what the main menu displays
        print("\nMain Menu:")
        print("[0] Add Items")
        print("[1] Add Money")
        print("[2] Checkout")
        print(f"Current Balance: AED {self.balance:.2f}")

    def display_products(self): # Displays products by category as shown in class Product, highly inspired by similar code from ChatGPT, highly practical as the products can be disorganzied when adding to the code
        print(f"\nAvailable Products by Category:")
        categories = {}
        for code, product in self.products.items():
            if product.category not in categories:
                categories[product.category] = [] # If the category is not in the dictionary, then it creates one 
            categories[product.category].append((code, product)) # Assigns the product to a list managed by category
        for category, items in categories.items(): # For loop that displays the Category and all related products and loops for each category
            print(f"Category: {category}")
            for code, product in items:
                print(f"[{code}] {product}")
    
    def add_money(self): # Allows the user to add money to pay for the products in cart
        print("\nAdd Money")
        print("[1] AED 1\n[5] AED 5\n[10] AED 10\n[20] AED 20\n[50] AED 50")
        try: # Using try for this function cancels the entire add_money function if the user inputs incorrectly
            amount = int(input("How much money will you add? "))
            if amount in [1, 5, 10, 20, 50]: # Checks if entered amount is valid
                self.balance += amount # Adds money to balance
                print(f"Added AED {amount}. New Balance: AED {self.balance:.2f}")
                money_again = int(input("[0] Continue to Menu, [1] Add More? ")) # Asks if you want to add more money
                if money_again == 1:
                    self.add_money()
                else:
                    return
            else: # Terminates function in case of invalid amount
                print("Invalid Amount. Please select from the available options. Terminating...")
        except ValueError: # In case the user inputs a word or invalid number
            print("Invalid Input. Please enter a valid number...")

    def select_product(self): # Function for selecting a product
        self.display_products() # Calls for the function to display products
        try:
            code = int(input("Enter the product code: "))
            if code in self.products: # Checks if code is valid for a product
                product = self.products[code] # Converts the code to the desired product
                if product.stock > 0: # Checks if the product is in stock
                    quantity = int(input(f"How many {product.name}(s) would you like? "))
                    if quantity <= product.stock: # Checks if the amount of the product is enough
                        total_cost = quantity * product.price # Calculates total
                        print(f"Total Cost: AED {total_cost:.2f}") 
                        self.cart.append((product, quantity)) # Adds the product and quantity to cart
                        print(f"Added {quantity} {product.name}(s) to cart.")
                        product.stock -= quantity # Deducts chosen amount from stock
                        food_again = int(input("[0] Continue to Menu, [1] Order Again? ")) # Asks if you want to order again
                        if food_again == 1:
                            self.select_product()
                        else:
                            return
                    else:
                        print(f"Not enough stock. Availabe Stock: {product.stock}")
                else:
                    print(f"{product.name} is out of stock")   
            else:
                print("Invalid product code...")
        except ValueError:
            print("Invalid input. Please enter a valid number...")
    
    def checkout(self): # Checkout, calculates total and and checks balance
        if not self.cart: # Checks if cart is empty, got from ChatGPT
            print("Your Cart is empty. Please add items before checkout.")
            return
        
        print("Receipt:") # Start of receipt
        total = 0 # Initiates a "total" variable
        for product, quantity in self.cart: # Pulls out each instance of product and quantity to calculate total
            cost = product.price * quantity
            print(f"{product.name} x{quantity} - AED {cost:.2f}")
            total += cost # Adds the the cost of goods from each iteration to the total

        if self.balance >= total: # Checks if the balance of the user is enough
            self.balance -= total # If balance is sufficient, deduct total cost from balance
            change = self.balance # Designates change
            print(f"Total: AED {total:.2f}")
            print(f"Change: AED {change:.2f}")
            print("Thank you for your purchase!")
            self.balance = 0 # Resets balance after releasing change like in a real vending machine
            self.cart.clear() # Clears cart
        else:
            print(f"Not enough balance. Please add AED {total - self.balance:.2f} more.") # Tells the user how much more is needed for their cart.
    
    def run(self): # The main loop where all of the functions work together
        while True: # Initiates the loop
            self.display_menu() # Initiates Menu, if any error occurs in any of the functions, it returns here
            try:
                choice = int(input("Select an option: ")) # Main part of the code, this part chooses which function to run
                if choice == 0:
                    self.select_product() # Runs select product function
                elif choice == 1:
                    self.add_money() # Runs add money function
                elif choice == 2:
                    self.checkout() # Runs checkout function and finalizes the purchase
                else:
                    print("Invalid option. Please select from the menu.")
            except ValueError: # Safety net in case any code does not work or if the user inputs something that could break the code, recommended by ChatGPT
                print("Invalid input. Please enter a number...")

if __name__ == "__main__": # Will only run when run by Python locally and not imported, solves issue of importing script as explained by ChatGPT
    vending_machine = VendingMachine() # As ChatGPT put as analogy, the class is the blueprint and the variable is building created from it, allowing access to its methods
    vending_machine.run() # Runs all the code