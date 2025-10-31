class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string=''
        for i in digits:
            x=str(i)
            string+=x
        y=int(string)+1
        string=str(y)
        lst=[]
        for i in string:
            lst.append(int(i))
        return lst
