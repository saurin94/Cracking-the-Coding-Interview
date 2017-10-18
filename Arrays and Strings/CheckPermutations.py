def check_permutations(a, b):
    c = {}
    d = {}
    for i in a:
        d[i] = d.get(i,0) + 1
    for i in b:
        c[i] = c.get(i,0) + 1
    return d == c

print check_permutations("abcd", "dcba")
print check_permutations("saurin", "nirsaur")
