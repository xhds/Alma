class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        """ solution 1
        while k>0 :
            nums.insert(0, nums.pop(-1))
            k -= 1
        """

        """ 反转再反转 """
        k = k%len(nums)
        nums[:-k] = nums[:-k][::-1]
        nums[-k:] = nums[-k:][::-1]
        nums[:] = nums[::-1]


if __name__ == "__main__":
    s = Solution()
    x = [-1,-100,3,99]
    #s.rotate(x, 2)
    print(x[:-2])