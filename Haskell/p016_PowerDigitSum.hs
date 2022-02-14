-- PROJECT EULER - PROBLEM 16
-- POWER DIGIT SUMS

-- https://projecteuler.net/problem=16


-- 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

-- What is the sum of the digits of the number 2^1000?


digitSum :: Integer -> Integer
digitSum 0 = 0
digitSum x = digitSum (x `div` 10) + (x `mod` 10)

main :: IO ()
main = print (digitSum (2^1000))

