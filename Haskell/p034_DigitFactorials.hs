-- PROJECT EULER - PROBLEM 34
-- DIGIT FACTORIALS

-- https://projecteuler.net/problem=34


-- 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

-- Find the sum of all numbers which are equal to the sum of the factorial of their digits.

-- Note: As 1! = 1 and 2! = 2 are not sums they are not included.


factorials :: [Int]
factorials = [product [1..x] | x <- [0..9]] 

isFactorion :: Int -> Bool
isFactorion x = x == sfd x
    where
        sfd 0 = 0
        sfd x = sfd (x `div` 10) + factorials !! (x `mod` 10)

main :: IO ()
main = print (sum [x | x <- [10..10^7], isFactorion x])