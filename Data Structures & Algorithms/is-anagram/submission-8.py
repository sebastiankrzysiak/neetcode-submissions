class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def create_list(word):
            arr = [0] * 26

            for letter in word:
                arr[ord(letter) - ord("a")] += 1
            
            return arr
        
        return create_list(s) == create_list(t)