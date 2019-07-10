class iterDemo:
    def __init__(self):
        pass 

    def __iter__(self):
        pass
    
    def next(self):
        pass
    
ob=iterDemo()

for i in ob:
    print(i)

with fopen