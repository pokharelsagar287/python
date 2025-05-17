#first videos

# print("HEllO WORLD!")
# print("sagar")
# # new code for testing purpose
# ''' hello sir'''
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

#unit conversion by package pint


# from pint import UnitRegistry
# import matplotlib.pyplot as plt
# a = UnitRegistry()
# # taking input from user
# length_value = float(input("Enter the length in meters: "))
# # converting to different units
# length = length_value * a.meter
# print(length.to('kilometers'))
# print(length.to('foot')) 
# p = length.to('kilometer').magnitude
# q = length.to('foot').magnitude


# #plotting the values using matplotlib
# units = ['Meters', 'Kilometers', 'Feet']
# values = [length_value, p, q]

# plt.bar(units, values, color=['blue', 'green', 'orange'])
# plt.title("Length Conversion")
# plt.xlabel("Units")
# plt.ylabel("Value")
# plt.grid(True)
# plt.show()

import tkinter as tk
from tkinter import messagebox

def estimate_materials():
    try:
        length = float(entry_length.get())
        breadth = float(entry_breadth.get())
        thickness = float(entry_thickness.get())

        volume = length * breadth * thickness
        shrinkage = 0.33
        dry_volume = volume * (1 + shrinkage)

        cement_ratio = 1
        sand_ratio = 2
        aggregate_ratio = 4
        total_ratio = cement_ratio + sand_ratio + aggregate_ratio

        cement_volume = (cement_ratio / total_ratio) * dry_volume
        sand_volume = (sand_ratio / total_ratio) * dry_volume
        aggregate_volume = (aggregate_ratio / total_ratio) * dry_volume

        cement_bags = cement_volume / 0.035
        sand_bags = sand_volume / 0.035

        result_text.set(f"Estimated quantities for 1 cubic meter of concrete:\n"
                        f"Cement: {cement_bags:.1f} bags\n"
                        f"Sand: {sand_bags:.2f} bags\n"
                        f"Aggregate: {aggregate_volume:.2f} cubic meters"
        )
        messagebox.showinfo("Estimation Result", result_text.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
# Create GUI window
root = tk.Tk()
root.title("Material Quantity Estimator")
root.geometry("350x250")

# Define result_text as a StringVar
result_text = tk.StringVar()

# Input fields
tk.Label(root, text="Length (m):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1)

tk.Label(root, text="Breadth (m):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_breadth = tk.Entry(root)
entry_breadth.grid(row=1, column=1)

tk.Label(root, text="Thickness (m):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_thickness = tk.Entry(root)
entry_thickness.grid(row=2, column=1)

# Button
btn_calculate = tk.Button(root, text="Estimate Materials", command=estimate_materials)
btn_calculate.grid(row=3, columnspan=2, pady=20)

# Run the GUI
root.mainloop()

# #Material Quantity Estimator

# length = input("Enter the length of the slab in meters: ")
# breadth = input("Enter the breadth of the slab in meters: ")
# thickness = input("Enter the thickness of the slab in meters: ")

# volume = float(length) * float(breadth) * float(thickness)
# print("\nVolume of the slab is: ", volume, "cubic meters")

# # assume 33% shrinakage of concrete
# shrinkage = 0.33
# dryVolume = volume * (1 + shrinkage)

# #mix ratio of concrete
# cement_ratio = 1
# sand_ratio = 2
# aggregate_ratio = 4
# total_ratio = cement_ratio + sand_ratio + aggregate_ratio

# #calculate the quantity of cement, sand and aggregate

# cement_volume = (cement_ratio / total_ratio) * dryVolume
# sand_volume = (sand_ratio / total_ratio) * dryVolume
# aggregate_volume = (aggregate_ratio / total_ratio) * dryVolume

# #convert cement volume and sand volume to bags
# cement_bags = cement_volume / 0.035
# sand_bags = sand_volume / 0.035

# #print the results
# print("\nEstimated quantities for 1 cubic meter of concrete:")
# print(f"Cement: {cement_bags:.1f} bags")
# print(f"Sand: {sand_bags:.2f} bags")
# print(f"Aggregate: {aggregate_volume:.2f} cubic meters")




