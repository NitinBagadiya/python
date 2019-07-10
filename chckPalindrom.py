import os

def chckPalindrom(a):
    for i in range(0,int(len(a)/2)):
        if a[i]!=a[-i-1]:
            return False
    return True

if __name__=="__main__":
    print(chckPalindrom("deeffeed"))
    print(chckPalindrom("Niti"))
    print(chckPalindrom("Naman"))
    print(chckPalindrom("ababbaba"))