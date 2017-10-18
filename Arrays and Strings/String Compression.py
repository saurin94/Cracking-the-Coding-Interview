def compress_string(s):
    result = ""
    count = 0
    for i in range(len(s)):
        count += 1
        if i+1 >= len(s) or s[i] != s[i+1]:
            result += s[i]
            result += str(count)
            count = 0
    if len(result) >= len(s):
        return s
    else:
        return result
print compress_string("aa")
print compress_string("a")
print compress_string("aabbccddd")
print compress_string("aaaabbbbccc")
