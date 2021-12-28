// PROJECT EULER - PROBLEM 3
// LARGEST PRIME FACTOR

// The prime factors of 13195 are 5, 7, 13 and 29.

// What is the largest prime factor of the number 600851475143?


#include <stdio.h>

long largestPrimeFactor(long n);


int main(void) {

    printf("%i\n", largestPrimeFactor(600851475143));
    
}


long largestPrimeFactor(long n) {
    
    if (n%2==0) {
        while (n%2 == 0) {
            n = n/2;
        }
    }
    
    long k = 3;
    
    while (k*k <= n) {
        if (n%k == 0) {
            while (n%k == 0) {
                n = n/k;
            }
        }

        k += 2;
    }
    
    return n;
}

