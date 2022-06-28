class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        if s1[0] == s2[0]:
            return self.minOperations(s1[1:], s2[1:])
        else:
            return min(1 + self.minOperations(s1[1:], s2[:]), 
                       1 + self.minOperations(s1[1:], s2[1:]), 
                       1 + self.minOperations(s1[:], s2[1:]))


solution = Solution()


s1 = "hello"
s2 = "seldom"
print(solution.minOperations(s1, s2))
