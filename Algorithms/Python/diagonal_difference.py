def diag_diff(matrix, n):
    xL = 0
    yL = 0

    xR = 0
    yR = n - 1

    left_diagonal = 0
    right_diagonal = 0

    while xL < n:
        left_diagonal += matrix[xL][yL]
        right_diagonal += matrix[xR][yR]

        xL += 1
        yL += 1

        xR += 1
        yR -= 1

    return abs(left_diagonal - right_diagonal)
