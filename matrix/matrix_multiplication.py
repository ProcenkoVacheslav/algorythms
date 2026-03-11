from decorators import time_decorator


@time_decorator('matrix', 'matrix_multiplication')
def matrix_multiplication(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    matrix_c = []

    for i in range(len(matrix_a)):
        matrix_c.append([])
        for j in range(len(matrix_b[0])):
            matrix_c[-1].append(0)
            for k in range(len(matrix_b)):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return matrix_c


if __name__ == "__main__":
    matrx_a = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    matrx_b = [
        [7, 8],
        [9, 1],
        [2, 3],
    ]

    print(*matrix_multiplication(matrx_a, matrx_b), sep='\n')
