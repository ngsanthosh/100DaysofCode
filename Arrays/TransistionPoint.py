def transitionPoint(arr, n):
    #Code here
    # Method1
    try:
        return arr.index(1) 
    except:
        return -1