
def print_menu():
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")


def add_matrices():
    rows1, cols1 = [int(i) for i in input("Enter size of first matrix: > ").split()]
    print("Enter first matrix:")
    matrix_1 = [[int(j) if j.isdigit() else float(j) for j in input("> ").split()] for i in range(rows1)]

    rows2, cols2 = [int(i) for i in input("Enter size of second matrix: > ").split()]
    print("Enter second matrix:")
    matrix_2 = [[int(j) if j.isdigit() else float(j) for j in input("> ").split()] for i in range(rows2)]

    if (rows1, cols1) != (rows2, cols2):
        print('The operation cannot be performed.')
    else:
        print("The result is:")
        for i in range(rows1):
            for j in range(cols1):
                print(matrix_1[i][j] + matrix_2[i][j], end=' ')
            print()

# add_matrices()


def multiply_matrix_by_constant():
    rows, cols = map(int, input("Enter size of first matrix: > ").split())
    print("Enter matrix:")
    matrix = [[int(j) if j.isdigit() else float(j) for j in input("> ").split()] for i in range(rows)]

    constant = input("Enter constant: > ")
    print("The result is:")

    for i in range(rows):
        for j in range(cols):
            if type(constant) == int:
                print(matrix[i][j] * constant, end=' ')
            else:
                print(matrix[i][j] * float(constant), end=' ')
        print()


def multiply_matrices():
    rows1, cols1 = [int(i) for i in input("Enter size of first matrix: > ").split()]
    print("Enter first matrix:")
    matrix_1 = [[int(j) if j.isdigit() else float(j) for j in input("> ").split()] for i in range(rows1)]

    rows2, cols2 = [int(i) for i in input("Enter size of second matrix: > ").split()]
    print("Enter second matrix:")
    matrix_2 = [[int(j) if j.isdigit() else float(j) for j in input("> ").split()] for i in range(rows2)]

    if len(matrix_1[0]) != len(matrix_2):
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        result_matrix = [[0 for j in range(len(matrix_2[0]))] for i in range(len(matrix_1))]
        # print(result_matrix)
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for l in range(len(matrix_2)):
                result_matrix[i][j] += matrix_1[i][l] * matrix_2[l][j]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            print(result_matrix[i][j], end=' ')
        print()


def transpose_matrices():
    print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
    user_choice = input("Your choice: > ")

    rows, cols = [int(i) for i in input("Enter matrix size: > ").split()]
    print("Enter matrix:")
    matrix = [[int(j) if j.isdigit() else float(j) for j in input("> ").split()] for i in range(rows)]
    print("The result is:")

    if user_choice == '1':
        main_diagonal(matrix, rows, cols)
    elif user_choice == '2':
        side_diagonal(matrix, rows, cols)
    elif user_choice == '3':
        vertical_line(matrix, rows, cols)
    elif user_choice == '4':
        horizontal_line(matrix, rows, cols)
    else:
        print('Invalid input!\n')


def main_diagonal(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[j][i], end=' ')
        print()


def side_diagonal(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[cols - 1 - j][rows - 1 - i], end=' ')
        print()


def vertical_line(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][rows - 1 - j], end=' ')
        print()


def horizontal_line(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[rows - 1 - i][j], end=' ')
        print()


def determinant(m):
    m_size = len(m)
    if m_size == 1:
        return m[0][0]
    if m_size == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    det = 0
    for j in range(m_size):
        minor = [[m[i][k] for k in range(m_size) if k != j] for i in range(1, m_size)]
        det += m[0][j] * ((-1) ** j * determinant(minor))
    return det


def inverse_matrix():
    rows, cols = [int(i) for i in input("Enter matrix size: > ").split()]
    print("Enter matrix:")
    matrix_1 = [[int(j) if j.isdigit() else float(j) for j in input("> ").split()] for i in range(rows)]
    print("The result is: ")
    det = determinant(matrix_1)
    m_size = len(matrix_1)
    if det == 0:
        print("This matrix doesn't have an inverse.")
    elif len(matrix_1) == 2:
        inversed_matrix = [[matrix_1[1][1] / det, -1 * matrix_1[0][1] / det],
                           [-1 * matrix_1[1][0] / det, matrix_1[0][0] / det]]
        for i in inversed_matrix:
            print(*i)
    else:
        cofactors = []
        for r in range(len(matrix_1)):
            cofactor_row = []
            for c in range(len(matrix_1)):
                minor = [row[:c] + row[c + 1:] for row in (matrix_1[:r] + matrix_1[r + 1:])]
                cofactor_row.append(((-1) ** (r + c)) * determinant(minor))
            cofactors.append(cofactor_row)
        cofactors = [[cofactors[j][i] for j in range(cols)] for i in range(rows)]
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / det
        for i in range(rows):
            for j in range(cols):
                print(round(cofactors[i][j], 3), end=' ')
            print()


while True:
    print_menu()
    user_choice = input("Your choice: > ")
    if user_choice == '1':
        add_matrices()
    elif user_choice == '2':
        multiply_matrix_by_constant()
    elif user_choice == '3':
        multiply_matrices()
    elif user_choice == '4':
        print()
        transpose_matrices()
    elif user_choice == '5':
        rows, cols = [int(i) for i in input("Enter matrix size: > ").split()]
        print("Enter matrix:")
        matrix_1 = [[int(j) if j.isdigit() else float(j) for j in input("> ").split()] for i in range(rows)]
        print("The result is: ")
        print(determinant(matrix_1))
    elif user_choice == '6':
        inverse_matrix()
    elif user_choice == '0':
        break
    print()