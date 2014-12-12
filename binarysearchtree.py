class Node(object):
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def append_node(self, value):
    	new_node = Node(value)
        if not self.root:
            # if there's no root (e.g. this is first node), set root to new node
            self.root = new_node
        else:
            # start search at root
            # "node" is a marker for where we currently are
            node = self.root
            while new_node.value != node.value: # as long as node hasn't already been added
                if new_node.value < node.value and node.left:
                    # if node exists to the left, move left --> new root
                    node = node.left
                elif new_node.value < node.value:
                    # set node.left to new_node (add to tree)
                    node.left = new_node

                elif new_node.value > node.value and node.right:
                    # checks if node to right exists, move right --> new root
                    node = node.right

                elif new_node.value > node.value:
                    # set node.right to new_node (add to tree)
                    node.right = new_node

    def lookup(self, value, node=None):
    	# @param self is the instance of the tree
    	# @param value is the value i'm searching for
    	# node is where to start but must assign value later
    	if node == None:
    		# start looking at the top of the tree
    		node = self.root
    	if value > node.value:
    		if node.left is None:
    			return None
    		return node.right.lookup(value, node = node.right)
    	elif value > node.value:
    		if node.right is None:
    			return None
    		return node.left.lookup(value, node = node.left)
    	else:
    		return True

    def depth_first_traversal(self, node):
        if node:
            #if you printed first it would be "pre ordered"
            self.depth_first_traversal(node.left)
            # print here because you have no more left values so it will be "in order"
            print node.value
            self.depth_first_traversal(node.right)
            # if you print here it would be "post order"
        return


t = BinarySearchTree()

node_options = [9, 5, 13, 1, 6]
for i in node_options:
	t.append_node(i)

t.depth_first_traversal(t.root)



# depth first traversal
# go to my left node go to my right node and return
# go down as far as you can and then cover all options
# use this if you want to check out all the nodes
# when you have nothing to the left you can begin printing, then the nodes will 
# be in order


