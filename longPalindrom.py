import math
import chckPalindrom
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        while length > 1:
            i=0
            while i <= (len(s)-length):
                sub=s[i:length+i]
                print('{}   {}      {}'.format(i,length,str(sub)))
                i=i+1
                if chckPalindrom.chckPalindrom(sub):
                    return sub
                del sub 
            length=length-1

s=Solution()

print(s.longestPalindrome('1000001abcdefghihgfedcba0000001'))