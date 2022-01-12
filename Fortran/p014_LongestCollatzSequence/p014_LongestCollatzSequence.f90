! PROJECT EULER - PROBLEM 14
! LONGEST COLLATZ SEQUENCE

! https://projecteuler.net/problem=14


! The following iterative sequence is defined for the set of positive integers:

!       n -> n/2 (n is even)
!       n -> 3n+1 (n is odd)

! Using the rule above and starting with 13, we generate the following sequence:

!       13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

! It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
! Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

! Which starting number, under one million, produces the longest chain?

! NOTE: Once the chain starts the terms are allowed to go over one million.


! This program calculates the Collatz sequence for all starting numbers from 2 to MAXSTART.
! The length of each sequence is obtained by incrementing COUNT every time a new term is calculated.
! To avoid recalculating terms, sequence length for each starting number is stored in vector COUNTHIST.
! When a new term in the current sequence drops below its starting number (therefore becoming the starting 
! number of a previous sequence) the remaining length is looked up in COUNTHIST and summed to COUNT.

program main
    implicit none
    integer (kind=4), parameter :: maxstart=1000000
    integer (kind=4) :: start, longest
    integer (kind=8) :: term
    integer (kind=2) :: count, largestcount=0
    integer (kind=2), allocatable, dimension(:) :: counthist
    integer (kind=2), parameter :: one=1
    
    allocate(counthist(maxstart))
    
    counthist(1) = 0

    do start=2, maxstart
        
        count = 0
        term = start

        do while ( term >= start )
            call getnext(term)
            count = count + one
        end do

        count = count + counthist(term)
        counthist(start) = count

        if ( count > largestcount ) then
            largestcount = count
            longest = start
        end if

    end do

    print *, "LONGEST COLLATZ SEQUENCE"
    print *, " Starting term:", longest
    print *, "  Chain length:     ", largestcount + one

end program main

subroutine getnext(term)
    implicit none
    integer (kind=8) :: term
    if ( mod(term,2) == 0 ) then
        term = term/2
    else 
        term = 3*term + 1
    end if
end subroutine getnext