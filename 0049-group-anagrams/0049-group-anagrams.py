class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {}

        for str in strs:
            key = "".join(sorted(str))
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(str)

        return list(hash_map.values()) 

