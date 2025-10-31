class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        if n==0:
            return False

        k=k%n  #to prevent k being larger than len(list)

        nums.reverse()
        nums[:k]=reversed(nums[:k]) #double reverse the first half 
        nums[k:]=reversed(nums[k:])
