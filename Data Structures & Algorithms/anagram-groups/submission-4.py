class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def create_key(word):
            arr = [0] * 26

            for letter in word:
                arr[ord(letter) - ord("a")] += 1
            
            return tuple(arr)
        

        hashMap = defaultdict(list)

        for word in strs:
            key = create_key(word)
            hashMap[key].append(word)
        
        return list(hashMap.values())