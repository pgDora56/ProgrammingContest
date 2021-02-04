main :: IO()
main = do
    n <- readLn
    print $ (n+1)*n `div` 2
