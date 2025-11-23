integer, decimal = input().split(".")
if integer[-1] == "9":
    print("GOTO Vasilisa.")
else:
    first_number = int(decimal[0])
    if first_number < 5:
        print(integer)
    else:
        print(int(integer)+1)
