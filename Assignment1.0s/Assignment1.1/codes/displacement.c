#include <stdio.h>
#include <math.h> // For trigonometric functions

// Function prototypes
void calculate_displacement(float distance, float angle_degrees, float *dx, float *dy);

int main() {
    FILE *ptr;  // File pointer for file operations
    ptr = fopen("points.txt", "w"); // Open file for writing
    
    // Check if the file was opened successfully
    if (ptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    float distance = 40.0f; // Distance in km
    float angle_degrees = -120.0f; // Angle in degrees (30 degrees west of south, so -120 degrees from the positive x-axis)
    float dx, dy; // Components of the displacement vector

    // Calculate the displacement vector components
    calculate_displacement(distance, angle_degrees, &dx, &dy);

    // Write results to the file
    fprintf(ptr, "x = %.2f\n", dx);
    fprintf(ptr, "y = %.2f\n", dy);

    // Close the file
    fclose(ptr);
    return 0;
}

// Function to calculate the components of the displacement vector
void calculate_displacement(float distance, float angle_degrees, float *dx, float *dy) {
    // Convert angle to radians
    float angle_radians = angle_degrees * M_PI / 180.0f;

    // Calculate components
    *dx = distance * cosf(angle_radians); // x-component (east-west axis)
    *dy = distance * sinf(angle_radians); // y-component (north-south axis)
}

