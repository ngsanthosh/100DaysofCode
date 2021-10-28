def CountLeafNodesIter(root) :
	if root is None :
		return 0
	stack = []
	cnt = 0
	stack.append(root)
	while stack :
		top = stack.pop()
		if top.left is None and top.right is None :
			cnt+=1
		else :
			if top.left :
				stack.append(top.left)
			if top.right :
				stack.append(top.right)
	return cnt
