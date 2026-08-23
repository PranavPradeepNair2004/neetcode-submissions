from collections import Counter, defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for word in strs:
            # 1. Use Counter to get the exact occurrences of letters
            word_count = Counter(word)
            
            # 2. Convert to a frozenset of (letter, count) tuples so it can be a key
            key = frozenset(word_count.items())
            
            # 3. Group the original word under this unique key
            ans[key].append(word)
            
        return list(ans.values())