import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libsect.so')

# Define the function prototype
lib.main.argtypes = []  # No arguments for main
lib.main.restype = ctypes.c_int  # Return type is int

def call_c_code():
    # Call the main function from C, which is expected to update the y-coordinate of P
    result = lib.main()  # This could be where you fetch or calculate the ratio, etc.
    return result

if __name__ == '__main__':
    # Coordinates of points A, B, and P
    A = np.array([2, 3])
    B = np.array([6, -3])
    P = np.array([4, 0])  # Initialize P, with y-coordinate starting at 0

    # Call the C function to get the value of m or update P
    call_c_code()  # This function can modify the coordinates or return relevant results
    
    # Plot the points and the line segment
    plt.figure(figsize=(10, 10))
    
    # Plot the line AB
    plt.plot([A[0], B[0]], [A[1], B[1]], 'ro-', label='Line AB')  
    
    # Plot and label point A
    plt.plot(A[0], A[1], 'bo', label='Point A')
    plt.annotate(f'A ({A[0]}, {A[1]})', (A[0], A[1]), textcoords="offset points", xytext=(-10,10), ha='center')
    
    # Plot and label point B
    plt.plot(B[0], B[1], 'go', label='Point B')
    plt.annotate(f'B ({B[0]}, {B[1]})', (B[0], B[1]), textcoords="offset points", xytext=(-10,-15), ha='center')
    
    # Plot and label point P (after calling C function)
    plt.plot(P[0], P[1], 'mo', label=f'Point P')
    plt.annotate(f'P ({P[0]}, {P[1]})', (P[0], P[1]), textcoords="offset points", xytext=(10,10), ha='center')
    
    # Set labels and plot properties
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.title('Plot of Points A, B, and P')
    plt.show()

