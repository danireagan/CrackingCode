# Given a matrix, rotate by 90 degree, first take transpose, then shift the columns

Matrix = []
Rows = int(input("Enter number of rows"))
Columns = int(input("Enter number of rows"))

for i in range(Rows):
    row = list(map(int,input(f"Enter the row {i} values").split()))
    Matrix.append(row)

for i in range(Rows):
    for j in range(i+1,Columns):
        temp = Matrix[i][j]
        Matrix[i][j] = Matrix[j][i]
        Matrix[j][i] = temp

print("Transpose Matrix")
print(Matrix)

for i in range(Rows):
    k = Columns - 1
    for j in range(Columns//2):
        temp = Matrix[i][j]
        Matrix[i][j] = Matrix[i][k]
        Matrix[i][k] = temp
        k -= 1

print("Rotated Matrix")
print(Matrix)



