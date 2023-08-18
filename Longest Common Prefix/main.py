'''
Write a function to find the longest common prefix string amongst an 
array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        min_length = min(len(word) for word in strs)
        for i in range(min_length):
            char = strs[0][i]
            if all(word[i] == char for word in strs):
                common_prefix += char
            else:
                break
        return common_prefix