rows = int(input("rows= "))
cols = int(input("cols= "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input( ))
        row.append(value)
    matrix.append(row)

print("our marrix:")
for row in matrix:
    print(row)


# output:
# rows= 2
# cols= 2
# 1
# 2
# 3
# 4
# our marrix:
# [1, 2]
# [3, 4]
