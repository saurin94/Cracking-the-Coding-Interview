def helper(a, n, b, m):
    edits = 0
    large = 0
    small = 0
    while large < n and small < m:
        if a[large] != b[small]:
            if a[large + 1] != b[small]:
                edits += 1
        large += 1
        small += 1
    while small < n:
        if a[small]:
            edits += 1
        small += 1
    if edits <= 1:
        return True
    else:
        return False


def same_length(a, b, n):
    edits = 0
    while n >= 0:
        if a[n] != b[n]:
            edits += 1
        n -= 1
    if edits <= 1:
        return True
    else:
        return False


def one_away(a, b):
    n = len(a)
    m = len(b)
    if n - m > 1:
        return False
    if n > m:
        t = helper(a, n, b, m)
    elif m > n:
        t = helper(b, m, a, n)
    else:
        t = same_length(a, b, n - 1)

    return t


print "pale paler : ", one_away("pale", "paler")
print "pale bale :", one_away("pale", "bale")
print "pale pales :", one_away("pale", "pales")
print "pale bake :", one_away("pale", "bake")
print "pale lape :", one_away("pale", "lape")
print one_away("pa", "paaaaale")

