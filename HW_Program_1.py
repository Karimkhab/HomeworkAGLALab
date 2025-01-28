class ManySolution(Exception):
    """Exception raised when multiple solutions exist"""
    pass


def gaussian_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[j][i] != 0:
                factor = matrix[j][i] / matrix[i][i]
                for k in range(len(matrix[0])):
                    matrix[j][k] -= factor * matrix[i][k]
    return matrix


def solve_system(matrix):
    matrix = gaussian_elimination(matrix)
    if (matrix[2][3] == 0 and matrix[2][2] == 0):
        z = 0
    else:
        z = matrix[2][3] / matrix[2][2]
    if matrix[1][1] == 0 and matrix[1][2] == 0 and matrix[1][3] == 0:
        raise ManySolution
    elif (matrix[1][1] == 0 and matrix[1][3] / matrix[1][2] == z):
        raise ManySolution
    else:
        y = (matrix[1][3] - z * matrix[1][2]) / matrix[1][1]
    x = (matrix[0][3] - y * matrix[0][2] - z * matrix[0][1]) / matrix[0][0]
    return x, y, z


if __name__ == "__main__":
    mx = [
        [1, 1, 1, 6],
        [1, 2, 2, 11],
        [2, 3, -4, 3]
    ]
    # mx = [
    #     [1, 1, 1, 7],
    #     [1, 2, 2, 10],
    #     [2, 3, -4, 3]
    # ]
    try:
        x, y, z = solve_system(mx)
        print(x,y,z)
    except ZeroDivisionError:
        print("No solution")
    except ManySolution:
        print("Many solution")
