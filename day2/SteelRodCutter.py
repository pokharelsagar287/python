input_length = (input("Enter the length of the steel rod in meter (comma-separated): "))
lengths = [float(x) for x in input_length.split(",")]

rod_length = 12.0;
rods_used = 1;
remaining = rod_length
waste_list = []


#cutting process
for length in lengths:
    if length > rod_length:
        print(f"❌ Length {length} m is greater than rod length. Skipping.")
        continue
    if length <= remaining:
        remaining -= length
    else:
        waste_list.append(round(remaining, 2))  # waste of old rod
        rods_used += 1
        remaining = rod_length - length 

waste_list.append(round(remaining, 2))

#display resulta
print("\n✅ Steel Cutting Summary")
print("Total rods used:", rods_used)
print("Rod length:", rod_length)
print("Waste after each rod:")
for i, waste in enumerate(waste_list, start=1):
    print(f"  Rod {i}: {waste} m waste")
