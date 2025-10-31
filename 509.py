class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1

        a,b=0,1
        for i in range(2,n+1):
            cur=a+b
            a=b
            b=cur

        return cur
