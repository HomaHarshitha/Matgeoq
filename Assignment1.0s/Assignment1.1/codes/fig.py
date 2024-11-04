import matplotlib.pyplot as plt

# Read the displacement vector from plot.txt
with open("points.txt", "r") as file:
    lines = file.readlines()
    dx = float(lines[0].split('=')[1])
    dy = float(lines[1].split('=')[1])

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the displacement vector
ax.quiver(0, 0, dx, dy, angles='xy', scale_units='xy', scale=1, color='r', label='Displacement Vector')

# Plot origin and endpoint of the displacement vector
ax.plot(0, 0, 'ko', label='Origin')  # origin
ax.plot(dx, dy, 'go', label='Endpoint')  # endpoint

# Annotate the origin and endpoint
ax.annotate('Origin', (0, 0), textcoords="offset points", xytext=(10,10), ha='center', fontsize=12, color='black')
ax.annotate(f'({dx:.1f}, {dy:.1f})', (dx, dy), textcoords="offset points", xytext=(-70,-10), ha='center', fontsize=12, color='green')

# Plot cardinal directions
ax.annotate('N', xy=(0, 15), xytext=(0, 20), ha='center', fontsize=12, color='blue')
ax.annotate('S', xy=(0, -15), xytext=(0, -20), ha='center', fontsize=12, color='blue')
ax.annotate('E', xy=(15, 0), xytext=(20, 0), ha='center', fontsize=12, color='blue')
ax.annotate('W', xy=(-15, 0), xytext=(-20, 0), ha='center', fontsize=12, color='blue')

# Set limits and labels
ax.set_xlim(min(dx - 10, -50), max(dx + 10, 10))
ax.set_ylim(min(dy - 10, -50), max(dy + 10, 10))
ax.set_xlabel('West-East (km)')
ax.set_ylabel('South-North (km)')
ax.grid(True)

# Set aspect ratio to be equal
ax.set_aspect('equal')

# Show legend and plot
plt.title('Displacement Vector Representation')
plt.legend()
plt.show()

