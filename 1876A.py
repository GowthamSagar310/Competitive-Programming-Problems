"""

1. cost = p for each person
2. if ith resident got announcement, he can share to ai residents, with bi per share. 

- more share / less cost is what is want
- share / cost should be more. (shares more, cost less)
"""

for _ in range(int(input())):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    residents = sorted(zip(a, b), key=lambda x: x[1])
    total_cost = p # always first resident needs p 
    remaining = n-1 # first resident is informed

    for a_val, b_val in residents:
        if remaining <= 0: # no more residents to inform (n = 1 case)
            break

        share_cost = b_val
        if share_cost < p:
            informed = min(a_val, remaining)
            total_cost += informed * b_val
            remaining -= informed
        else:
            # because the array is sorted, all the remaining sharing costs are more. 
            # we can use "p" to solve the problem
            break
    
    # loop is broken above, if there are still remaining, that means
    # it is better to use "p"
    total_cost += remaining * p
    print(total_cost)