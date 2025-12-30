sum of all digits of a number till it reaches a single digit == digit root == number % 9

- num = d1 * (10^n1) + d2 * (10^(n1-1)) + ... dn
- num % 9 = (d1 * (10^n1) + d2 * (10^(n1-1)) + ... dn) % 9
- num % 9 = (d1 * 1 + d2 * 1 + d3 * 1 + ..) % 9
- num % 9 = (sum of digits) % 9
- if (sum of digits) > 9: again it can be converted to d1 * (10^n1) + ... 
- if (sum of digits) <= 9: (sum of digits) % 9 = [0, 8]

case1: num % 9 == 0
- in that case, num % 9 != (sum of digits) % 9 -> except for 0
- to make it work, the clever trick used here is
- (sum of digits) % 9 = 1 + (n-1) % 9
- this does not work for 0, so an extra condition is required

```python
# O(1) solution
def sum_of_digits_of_a_number(n):
    if n == 0: return 0
    return 1 + (n-1) % 9
```

Casting out 9s trick
1. If the task is find the sum of digits recursively till a single digit
    1. we can use digit root = 1 + (n-1) % 9
    or 
    2. we can ignore 9s or combinations of 9s from the sum, meaning
       - number = 549821 = 5+4+9+8+2+1 = 29 = 11 = 2
       - num = d1 * (10^n1) + d2 * (10^(n1-1)) + ... dn
       - num = d1 * (99... + 1) + d2 * (9... + 1) + ...
       - num = d1 * (99...) + d2 * (9...) + ... + (d1 + d2 + d3 + .. dn)
       - num = [numbers divisible by 9] + (sum of digits of num)
       - to get only the sum of digits = we can just MOD 9
       - num % 9 = 0 + 0 + 0 + .. (sum of digits) % 9
       - inside (sum of digits), if there a 9 or combination of 9, its MOD 9 = 0 -> sum wont change
       - (a + b) % m = (a%m + b%m)%m
       - so we can simply ignore values of 9 or combinations of 9
       - number = 549821 = 5+4 +9 +8+1 +2 = 2
       - this is a mental trick to calculate. code equivalent is still 1 + (n-1) % 9

Casting out 11s
Two numbers a and b are congruent modulo n if their difference is a multiple of n.
- if a % n == b % n, (a-b) % n == 0
- 10 ≡ -1 % 11, because (10-(-1)) % 11 == 0
- how is this helpful ? The powers of 10 oscillate with % 11
- 10^0 = 1 -> 1 % 11 = 1
- 10^1 = 10 -> 10 % 11 = -1 (write 10 as 11-1)
- 10^2 = 100 -> 100 % 11 = 1 (write 100 as 99+1)
- 10^3 = 1000 -> 1000 % 11 = -1 (write 1000 as 100 * 10 -> (100 * 10) % 11 = (1 * -1))
- so to find number % 11, we take alternating sums of digits
- num = d1 * (10^n1) + d2 * (10^(n1-1)) + ... dn
- num % 11 = (dn - dn-1 + dn-2 + ...) % 11

Problems
1. https://leetcode.com/problems/add-digits/description/