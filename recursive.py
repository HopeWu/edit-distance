class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        if not s1 and s2:
            return len(s2)
        if not s2 and s1:
            return len(s1)
        if not s1 and not s2:
            return 0

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
s1 = "workattech"
s2 = "workattech"
print(solution.minOperations(s1, s2))
s1 = "abc"
s2 = "def"
print(solution.minOperations(s1, s2))
s1 = "ab"
s2 = "ba"
print(solution.minOperations(s1, s2))
s1 = "workat"
s2 = "word"
print(solution.minOperations(s1, s2))
