def solve():
    n = len(s)
    vowels = ["a", "e", "i", "o", "u"]
    for i, l in enumerate(s):
        if l not in vowels and l != "n":

            # if last letter is consonant, there cannot be vowel next to it.
            if i == n-1:
                return "NO"
            
            # if this is not last letter and is a consonant
            # there must a vowel next to it.
            if s[i+1] not in vowels:
                return "NO"

    return "YES"

s = input()

# rules 
# 1. vowel after every consonant, except for n 
# 2. any letter after vowel
# 3. for "n", any letter

print(solve())
