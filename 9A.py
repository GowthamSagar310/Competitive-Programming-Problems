y, w = map(int, input().split())
numerator = 6-max(y, w)+1
denominator = 6

if numerator == 1: print("1/6")
if numerator == 2: print("1/3")
if numerator == 3: print("1/2")
if numerator == 4: print("2/3")
if numerator == 5: print("5/6")
if numerator == 6: print("1/1")