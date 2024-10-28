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
