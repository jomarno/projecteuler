// PROJECT EULER - PROBLEM 12
// HIGHLY DIVISIBLE TRIANGULAR NUMBER

// The sequence of triangle numbers is generated by adding the natural numbers.
// So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
// The first ten terms would be:

//       1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

// Let us list the factors of the first seven triangle numbers:

//        1:1
//        3:1,3
//        6:1,2,3,6
//       10:1,2,5,10
//       15:1,3,5,15
//       21:1,2,7,21
//       28:1,2,4,7,14,28

// We can see that 28 is the first triangle number to have over five divisors.

// What is the value of the first triangle number to have over five hundred divisors?


#include <stdio.h>
#include <math.h>

int ndivs(int k);

int main(void) {
    int i=1, n=1, tri=1;
    
    while (n < 500) {
        i++;
        tri = tri + i;
        n = ndivs(tri);
    }

    printf("%i\n", tri);

}

int ndivs(int k) {
    int i, n;

    n = 2;


    for (i=2; i<=(int)floor(sqrt((float)k)); i++) {
        if (k%i == 0) {
            n = n + 2;
        }
    }

    return n;
}

