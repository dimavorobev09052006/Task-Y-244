matr = [[1, 2, 4, 7],
        [7, 3, 1, 9],
        [8, 7, 6, 1],
        [1, 3, 9, 2]]
print(max([max(row) for row in matr if row == sorted(row) or row[::-1] == sorted(row)]))
