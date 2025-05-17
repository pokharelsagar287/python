#create material dictionary
materials = {
    "cement": "Rs. 550 per bag",
    "sand": "Rs. 1200 per cubic meter",
    "gravel": "Rs. 900 per cubic meter",
    "steel": "Rs. 80 per kg",
    "bricks": "Rs. 15 per piece",
    }

material_name = input("Enter the name of the material: ").lower()
#check if material is in the dictionary
if material_name in materials:
    print(f"The price of {material_name} is {materials[material_name]}")
else:
    print("Material not found")
