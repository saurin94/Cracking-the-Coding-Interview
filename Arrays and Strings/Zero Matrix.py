def get_zero_positions(a):
    n = len(a)
    m = len(a[0])
    rows = []
    cols = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                rows.append(i)
                cols.append(j)

    print cols
    for i in range(n):
        if i in rows:
            a[i] = [0]*n
            for j in range(m):
                if j in cols:
                    print i, j, a[i][j]
                    a[i][j] = 0

    print a

mat2 = [[1, 2, 3, 4], [5, 0, 7, 8], [9, 10, 0, 12], [13, 14, 15, 16]]
get_zero_positions(mat2)