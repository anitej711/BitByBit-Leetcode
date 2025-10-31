#code is not optimized 

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = 0
        for i in range(2, n):
            c = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    c += 1
            if c == 2:
                d += 1

        return d
