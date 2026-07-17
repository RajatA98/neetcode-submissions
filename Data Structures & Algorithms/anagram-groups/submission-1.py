from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #store each list in hashmap
        groups = defaultdict(list)
        #key will be character counts 
        for s in strs:
            char_cnt = [0] * 26

            for c in s:
                char_cnt[ord(c) - ord('a')] += 1
            groups[tuple(char_cnt)].append(s)
        return list(groups.values())
        