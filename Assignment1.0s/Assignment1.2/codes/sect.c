#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "matfun.h" // Your custom matrix function library

int main() {
    // Points A (2, 3) and B (6, -3)
    double **A = createMat(2, 1); // Create a 2x1 matrix for point A
    A[0][0] = 2;
    A[1][0] = 3;
    
    double **B = createMat(2, 1); // Create a 2x1 matrix for point B
    B[0][0] = 6;
    B[1][0] = -3;
    
    // Given point P(4, m)
    double **P = createMat(2, 1); // Create a 2x1 matrix for point P
    P[0][0] = 4;
    P[0][1] = 0;

    // Calculate the ratio k
    double k = (P[0][0] - A[0][0]) / (B[0][0] - P[0][0]); // Calculate ratio k

    // Find the y-coordinate (m) using the section formula
    double **result = Matsec(A, B, 2, k); // Use the section formula to find m
    P[1][0] = result[1][0]; // Update the y-coordinate of P
    // Free allocated memory
    for (int i = 0; i < 2; i++) {
        free(A[i]);
        free(B[i]);
        free(result[i]);
    }
    free(A);
    free(B);
    free(result);

    return 0;
}

