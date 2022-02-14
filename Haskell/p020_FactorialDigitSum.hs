-- PROJECT EULER - PROBLEM 20
-- FACTORIAL DIGIT SUM

-- https://projecteuler.net/problem=20


-- n! means n × (n − 1) × ... × 3 × 2 × 1

-- For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
-- and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

-- Find the sum of the digits in the number 100!


digitSum :: Integer -> Integer
digitSum 0 = 0
digitSum x = digitSum (x `div` 10) + (x `mod` 10)

main :: IO ()
main = print (digitSum (product [1..100]))

