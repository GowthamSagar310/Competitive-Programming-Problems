n = int(input())
count=0
first_digit=n
temp = n
while temp:
    first_digit = temp % 10
    count += 1
    temp //= 10
new_num = (first_digit+1) * 10 ** (count-1)
print(new_num-n)