# Zero Matrix - Make rows and columns to zero if an entry is zero in given matrix

rows = int(input("Enter the number of rows"))
columns = int(input("Enter the number of columns"))
Matrix = []

for i in range(rows):
    row = list(map(int,input(f"Enter row {i} values").split()))
    Matrix.append(row)

indices = []

# Utilize a list to store the indices
# for i in range(rows):
#     for j in range(columns):
#         if Matrix[i][j] == 0:
#             indices.append([i, j])

# for items in indices:
#     for j in range(columns):
#         Matrix[items[0]][j] = 0
    
#     for i in range(rows):
#         Matrix[i][items[1]] = 0


# In place storage of indices by making them -1

for i in range(rows):
    for j in range(columns):
        if Matrix[i][j] == 0:
            Matrix[i][j] = -1

for i in range(rows):
    for j in range(columns):
        if Matrix[i][j] == -1:
            Matrix[i][j] = 0
            for k in range(rows):
                if Matrix[k][j] != -1:
                    Matrix[k][j] = 0
            for k in range(columns):
                if Matrix[i][k] != -1:
                    Matrix[i][k] = 0

print(Matrix)