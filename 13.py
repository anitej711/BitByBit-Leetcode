class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        num = 0
        for i in s:
            if i=='M':
                num+=1000
            elif i=='D':
                num+=500
            elif i=='C':
                num+=100
            elif i=='L':
                num+=50
            elif i=='X':
                i+=10
            elif i=='V':
                num+=5
            elif i=='I':
                num+=1

        return num
