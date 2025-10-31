class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        greater=0
        smaller=0
        if a>b:
            greater=a
            smaller=b
        else:
            greater=b
            smaller=a

        c=0
        for i in range(1,greater+1):
            if greater%i==0 and smaller%i==0:
                c+=1
        return c
