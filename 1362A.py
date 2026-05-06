# all the operations are just x2, x4, x8
# it all revolves around this. 

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    if b % a != 0:
        print(-1)
        continue
    
    d = b // a
    
    # if not power of 2, not going to work.
    if d & (d-1) != 0:
        print(-1)
        continue

    # number of times divisible only 2
    # sufficient bit length - 1
    # 16 can be represented in 5 bits 
    # 2^4 -> 4 times divisible by 2
    k = d.bit_length() - 1

    eights = k // 3 # use 3 2s to form one eight to minimize ops
    fours = (k % 3) // 2 # one groups of 3 are used, if 2s are present, use groups of 2 2s, to make 4s [0, 1, 2]
    twos = (k % 3) % 2 # if all of them are used [0, 1]
    print(eights + fours + twos)