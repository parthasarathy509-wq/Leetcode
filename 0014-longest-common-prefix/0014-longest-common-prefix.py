class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Take the first word as our reference base
        base = strs[0]
        
        # Loop through each character index of the base word
        for i in range(len(base)):
            char = base[i]
            
            # Check this same index 'i' in all other words
            for other_word in strs[1:]:
                # Check if we ran out of letters in the other word,
                # or if the characters don't match
                if i == len(other_word) or other_word[i] != char:
                    # Return everything up to this index
                    return base[:i]
                    
        return base
