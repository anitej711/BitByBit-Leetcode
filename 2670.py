class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=len(nums)
        res=[]

        for i in range(x):
            before=nums[:i+1]
            after=nums[i+1:]

            d_before={}
            d_after={}

            for i in before:
                d_before[i]='seen'
            before_count=len(d_before)

            for i in after:
                d_after[i]='seen'
            after_count=len(d_after)
            
            res.append(before_count-after_count)

        return res
            
