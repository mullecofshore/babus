i = 1
j = 1

row_count = int(input("Please enter a number for asterikses: "))


while i <= row_count:
    while j <= i:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1
    j = 1 


number_rows = int(input("Please enter a number for number row: "))

a= 1
v = 1

for a in range(1, number_rows + 1):
    for v in range(1,a + 1):
        print(v, end=" ")
    print()