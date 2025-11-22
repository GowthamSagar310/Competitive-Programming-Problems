a, b, c = map(int, input().split())
print(max(a, b, c)-min(a, b, c))


# D(p)=∣x1​−p∣+∣x2​−p∣+∣x3​−p∣
# we need to minimize this. 

# If you stand left of the median, more people are to your right than to your left. So moving right decreases total distance (since you’re moving closer to more people).
# If you stand right of the median, more people are to your left than to your right. So moving left decreases total distance.
# At the median, the number of people on the left and right are balanced, so moving in either direction increases distance.
