-- PROJECT EULER - PROBLEM 48
-- SELF POWERS

-- https://projecteuler.net/problem=48


-- The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

-- Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


selfPowers :: Integer -> Integer 
selfPowers n = sum [k^k | k <- [1..n]]

main :: IO ()
main = print (selfPowers 1000 `mod` 10^10)

