import random

# פונקציה ליצירת מטריצה ריבועית בגודל n x n עם ערכים רנדומליים
def create_matrix(n):
    matrix = []
    for _ in range(n):
        row = [random.randint(1, 10) for _ in range(n)]  # ערכים רנדומליים בין 1 ל-10
        matrix.append(row)
    return matrix

# פונקציה להדפסת מטריצה
def print_matrix(matrix):
    for row in matrix:
        print(row)

# פונקציה לחיבור של 2 מטריצות
def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# פונקציה לכפל של 2 מטריצות
def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            total = 0
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)
    return result

# יצירת 2 מטריצות בגודל ריבועי 3x3
matrix1 = create_matrix(3)
matrix2 = create_matrix(3)

# הדפסת המטריצות
print("מטריצה ראשונה:")
print_matrix(matrix1)
print("\nמטריצה שנייה:")
print_matrix(matrix2)

# הדפסת סכום המטריצות
print("\nסכום המטריצות:")
print_matrix(add_matrices(matrix1, matrix2))

# הדפסת הכפל של המטריצות
print("\nמכפלת המטריצות:")
print_matrix(multiply_matrices(matrix1, matrix2))
