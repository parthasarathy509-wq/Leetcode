class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return " "
        base=strs[0]
        for i in range(len(base)):
            char=base[i]
            for j in strs[1:]:
                if i==len(j) or j[i]!=char:
                    return base[:i]
        return base
        