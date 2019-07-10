price = [0,2,5,8,14,1]
#,7,2,9,8,3,5]

def rodcut(rod):

    if rod < 0:
        return

    rev=0
    for i in range(1,rod+1):
        rev = max(rev, price[i] + rodcut(rod-i))
    return rev

print(rodcut(5))


