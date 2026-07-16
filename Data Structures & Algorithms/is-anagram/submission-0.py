class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        one, two = Counter(s), Counter(t)

        return one == two
        