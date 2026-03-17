start, end = input().split()
n = int(input())
n = n % 4

m = {
    "^": 0,
    ">": 1,
    "v": 2,
    "<": 3
}

if n == 0 or n == 2:
    print("undefined")
else:
    start_i, end_i = m[start], m[end]
    code = str(start_i) + str(end_i)
    if code in ["01", "12", "23", "30"]:
        print("cw" if n == 1 else "ccw")
    if code in ["03", "32", "21", "10"]: 
        print("ccw" if n == 1 else "cw")
