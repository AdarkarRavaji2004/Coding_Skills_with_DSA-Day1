# class Tree:
#     def __init__(self,value):
#         self.value = value
#         self.children = []
    
#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret = "  " * level + str(self.value) + "\n"
#         for child in self.children:
#             ret+=child.__str__(level+1)
#         return ret

# rootNode=Tree("Drinks")
# hot = Tree("Hot")
# cold = Tree("Cold")
# tea = Tree("Tea")
# coffee = Tree("Coffee")
# nonAlcoholic = Tree("Non-Alcoholic")
# Alcoholic = Tree("Alcoholic")

# #add child nodes in tree
# rootNode.addChild(hot)
# rootNode.addChild(cold)

# hot.addChild(tea)
# hot.addChild(coffee)

# cold.addChild(nonAlcoholic)
# cold.addChild(Alcoholic)

# print(rootNode)

#================================
#Binary tree:
#tree that has at most 2 child node

#full Binary Tree :-
# Each node has either 0 or 2 children
# no single children

#complete Binary tree :-
#All levels ecxept possibly the last are completely filled
#Nodes in the last level are filled from left and right

#Perfect Binary Tree :-
#All internal nodes have exactly two nodes 
#All leaf nodes are at the same level

#================================================================================================================
#Creation of Tree :
# class Tree:
#     def __init__(self,data):
#         self.data = data
#         self.children = []

#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret = "  " * level + str(self.data) + "\n"
#         for child in self.children:
#             ret+=child.__str__(level+1)
#         return ret
    
# rootNode = Tree("N1")
# n2 = Tree("N2")
# n3 = Tree("N3")
# n4 = Tree("N4")
# n5 = Tree("N5")
# n6 = Tree("N6")
# n7 = Tree("N7")
# n8 = Tree("N8")
# n9 = Tree("N9")

# rootNode.addChild(n2)
# rootNode.addChild(n3)

# n2.addChild(n4)
# n2.addChild(n5)

# n3.addChild(n6)
# n3.addChild(n7)

# n4.addChild(n8)
# n4.addChild(n8)

# print(rootNode)

#====================================================================================================
#                       Binary search Tree
#-----------------------------------------------------------------------------------------------------
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertNode(self.root,data)

    def insertNode(self,rootNode,data):
        if data < rootNode.data:
            if rootNode.left is None:
                rootNode.left = Node(data)
            else:
                self.insertNode(rootNode.left,data)
        else:
            if rootNode.right is None:
                rootNode.right = Node(data)
            else:
                self.insertNode(rootNode.left,data)


btObj = BinaryTree()
btObj.insert(50)
btObj.insert(30)
btObj.insert(70)

print(btObj)