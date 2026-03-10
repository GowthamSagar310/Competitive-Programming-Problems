import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    """
    median_index = i
    first_ele_index = j
    """

    def solve(arr, n):
        first_element = arr[0]
        median_index = (n // 2) if n & 1 else (n // 2)-1

        arr.sort()
        first_element_index = arr.index(first_element)

        
    print("YES" if solve(arr, n) else "NO")
                
