# two 5 digit numbers, say abcde and fghij
# both numbers combined should have all 0-9 (10 numbers, 10 slots. so no repeatition)
# (abcde / fghij = N)
# 2 <= N <= 79
# abcde > fghij

# given the constraints
# 1. what is minimum 5 digit number possible ? 01234
# 2. what is maximum 5 digit number possible ? 98765
# 3. if the numerator is known, denominator is just (numerator / N) but this leads to division problems
#    so we fix the denominator, which gives the numerator by (denominator * N)
# 4. if iterate denominator from 01234 to 98765, we can find numerators and see if all digits are present.
# 5. is there a better optimization ? 
#    say numerator = 56780 and N = 10, what is the maximum possible denominator ? 56780 / 10 = 5678
#    any number which is greater than this (5678) is going to produce value less 10. 56780 / 5679 is < 10
#    so maximum possible value for denominator is abcde / N
# 
# 6. how to check if all the numbers from 0-9 are present ? 
#    from 01234 to 09999 -> that is < 10000 -> all numbers have a leading 0
#    think of 10 slots for numbers 0-9. each position is set when we encounter that number
#    if at the end, all 10 slots are set, then all digits are present. 
#    which in binary looks like 11111111 = (2 ^ 10) - 1 = (1 << 10)-1


# time complexity ? for N = 2, fghij can be from 01234 to (98765 / 2) which is ~50K numbers
# for each number there are two inner loops (10 operations), in total, per test case = 50K * 10 = 500K operations = 5 * 10^5 < 1sec

first = True
while True:
    N = int(input())
    if N == 0:
        break
    else:
        if not first:
            print()
        first = False
        found = False
        for fghij in range(1234, (98765 // N)+1):
            abcde = fghij * N
            value = fghij < 10000 # sets last bit as 1 if "f" is 0
            temp = abcde
            while temp: value |= (1 << (temp%10)); temp //= 10
            temp = fghij
            while temp: value |= (1 << (temp%10)); temp //= 10
            if value == (2**10)-1:
                found = True
                print("{:05d} / {:05d} = {}".format(abcde, fghij, N))
        if not found:
            print("There are no solutions for {}.".format(N))

# how to generate 10 digit numbers using recursion ? 
# what is the time complexity of this method ? 
# for first slot there are 10 options (0-9)
# for second slot there are only 9 options (0-9 except for what is choosen for first slot)
# ....
# 10 * 9 * 8 ... = 10! choices = 3628800 = 3 * 10^6 (slightly slower than above solution)
def recur(index, number_mask, numbers):
    if index == 10:
        abcde = int("".join(numbers[:5]))
        fghij = int("".join(numbers[5:]))
        if abcde / fghij == N:
            print("{:05d} / {:05d} = {}".format(abcde, fghij, N))
        return

    for digit in range(10):
        if not (number_mask & (1 << digit)):
            numbers.add(digit)
            recur(index+1, number_mask | (1 << digit), numbers)
            numbers.pop()

# Slightly better
# Generate only first 5 digits, and by relation find the numerator
# this reduces the number of permuations to 10 * 9 * 8 * 7 * 6
# but for each of this, it takes extra 10 ops to check if it is valid
def is_valid_combination(abcde, fghij):
        value = fghij < 10000 # sets last bit as 1 if "f" is 0
        temp = abcde
        while temp: value |= (1 << (temp%10)); temp //= 10
        temp = fghij
        while temp: value |= (1 << (temp%10)); temp //= 10
        return value == (2**10)-1

def recur(index, number_mask, number):
    if index == 5:
        fghij = number
        abcde = fghij * N
        if is_valid_combination(abcde, fghij):
            print("{:05d} / {:05d} = {}".format(abcde, fghij, N))
        return
    for digit in range(10):
        if not (number_mask & (1 << digit)):
            recur(index+1, number_mask | (1 << digit), number * 10 + digit)
