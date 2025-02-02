import numpy as np


def GaussJordanMethod(mx):
    n, m = mx.shape

    for i in range(n):
        pivot = mx[i][i]
        if pivot == 0:
            for j in range(i + 1, n):
                if mx[j][i] != 0:
                    mx[[i, j]] = mx[[j, i]]
                    pivot = mx[i][i]
                    break
        for k in range(m):
            mx[i][k] /= pivot

        for j in range(n):
            if j != i:
                fact = mx[j][i]
                for k in range(m):
                    mx[j][k] -= fact * mx[i][k]

    return mx



if __name__ == "__main__":
    # matrix = np.array([[1, 0, 0, 1,0,0],
    #                   [1, 1, 1, 0,1,0],
    #                   [0, 0, 1, 0,0,1]],dtype=float)

    matrix = np.array([[2, -1, 0, 1, 0, 0],
                            [-1, 2, -1, 0, 1, 0],
                       [0, -1, 2, 0, 0, 1]],dtype=float)
    # matrix = np.array([[0, 0, 1, 1, 0, 0],
    #                    [0, 1, 1, 0, 1, 0],
    #                    [1, 1, 1, 0, 0, 1]],dtype=float)
    print(matrix)
    print("")
    print(GaussJordanMethod(matrix))
