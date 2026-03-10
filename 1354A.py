from math import ceil
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    # if d >= c:
    #     # if not already found. 
    #     # never going to find. 

    #     if a <= b:
    #         print(b)
    #     else:
    #         print(-1)

    # else:
    #     # should be possible
        
    #     # within the first alarm
    #     if a <= b:
    #         print(b)
    #     else:
    #         # total sleep required = a
    #         # first alarm is already over. 
    #         # total needed = a-b

    #         # it takes d minutes to go to sleep
    #         # next alarm as c minutes away
    #         # minutes that he will sleep = d-c

    #         print(b + c * ceil((a-b)/(c-d)))


    # simpler solution
    if a <= b:
        print(b)
    else:
        if d >= c:
            print(-1)
        else:
            print(b + c * ceil((a-b)/(c-d)))