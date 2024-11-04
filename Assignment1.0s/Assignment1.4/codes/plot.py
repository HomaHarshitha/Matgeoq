import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libdc.so')

# Define the argument and return types for the C function
lib.findDirectionCosines.argtypes = [ctypes.POINTER(ctypes.c_double),
                                     ctypes.POINTER(ctypes.c_double),
                                     ctypes.POINTER(ctypes.c_double)]

def find_direction_cosines(point1, point2):
    # Convert Python lists to ctypes arrays
    p1 = (ctypes.c_double * 3)(*point1)
    p2 = (ctypes.c_double * 3)(*point2)
    direction_cosines = (ctypes.c_double * 3)()

    # Call the C function
    lib.findDirectionCosines(p1, p2, direction_cosines)

    # Convert the result back to a Python list
    return [direction_cosines[0], direction_cosines[1], direction_cosines[2]]

# Points in 3D space
point1 = [-2, 4, -5]
point2 = [1, 2, 3]

# Get direction cosines from C function
direction_cosines = find_direction_cosines(point1, point2)

# Plotting the points and direction vector
fig = plt.figure(figsize=(10, 8))  # Increased figure size
ax = fig.add_subplot(111, projection='3d')

# Plot point1 and point2
ax.scatter(point1[0], point1[1], point1[2], color='blue', label="Point 1")
ax.scatter(point2[0], point2[1], point2[2], color='green', label="Point 2")

# Annotate the points with coordinates
ax.text(point1[0], point1[1], point1[2], f'({point1[0]}, {point1[1]}, {point1[2]})', 
        color='blue', fontsize=12, ha='right')
ax.text(point2[0], point2[1], point2[2], f'({point2[0]}, {point2[1]}, {point2[2]})', 
        color='green', fontsize=12, ha='right')

# Plot the direction vector
direction_vector = np.array(point2) - np.array(point1)
ax.quiver(point1[0], point1[1], point1[2],
          direction_vector[0], direction_vector[1], direction_vector[2],
          color='red', label='Direction Vector')

# Labels and legend
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()

# Show plot
plt.show()

