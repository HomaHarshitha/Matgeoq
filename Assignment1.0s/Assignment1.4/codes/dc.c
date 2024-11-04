#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "matfun.h"
void freedoublepointer(double **p){
    for(int i=0;i<3;i++){
        free(p[i]);
    }
    free(p);
}
// Export this function for ctypes in Python
void findDirectionCosines(double *point1, double *point2, double *directionCosines) {
    double **p1 = createMat(3, 1);
    double **p2 = createMat(3, 1);
    double **directionVector;
    double **unitVector;
    double norm;

    // Initialize points
    p1[0][0] = point1[0];
    p1[1][0] = point1[1];
    p1[2][0] = point1[2];
    
    p2[0][0] = point2[0];
    p2[1][0] = point2[1];
    p2[2][0] = point2[2];

    // Compute direction vector: p2 - p1
    directionVector = Matsub(p2, p1, 3, 1);

    // Compute the norm of the direction vector
    norm = Matnorm(directionVector, 3);

    // Scale the direction vector to get the unit vector (direction cosines)
    unitVector = Matscale(directionVector, 3, 1, 1.0 / norm);

    // Store the direction cosines
    directionCosines[0] = unitVector[0][0];
    directionCosines[1] = unitVector[1][0];
    directionCosines[2] = unitVector[2][0];

    // Free allocated memory
    freedoublepointer(p1);
    freedoublepointer(p2);
    freedoublepointer(directionVector);
    freedoublepointer(unitVector);
}
