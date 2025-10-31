class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest=0
        for i in accounts:
            #sum=0
            # for j in i:
            #     sum+=j
            # if sum>richest:
            #     richest=sum
            richest=max(richest,sum(i))
            # if sum>richest:
            #     richest=sum

        return richest
