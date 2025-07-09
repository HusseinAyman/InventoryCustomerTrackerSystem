# -------------------------
# Full Inventory and Customer Tracker System
# -------------------------

inventory = {}
purchases = []
customer_names = set()

# Function to add one product from admin input
def add_product():
    print("\nEnter product details:")
    try:
        pid = input("Product ID: ").strip()
        if pid in inventory:
            print("Product ID already exists. Choose a unique ID.")
            return

        name = input("Product Name: ").strip()
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
        categories_input = input("Categories (comma-separated): ")
        categories = {cat.strip().lower() for cat in categories_input.split(',')}

        inventory[pid] = (name, price, qty, categories)
        print(f"Product '{name}' added successfully.")

    except ValueError:
        print("Invalid input. Please enter numbers correctly for price and quantity.")

# Function to display all products
def view_products():
    print("\n--- Product List ---")
    if not inventory:
        print("No products in inventory.")
        return
    for pid, (name, price, qty, categories) in inventory.items():
        print(f"ID: {pid}")
        print(f"  Name: {name}")
        print(f"  Price: {price}")
        print(f"  Quantity: {qty}")
        print(f"  Categories: {', '.join(categories)}")
        print("----------------------------")

# Function to search products by category
def search_by_category(category):
    found = False
    print(f"\nProducts in category '{category}':")
    for pid, (name, price, qty, cats) in inventory.items():
        if category.lower() in cats:
            print(f"- {name} (ID: {pid}, Price: {price}, Quantity: {qty})")
            found = True
    if not found:
        print("No products found in this category.")

# Function to handle a customer purchase
def handle_purchase():
    name = input("Enter customer name: ").strip()
    customer_names.add(name)
    items = []
    total = 0.0

    while True:
        pid = input("Enter product ID to purchase (or 'done' to finish): ").strip()
        if pid.lower() == 'done':
            break
        if pid not in inventory:
            print("Invalid product ID. Try again.")
            continue

        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity. Must be a positive integer.")
            continue

        name_, price, stock, cats = inventory[pid]
        if qty > stock:
            print(f"Not enough stock. Only {stock} left.")
            continue

        inventory[pid] = (name_, price, stock - qty, cats)
        items.append((pid, qty))
        total += price * qty

    if items:
        purchases.append({"name": name, "items": items, "total": total})
        print(f"Purchase complete. Total: ${total:.2f}")
    else:
        print("No items purchased.")

# Function to save purchases to file
def save_purchases():
    try:
        with open("purchases.txt", "w") as f:
            for p in purchases:
                f.write(f"Customer: {p['name']}\n")
                for pid, qty in p['items']:
                    name_, price, _, _ = inventory.get(pid, ("Unknown", 0.0, 0, set()))
                    f.write(f"- {name_} (x{qty})\n")
                f.write(f"Total: ${p['total']:.2f}\n\n")
        print("Purchases saved to purchases.txt")
    except Exception as e:
        print("Error saving purchases:", e)

# Function to save inventory to file
def save_inventory():
    try:
        with open("inventory.txt", "w") as f:
            for pid, (name, price, qty, cats) in inventory.items():
                f.write(f"{pid},{name},{price},{qty},{'|'.join(cats)}\n")
        print("Inventory saved to inventory.txt")
    except Exception as e:
        print("Error saving inventory:", e)

# Function to generate summary report
def generate_report():
    print("\n--- Summary Report ---")
    print(f"Total Customers: {len(customer_names)}")
    print(f"Unique Customers: {', '.join(customer_names)}")
    total_sales = sum(p['total'] for p in purchases)
    print(f"Total Sales: ${total_sales:.2f}")
    if inventory:
        lowest_stock = min(inventory.items(), key=lambda x: x[1][2])
        print(f"Product with lowest stock: {lowest_stock[1][0]} ({lowest_stock[1][2]} left)")

# Main menu to interact with the system
def main_menu():
    while True:
        print("\n==== Main Menu ====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search by Category")
        print("4. Make Purchase")
        print("5. View Report")
        print("6. Save and Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            cat = input("Enter category to search: ").strip().lower()
            search_by_category(cat)
        elif choice == '4':
            handle_purchase()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            save_purchases()
            save_inventory()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
