class BinarySearchtreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchtreeNode(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchtreeNode(data)
        
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
        
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchtreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root
arr = [2,3,1,4,7,5,6]
arr_tree = build_tree(arr)
print("Inorder traversal gives this sorted list:",arr_tree.in_order_traversal())


