a, b = map(int, input().split())
hours = 0
candles = a
melted = 0
while candles > 0:
    # use all the candles
    hours += candles

    # convert all the candles = melted
    melted += candles

    # how many melted candles can be converted to candles ? 
    candles = melted // b

    # but not all of them will be perfectly converted into candles
    # so leftover melted candles 
    melted = melted % b

print(hours)