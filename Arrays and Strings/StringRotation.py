class Solution:
    def __init__(self):
        string1 = "waterbottle"
        string2 = "bottlewater"
        newstring = string1 + string1
        ans = self.is_sub_string(newstring, string2)
        print ans

    @staticmethod
    def is_sub_string(s1, s2):
        if s2 in s1:
            return True
        else:
            return False

Solution()