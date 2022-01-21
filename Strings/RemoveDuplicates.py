

class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        count, used = 26 * [0], 26 * [0]
        for c in s:
            count[ord(c) - ord('a')] += 1
        stack = []
        for c in s:
            count[ord(c) - ord('a')] -= 1
            if used[ord(c) - ord('a')] == 0:
                while stack and c < stack[-1] and count[ord(stack[-1]) - ord('a')]:
                    used[ord(stack[-1]) - ord('a')] = 0
                    stack.pop()
                stack.append(c)
                used[ord(c) - ord('a')] = 1
        return ''.join(stack)