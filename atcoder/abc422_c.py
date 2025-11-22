for _ in range(int(input())):
    a, b, c = map(int, input().split())

    contests = 0 


    # how many "abc" -> min(a, b, c)
    mini = min(a, b, c)
    contests += mini
    a -= mini
    b -= mini
    c -= mini

    # next step: how many "aac" can be made ? 
    # next step: how many "acc" can be made ?
    # why this wont work ?
    # 
    # this is using up one letter fast. 
    # a = 2, b = 0, c = 4
    # making "aac" first will give only one contest
    # but taking "acc" first will give us two contests
    # so the order matters.


    # instead, we need to look for bottle necks
    # every contest needs
    # 1. 1 a, 1 c
    # 2. 3 letters (groups of 3. (a+b)//3)

    contests += min(min(a, c), (a+c) // 3)

    print(contests)