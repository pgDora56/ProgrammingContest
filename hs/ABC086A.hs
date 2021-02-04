main :: IO()
main = do 
    [a, b] <- map read . words <$> getLine
    case (mod (a*b) 2) of
        1 -> putStrLn "Odd"
        _ -> putStrLn "Even"
