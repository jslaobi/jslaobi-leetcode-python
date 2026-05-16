class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            # count = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
            for char in word:
                count[ord(char) - ord('a')] += 1
            """
            {
            (1, 0, 0, 0, 1, ..., 1, 0, 0, 0, 0, 0, 0): ["eat", "tea"],
            (1, 1, 0, 0, 0, ..., 1, 0, 0, 0, 0, 0, 0): ["bat"]
            }
            """
            anagrams_map[tuple(count)].append(word)
        
        return list(anagrams_map.values())