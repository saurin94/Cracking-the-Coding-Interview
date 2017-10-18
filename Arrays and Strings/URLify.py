def URLify(s,n):
    s = s.strip()
    s = s.replace(" ", "%20")
    return s

print URLify("Mr John Smith    ", 13)