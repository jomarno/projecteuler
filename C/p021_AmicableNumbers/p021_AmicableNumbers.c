// PROJECT EULER - PROBLEM 21
// AMICABLE NUMBERS

// Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
// If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

// For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55,110; therefore d(220) = 284.
// The proper divisors of 284 are 1,2,4,71 and 142; so d(284) = 220.

// Evaluate the sum of all the amicable numbers under 10000.


#include <stdio.h>

int divsum(int n);

int main(void) {
    const int n=10000;
    int s[n], amsum=0, i;

    for (i=1; i<=n; i++) {
        
        s[i-1] = divsum(i);

        if ( s[i-1]<i && s[s[i-1]-1]==i ) {
            amsum = amsum + i + s[i-1];
        }
    }

    printf("%i\n", amsum);
}

int divsum(int n) {
    int i, s;
    s = 0;
    for (i=1; i<=n/2; i++) {
        if (n%i == 0) {
            s+=i;
        }
    }
    return s;
}

