x = int(input("Enter number of blocks: "))
y = int(input("Enter number of rows: "))
z = int(input("Enter number of columns: "))

arr = []

for i in range(x):
    block = []
    for j in range(y):
        row = list(map(int, input().split()))
        block.append(row)
    arr.append(block)

print(arr)
