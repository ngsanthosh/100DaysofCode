def transitionPoint(arr, n):
    #Code here
    # Method1
    try:
        return arr.index(1) 
    except:
        return -1
    # Method2
    for i in range(len(arr)):
        if(arr[i]==1):
            return i
    return -1