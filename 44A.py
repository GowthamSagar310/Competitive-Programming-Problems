n = int(input())
trees = set()
for _ in range(n):
    tree, colour = input().split()
    if (tree + "#" + colour) not in trees:
        trees.add(tree + "#" + colour)
print(len(trees))