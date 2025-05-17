import matplotlib.pyplot as plt

length = 2.0
area = 0.01
E = 200e9

#creating load list

loads = list(range(1000, 2200, 1100))

#calculation displacement
displacements = []
for p in loads:
    # Calculate displacement
    delta = (p * length) / (E * area)
    displacements.append(delta)

# Plotting
plt.plot(loads, displacements, marker='o', color='blue', linestyle='--')
plt.title("Load vs Displacement")
plt.xlabel("Load (N)")
plt.ylabel("Displacement (m)")
plt.grid(True)
# Save the plot

plt.savefig("load_vs_displacement.png")
# Show the plot
plt.show()



