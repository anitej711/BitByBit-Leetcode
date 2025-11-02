class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # out=[]
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i!=j and nums[i]+nums[j]==target:
        #             return[i,j]
                
        dict1={}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in dict1:
                return [dict1[key], i]
            dict1[nums[i]] = i
