# Function to load inventory from file
def load_inventory(filename):
    inventory = {}
    try:    
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 2:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                item, quantity = parts
                inventory[item] = int(quantity)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except ValueError:
        print("Error: The file format is incorrect. Each line should be 'item,quantity'.")
    return inventory

# Function to save inventory to file (overwrite)
def save_inventory(filename, inventory):
    try:
        with open(filename, 'w') as file:  # Changed 'a' to 'w'
            for item, quantity in inventory.items():
                file.write(f"{item},{quantity}\n")
        print(f"Inventory saved to {filename}.")
    except Exception as e:
        print(f"Error saving inventory: {e}")

# Function to display inventory
def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"  {item}: {quantity}")

# Function to update inventory
def update_inventory(inventory):
    name = input("Enter the name of the item: ").strip()
    try:
        quantity = int(input("Enter the quantity to add (use negative to remove): "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for quantity.")
        return
    inventory[name] = inventory.get(name, 0) + quantity
    if inventory[name] < 0:
        inventory[name] = 0
        print("Quantity can't be negative. Set to 0.")
    print(f"Updated inventory: {name} now has {inventory[name]} units.")

# Main program
def main():
    filename = 'inventory.txt'
    inventory = load_inventory(filename)
    

    while True:
        print("\nInventory Management System")
        print("1. Display Inventory")
        print("2. Update Inventory")
        print("3. Save Inventory")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            update_inventory(inventory)
        elif choice == '3':
            save_inventory(filename, inventory)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Only run the program if the file is executed directly
if __name__ == "__main__":
    main()

