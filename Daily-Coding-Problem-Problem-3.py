class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
# serialize
def serialize(node):
    val = node.val
    if node.left:
        left = serialize(node.left)
    else:
        left = None
    if node.right:
        right = serialize(node.right)
    else:
        right = None
    
    serialized = [val, left, right]
    return serialized
    
# deserialize
def deserialize(nodeSerialized):
    val = nodeSerialized[0]
    if nodeSerialized[1]:
        left = deserialize(nodeSerialized[1])
    else:
        left = None
    if nodeSerialized[2]:
        right = deserialize(nodeSerialized[2])
    else:
        right = None
    return Node(val, left, right)


    







# the code should be able to pass the following test:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
