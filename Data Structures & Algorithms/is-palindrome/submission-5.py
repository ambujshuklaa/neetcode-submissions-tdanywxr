class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=""
        for i in s:
            if i.isalnum():
                l= l + i.lower()
        i = 0
        j = len(l)-1

        while (i<j):
            print(i,j)
            if l[i]==l[j]:
                i = i + 1
                j = j - 1
            else:
                return False
            
        return True

