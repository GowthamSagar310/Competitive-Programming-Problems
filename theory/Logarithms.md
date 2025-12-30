Think of logarithm as 
"to what power should I raise the base to get this number ?"

- log 8 to base 2 = 3
  to what power should I raise the 2 to get this 8 ? = 3
- log 10 to base 10 = 1
  to what power should I raise the 10 to get this 10 ? = 1
- log 1 to base 5 = 0
  to what power should I raise the 5 to get this 1 ? = 0

### Rules
1. Product::  $\log_b(xy) = \log_b x + \log_by$ 
2. Divide::  $\log_b(\frac{x}{y}) = \log_b x - \log_b y$
3. Power::  $\log_b(x^p) = p \log_b x$
4. Change of Base::  $\log_b a = \frac{\log_c a}{\log_c b}$
- $ \log_2(n) = \frac{\log_{10} n}{\log_{10} 2} $
- this mean $ \log_2(n)$ differs from $\log_{10} n$ by a constant. so they can be treated as same in Big O analysis.
- In Big-O notation, we write O(logn) without specifying the base because changing the base only multiplies by a constant

5. Identity::  $\log_b b = 1$
6. Zero Rule::  $\log_b 1 = 0$

