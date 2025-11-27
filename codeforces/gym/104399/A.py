a, b, c, x, y, z = map(int, input().split())
barley = a * x
hops = b * y
malt = c * z
 
maxi = max(barley, hops, malt)
if maxi == barley: print("Barley", end = " ")
if maxi == hops: print("Hops", end = " ")
if maxi == malt: print("Malt", end = " ")