#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "matfun.h"  // Include your matfun.h path

void generate_triangle_points(double *A, double *B, double *C) {
    double angle_B = 45.0 * (M_PI / 180.0); // Convert degrees to radians
    double angle_C = 30.0 * (M_PI / 180.0);
    double angle_A = 105.0 * (M_PI / 180.0); // Angle A

    // Lengths
    double BC = 7.0;
    double AB = (BC * sin(angle_C)) / sin(angle_A); // Calculate AB using Law of Sines
    double AC = (BC * sin(angle_B)) / sin(angle_A); // Calculate AC

    // Coordinates
    B[0] = 0.0; // B (0, 0)
    B[1] = 0.0;

    C[0] = BC; // C (7, 0)
    C[1] = 0.0;

    // Point A
    A[0] = AB * cos(angle_B); // A_x
    A[1] = AB * sin(angle_B); // A_y
}

int main() {
    double A[2], B[2], C[2];
    
    generate_triangle_points(A, B, C);

    // Return values to Python
    return 0;
}

