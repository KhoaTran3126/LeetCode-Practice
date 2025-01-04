class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Time Complexity is O(N + M)
        Space Complexity is O(1)
        """
        if len(s) != len(t): return False

        s_dict = {}
        t_dict = {}

        # O(n)
        ## Stores each letter in string s and their count in dict
        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 1
            else: s_dict[letter] += 1

        # O(m)
        ## Stores each letter in string t and their count in dict
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] = 1
            else: t_dict[letter] += 1

        # O(n+m)
        ## Compares if the dictionaries are similar; if not, return False
        for letter in s_dict.keys():
            if letter not in t_dict:
                return False
            elif s_dict[letter] != t_dict[letter]:
                return False
        return True
        