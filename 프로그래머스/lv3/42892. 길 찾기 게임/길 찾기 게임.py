import sys

class Node:
    def __init__(self, number, x, y):
        self.left = False
        self.right = False
        self.number = number
        self.x = x
        self.y = y

def solution(nodeinfo):
    sys.setrecursionlimit(1000000)
    
    nodeinfo = [(index+1, value[0], value[1]) for index, value in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: -x[2])
    root = Node(nodeinfo[0][0], nodeinfo[0][1], nodeinfo[0][2])
    
    for place in nodeinfo[1:]:
        target = root
        index, x, y = place
        node = Node(index, x, y)
        while True:
            if x < target.x:
                if not target.left:
                    target.left = node
                    break
                target = target.left
            else:
                if not target.right:
                    target.right = node
                    break
                target = target.right
    
    answer = [[], []]
    def preorder(node):
        answer[0].append(node.number)
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)
    preorder(root)
    
    def postorder(node):
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)
        answer[1].append(node.number)
    postorder(root)
    
    return answer