// PROJECT EULER - PROBLEM 14
// LONGEST COLLATZ SEQUENCE

// https://projecteuler.net/problem=14


// The following iterative sequence is defined for the set of positive integers:

//       n -> n/2 (n is even)
//       n -> 3n+1 (n is odd)

// Using the rule above and starting with 13, we generate the following sequence:

//       13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

// It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
// Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

// Which starting number, under one million, produces the longest chain?

// NOTE: Once the chain starts the terms are allowed to go over one million.


#include <stdio.h>

unsigned int next(unsigned int term);


int main(void){
    const int maxstart = 1000000;
    unsigned int term;
    int start, longest;
    int count, largestcount=0, counthist[maxstart];
    
    counthist[0]=0;
    counthist[1]=0;

    for (start=2; start<maxstart; start++){
        count = 0;
        term = start;
        while (term >= start){
            term = next(term);
            count++;
        }

        count = count + counthist[term];
        counthist[start] = count;

        if (count > largestcount){
            largestcount = count;
            longest = start;
        }
    }

    printf("%i\n", longest);

}


unsigned int next(unsigned int term){
    if (term%2 == 0){
        return term/2;
    }
    else {
        return 3*term + 1;
    }
}

