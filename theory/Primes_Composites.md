### Fundamental Theorem of arithmetic 
Every integer greater than 1 is either a prime, or can be expressed as a product of prime numbers. 

In formal terms, every integer n > 1 can be written uniquely as a product of primes:
> n = p1^a1 . p2^a2 . . . . pk^ak

where each Pi is prime and ai >= 1

---
#### Why every Composite number has a prime factor ? 
1. Take any composite number n > 1
    1. By definition, it can be writtern as `n = a*b` where `1 < a < n` and `1 < b < n`
    2. if `a` is not prime, its composite and so it can be further factored.
    3. we repeat this process -> eventually breaking everything into prime factors.
2. Sieve of Eratosthenes works only because of this. We are marking the multiple of the prime numbers as composite, as they are by definition composite (made of prime numbers) and because it has a divisor other 1 and itself.

#### Why atleast one factor of a composite number must be <= sqrt(n) ? 
```math
\text{Let }n=a\cdot b\text{ with }1<a\le b<n.\\
\text{Claim: at least one of }a\text{ or }b\text{ satisfies }a\le\sqrt{n}\text{ (equivalently }b\le\sqrt{n}\text{).}\\[6pt]
\text{Proof (by contradiction):}\\
\quad \text{Assume both }a>\sqrt{n}\text{ and }b>\sqrt{n}.\\
\quad \text{Then }a\cdot b>\sqrt{n}\cdot\sqrt{n}=n,\\
\quad \text{which contradicts }a\cdot b=n.\\
\quad \text{Hence it is impossible that both factors exceed }\sqrt{n}.\\[6pt]
\text{Therefore at least one of }a\text{ or }b\text{ must satisfy } \le\sqrt{n}.\\[6pt]
```
1. So, there must be a divisor, which is <= sqrt(n), if the number is a composite.
2. If it does not exist, then we can conclude that the number is prime.
3. Essentially, if no number <= sqrt(n) divides n, then no number > sqrt(n) can divide it either. 

#### why is it enough to check for primes <= sqrt(n) in sieve of eratosthenes ?
```python
if n <= 2: return 0
is_prime = [True] * (n)
is_prime[0] = is_prime[1] = False 

# why sqrt(n) if enough ?
for i in range(2, isqrt(n)+1):
    if is_prime[i]:
        for j in range(i*i, n, i):
            is_prime[j] = False
return sum(is_prime)
```
1. One way to think about this is, 
    1. we are trying to mark multiple of prime numbers <= n
    2. say there is prime number p > sqrt(n), its mutliples would be 2p, 3p etc.
    3. but 2p is already marked 2, similarily 3p is marked by 3
    4. instead of processing all these, we can directly skip to p * p, because smaller than these are already marked. 
    5. but now, `p * p` would be greater than `n` because `p > sqrt(n)`
    6. because we are not concered about numbers > n, there is no use of processing `p`
    7. so it is enough to choose the primes (just to mark the composites) which are `p <= sqrt(n)`
    8. *this is not to say that there are no primes > sqrt(n), there are !! but we are just not using them to mark composites.*
2. the other way to put this is,
    1. if every `composite number <= n` has some `factor (or divisor) <= sqrt(n)`, all these factor would have marked their multiples till `n` as composite. So the other factors which are `>sqrt(n)` have nothing left to mark and are useless to process.