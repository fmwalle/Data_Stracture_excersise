def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        num=x/2
        res=0
        i=1
        if x==1:
            return 1
        while i<=num:
            
            if i*i==x:
                res=i
                return res
            elif i*i <x:
                res=i
                i=i+1
                continue
            elif i*i>x:
                return res
        return res     

print(mySqrt(2))  

def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        result=[]

        for i in range(2**n):
            result.append(i^(i>>1))  
        return result  

def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        result=[]
        for i in range(2**n):
            result.append(i^(i>>1))

        start_index=result.index(start)    

        return result[start_index:] + result[:start_index]          
