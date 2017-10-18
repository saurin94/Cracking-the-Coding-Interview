def palindrome_check(s):
    d = {}
    s = s.lower().replace(" ","")
    for i in s:
        d[i] = d.get(i, 0) + 1

    counter = 0
    for ch, count in d.iteritems():
        if count % 2 != 0:
            counter += 1

    if counter <= 1:
        return True
    else:
        return False

print palindrome_check("sas sas")
print palindrome_check("Tact coa")
print palindrome_check("tac cat")
print palindrome_check("rin sau")
