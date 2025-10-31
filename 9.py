class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        else:
            palindrome=str(x)
            reversedx=palindrome[::-1]

            if reversedx==palindrome:
                return True
            else:
                return False
            
