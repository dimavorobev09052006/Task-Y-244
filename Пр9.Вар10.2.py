def sort_by_line(matrix, k):
    m = [(i, el) for i, el in enumerate(matrix[k].copy())]
    m.sort(key=lambda e: e[1])
    print(m)
    w = len(matrix[0])
    h = len(matrix)
    new_matrix = []
    for i in range(h):
        new_matrix.append([])
        for j in range(w):
            new_matrix[i].append(matrix[i][m[j][0]])
    return new_matrix
 
matrix = [[1, 2, 3, 4], [4, 2, 1, 3], [4, 5, 1, 2]]
print(sort_by_line(matrix,2))