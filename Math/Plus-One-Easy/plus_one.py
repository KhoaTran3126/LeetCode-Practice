class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        Time and Space Complexties are O(N).
        """
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        ## If the last digit is 9, sets it to 0
        digits[-1] = 0
        ## Iterates the list backward
        for i in range(len(digits)-2, -1, -1):
            ## If the digit behind is 0, increase the current digit according
            if digits[i+1]==0:
                if digits[i]<9:
                    digits[i] += 1
                    return digits
                digits[i] = 0

        ## If the first digit is nonzero, returns the list
        ## Else, adds a 1 to the front of the list
        if digits[0]!=0: return digits
        digits.insert(0, 1)
        return digits
        