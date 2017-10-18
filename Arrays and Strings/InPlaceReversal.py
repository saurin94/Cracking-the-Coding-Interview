def in_place_reversal(s):
    end = len(s)-1
    start = 0
    s = list(s)
    while start <= end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    print "".join(s)

s = "saurins"
in_place_reversal(s)
