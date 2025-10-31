class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # x=''
        # for i in s:
        #     if i.isalnum()==True:
        #         x+=i.lower()

        # front=0
        # rear=-1
        # c=0
        # for i in range(len(s)//2):
        #     if x[front]!=x[rear]:
        #         return False
        #     front+=1
        #     rear-=1

        # return True
        y=''
        for i in s:
            if i.isalnum():  
                y+=i.lower()
        
        x=''
        for i in s:
            if i.isalnum():
                x+=i.lower()
        x=x[::-1]
        
        if x==y:
            return True
        else:
            return False
