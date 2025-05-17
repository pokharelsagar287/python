materials = [
    {"name": "Cement", "rate": 950, "stock": 120},
    {"name": "Sand", "rate": 45, "stock": 30},
    {"name": "Steel", "rate": 110, "stock": 80},
    {"name": "Bricks", "rate": 12, "stock": 500},
    {"name": "Gravel", "rate": 60, "stock": 15}
]

#fucntion to display material on table neatly

def display_materials(materials):
    print("\nMaterial Stock and Rates")
    print("-" * 40)
    print(f"{'Material':<10} {'Rate (Rs)':<15} {'Stock (units)':<15}")
    print("-" * 40)
    for material in materials:
        print(f"{material['name']:<10} {material['rate']:<15} {material['stock']:<15}")
    print("-" * 40)
    print("Total Stock Value: Rs", sum(m['rate'] * m['stock'] for m in materials))
    print("-" * 40)

#function to sort materials by stock
def sort_materials_by_stock(materials):
    return sorted(materials, key=lambda x: x['stock'], reverse=True)
#function to sort materials by rate
def sort_materials_by_rate(materials):
    return sorted(materials, key=lambda x: x['rate'], reverse=True)
#function to sort materials by name
def sort_materials_by_name(materials):
    return sorted(materials, key=lambda x: x['name'])
#function to sort materials by low rate
def sort_materials_by_low_rate(materials):
    return sorted(materials, key=lambda x: x['rate'])



#main function to control the program
def main():
    while True:
        print("\nMaterial Stock Management")
        print("1. Display Materials")
        print("2. Sort Materials by Stock")
        print("3. Sort Materials by High Rate")
        print("4. Sort Materials by Name")
        print("5. Sort Materials by Low Rate")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_materials(materials)
        elif choice == '2':
            sorted_materials = sort_materials_by_stock(materials)
            display_materials(sorted_materials)
        elif choice == '3':
            sorted_materials = sort_materials_by_rate(materials)
            display_materials(sorted_materials)
        elif choice == '4':
            sorted_materials = sort_materials_by_name(materials)
            display_materials(sorted_materials)
        elif choice == '5':
            sorted_materials = sort_materials_by_low_rate(materials)
            display_materials(sorted_materials)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main() 