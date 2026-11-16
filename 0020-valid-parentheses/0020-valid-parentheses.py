class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapi={'}':'{',']':'[',')':'('}
        for i in s:
            if i in mapi:
                top=st.pop() if st else '#'
                if mapi[i]!=top:
                    return False
            else:
                st.append(i)
        return not st
        