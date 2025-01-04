class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time Complexity is O(N)
        Space Complexity in O(1)
        """

        """
        Properties of XOR operation:
        XOR(k ,0) = k
        XOR(k, k) = 0
        """

        ## Sets efault value for XOR operation
        result = 0
        for num in nums:
            result ^= num
        return result
        