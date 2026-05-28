class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        required_matches = len(freq)

        l = 0
        r = 0

        while r < len(s2):
            can_grow = s2[r] in freq and freq[s2[r]] > 0
            if can_grow:
                freq[s2[r]] -= 1
                if freq[s2[r]] == 0:
                    required_matches -= 1
                    if required_matches == 0:
                        return True
                r += 1
            elif l < r:
                if s2[l] in freq:
                    if freq[s2[l]] == 0:
                        required_matches += 1
                    freq[s2[l]] += 1
                l += 1
            else:
                l += 1
                r += 1
        
        return False
