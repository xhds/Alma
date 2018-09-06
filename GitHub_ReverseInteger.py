class Solution:
    def reverse(self, x):
        """
        :type x: int
        :return: int
        """
        result = 0
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = int("-" + str(x)[:0:-1])
        if abs(result) >= 2**31:
            return 0
        else:
            return result
    
if __name__=="__main__":
    s = Solution()
    print(s.reverse(1534236469))
    print(s.reverse(-123))
    print(s.reverse(120))
    print(2**31)