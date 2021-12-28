// PROJECT EULER - PROBLEM 6
// SUM SQUARE DIFFERENCE

// The sum of the squares of the first ten natural numbers is,

//     1² + 2² + ... . 10² = 385

// The square of the sum of the first ten natural numbers is,

//     (1 + 2 + ... + 10)² = 55² = 3025

// Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
// 3025 - 385 = 2640

// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


#include <stdio.h>

int triangular(int n);
int pyramidal(int n);
int sumSquareDiff(int n);


int main(void) {
    printf("%i\n", sumSquareDiff(100));
}


// Return the nth triangular number T(n) = 1 + 2 + 3 + ... + n
int triangular(int n) {
    return n*(n+1)/2;
}

// Return the nth pyramidal number P(n) = 1 + 4 + 9 + ... + n^2
int pyramidal(int n) {
    return triangular(n)*(2*n+1)/3;
}

// Return the square of the sum minus the sum of the squares
int sumSquareDiff(int n) {
    return triangular(n)*triangular(n) - pyramidal(n);
}

