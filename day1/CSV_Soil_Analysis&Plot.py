import csv


#initialize lists to store the values
moisture_values = []
density_values = []

#open the CSV file
with open('soil_data.csv', 'r') as file:
    #create a CSV reader object
    #since dictreader is used, the first row of the file should contain the column names
    reader = csv.DictReader(file)    
    
    
    #read the data from the file
    for row in reader:
        #append the values to the lists
        moisture_values.append(float(row['Moisture']))
        density_values.append(float(row['Density']))

#calculate the average moisture and density
average_moisture = sum(moisture_values) / len(moisture_values)
maximum_density = max(density_values)
minimum_density = min(density_values)

#print the results
print(f"Average Moisture: {average_moisture:.2f}")
print(f"Maximum Density: {maximum_density:.2f}")
print(f"Minimum Density: {minimum_density:.2f}")


#plot the data
import matplotlib.pyplot as plt
plt.plot(moisture_values, density_values, marker='o', linestyle='-', color='b')
plt.title("Moisture vs Density")
plt.xlabel("Moisture (%)")
plt.ylabel("Density (kg/m^3)")
plt.grid(True)
plt.savefig("moisture_vs_density.png")
plt.show()