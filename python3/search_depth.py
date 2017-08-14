#深度优先查找
def depth_tree(tree_node):
	if tree_node is not None:
		print(tree._data)
		if tree_node._left is not None:
			return depth_tree(tree_node._lefg)
		if tree_node._right is not None:
			return depth_tree(tree_node._right)

#广度优先查找
def level_queue(root):
	if root is None:
		return
	my_queue = []
	node = root
	my_queue.append(node)
	while my_queue:
		node = my_queue.pop(0)
		print (node.elem)
		if node.lchild is not None:
			my_queue.append(node.lchild)
		if node.rchild is not None:
			my_queue.append(node.rchild)					
