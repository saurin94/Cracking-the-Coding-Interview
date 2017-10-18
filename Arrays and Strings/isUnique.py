def with_data_structure(s1):
    d = {}
    for i in s1:
        d[i] = d.get(i, 0) + 1
        if d[i] > 1:
            return False
    return True


def without_data_structure(s1):
    s1 = sorted(s1)
    for i in range(len(s1)-1):
        if s1[i] == s1[i+1]:
            return False
    return True

s = "aaaaaaaa"
a = "abcdfghijklmno"
b = "abcdagh"
print s, " -> ", with_data_structure(s)
print s, " -> ", without_data_structure(s)
print a, " -> ", with_data_structure(a)
print a, " -> ", without_data_structure(a)
print b, " -> ", with_data_structure(b)
print b, " -> ", without_data_structure(b)