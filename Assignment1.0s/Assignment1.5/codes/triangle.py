import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libtriangle.so')

# Define the function signature in C
lib.generate_triangle_points.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

# Prepare arrays to hold the triangle points A, B, C
A = (ctypes.c_double * 2)()
B = (ctypes.c_double * 2)()
C = (ctypes.c_double * 2)()

# Call the C function to generate the points
lib.generate_triangle_points(A, B, C)

# Convert C arrays to numpy arrays for easier plotting
A = np.array([A[0], A[1]])
B = np.array([B[0], B[1]])
C = np.array([C[0], C[1]])

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the triangle
triangle = plt.Polygon([A, B, C], closed=True, fill=None, edgecolor='r')
ax.add_patch(triangle)

# Set limits
buffer = 1  # Add some buffer for better visibility
ax.set_xlim(min(A[0], B[0], C[0]) - buffer, max(A[0], B[0], C[0]) + buffer)
ax.set_ylim(min(A[1], B[1], C[1]) - buffer, max(A[1], B[1], C[1]) + buffer)

# Ensure the aspect ratio is equal
ax.set_aspect('equal', adjustable='box')

# Annotate points A, B, C using annotate
plt.annotate(f'A({A[0]:.2f}, {A[1]:.2f})', xy=(A[0], A[1]), xytext=(A[0] + 0.1, A[1] + 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)
plt.annotate(f'B({B[0]:.2f}, {B[1]:.2f})', xy=(B[0], B[1]), xytext=(B[0] + 0.1, B[1] + 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)
plt.annotate(f'C({C[0]:.2f}, {C[1]:.2f})', xy=(C[0], C[1]), xytext=(C[0] + 0.1, C[1] + 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Add grid
plt.grid(True)

# Show the plot
plt.show()

