class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedkey= ''.join(sorted(s))
            res[sortedkey].append(s)
        return list(res.values())