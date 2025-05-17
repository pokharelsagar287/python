length = []  # Initialize length as an empty list
sum = 0
for i in range(5):  # Loop to get 5 lengths
    l= float(input("Enter the length of the slab in mm: "))
    l_meters = l / 1000  # Convert length from mm to meters 
    length.append(l_meters)  # Append the converted length to the list
    # Calculate the sum of lengths in meters
    sum += l_meters
   
print("All Length in meters: ", length)
print("Sum of lengths in m: ", sum)

