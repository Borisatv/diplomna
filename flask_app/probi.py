list5 = [[1, 'string', 4, None], [1, 2, 3, 4], [None, 2, 23, 7], ['string', 3, 5, 6]]
x = 0
while x < len(list5):
    z = 0
    while z < len(list5[x]):
        if 'None' in str(list5[x][z]):
            list5.remove(list5[x])
        print(list5[x][z])
        z += 1
    x += 1
