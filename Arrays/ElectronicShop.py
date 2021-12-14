def getMoneySpent(keyboards, drives, b):
    l = []
    for x in keyboards:
        for y in drives:
            if x+y <= b:
                l.append(x+y)
    if not l:
        return -1
    else:
        return max(l)