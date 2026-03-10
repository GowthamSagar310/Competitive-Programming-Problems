m = input()
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
k = int(input())

for num, month in enumerate(months, 1):
    if month == m:
        new_index = (num + k) % 12
        if new_index == 0:
            print("December")
        else:
            print(months[new_index-1])
        break