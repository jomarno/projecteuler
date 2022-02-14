-- PROJECT EULER - PROBLEM 15
-- LATTICE PATHS

-- https://projecteuler.net/problem=15


-- Starting in the top left corner of a 2×2 grid, and only being able to move to 
-- the right and down, there are exactly 6 routes to the bottom right corner.

-- How many such routes are there through a 20×20 grid?


latticePaths :: Int -> Int
latticePaths n = sum [(n `choose` k)^2 | k <- [0..n]]
    where 
        choose n k = product [1..n] `div` (product [1..k] * product [1..(n-k)])

main :: IO ()
main = print (latticePaths 20) 

