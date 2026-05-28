class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for word in strs:
            encoded_string.append(f"{len(word)}#{word}")
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        j = 0
        
        while i < len(s):
            while i < len(s) and s[i].isdigit():
                i += 1
            digit = int(s[j : i])
            i += 1
            j = i
            j += digit
            res.append(s[i : j])
            i = j
        
        return res
            
