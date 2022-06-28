class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} 
        a_list = list(s)
        a_len = 0
        total = 0
        while not a_len >= len(a_list) - 1:
            if hash_table[a_list[a_len]] >= hash_table[a_list[a_len + 1]]:
                total = total + hash_table[a_list[a_len]] 
                
            else:
                 total = total - hash_table[a_list[a_len]] 
            a_len += 1
        return total + hash_table[s[len(a_list) - 1]]