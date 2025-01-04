class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Time Complexity and Space Complexity are both O(N)
        """
        complements_positions_map = {}

        for current_pos in range(len(nums)):
            current_num = nums[current_pos]
            ### Checks if the current number IS a complement
            ### If so, retrievs its position and return indices
            if current_num in complements_positions_map.keys():
                complement_pos = complements_positions_map[current_num]
                return [complement_pos, current_pos]
            else:
                ## Determines complement amd
                ## Stores current position and its number's complement 
                complement = target - current_num
                complements_positions_map[complement] = current_pos