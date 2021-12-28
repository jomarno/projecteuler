! PROJECT EULER - PROBLEM 21
! AMICABLE NUMBERS

! Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
! If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

! For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55,110; therefore d(220) = 284.
! The proper divisors of 284 are 1,2,4,71 and 142; so d(284) = 220.

! Evaluate the sum of all the amicable numbers under 10000.

function divsum(n) result(s)
    integer , intent(in) :: n
    integer  :: i, s
    
    s = 0
    do i = 1, n/2
        if ( mod(n,i) == 0 ) then
            s = s + i
        end if
    end do

end function divsum

program main
    implicit none
    integer , parameter :: n = 10000
    integer , dimension(n) :: s
    integer  :: divsum, amsum = 0, i

    do i = 1, n

        s(i) = divsum(i)
        
        if ( s(i) < i .and. s(s(i)) == i ) then
            amsum = amsum + i + s(i)
        end if

    end do

    print *, amsum
    
end program main