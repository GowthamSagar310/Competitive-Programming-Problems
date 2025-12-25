for _ in range(int(input())):
    n = int(input())

    # n = 1 -> impossible
    # n = 2 -> 66 -> 66 * 1
    # n = 3 -> no combination of 3, 6 will form a valid number 
    # n = 4 -> 3366 -> 66 * 51
    # n = 5 -> 36366 -> 66 * 551
    # n = 6 -> "33 3366" -> 66 * 5051 
    # n = 7 -> "33 36366" -> 66 * 50551

    # this is more like an observation
    # if the end 3366 is divisible by 66
    # add more "33" to the start wont effect this, because 33 * 10^p
    # is divisible by 66
    # and is also lexicographically smaller.
    # this wont work for odd length because
    # (333 3366) is not divisible by 66 as 333 * 10^p % 6 != 0

    # but odd lengthed numbers >= 5
    # we need to use 36366

    if n == 1 or n == 3:
        print(-1)
    elif n % 2 == 0:
        print("3" * (n-2) + "66")
    else:
        print("3" * (n-5) + "36366")
