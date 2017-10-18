def rotate_matrix(a):
    n = len(a[0])
    m = len(a)
    # Transpose
    for i in range(n):
        for j in range(m):
            if j >= i:
                temp = a[i][j]
                a[i][j] = a[j][i]
                a[j][i] = temp
    # Reverse
    for i in range(n):
        t = a[i][::-1]
        a[i] = t
    # Rotated Array
    return a


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
a = rotate_matrix(a)
for i in a:
    print i
print "\n___\n"
mat = rotate_matrix(mat2)
for i in mat:
    print i
