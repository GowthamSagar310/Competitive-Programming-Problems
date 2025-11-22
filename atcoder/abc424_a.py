a, b, c = map(int, input().split())

# two sides equal

if a == b or b == c or c == a:
  print("YES")
else:
  print("NO")