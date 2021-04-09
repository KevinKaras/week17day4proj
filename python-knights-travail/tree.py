class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent):
        if parent == None:
            self._parent = None
            return
        if self._parent == parent:
            print()
            return
        #node1.parent(node2) and node1 is already the parent.
        elif self._parent != parent and self._parent == None:
            self._parent = parent
            parent.add_child(self)
        # node1.parent = node2
        else:  
            self._parent.remove_child(self)
            self._parent = parent
            parent.add_child(self)

    
    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node.parent = self
    

    def remove_child(self, node):
        if node in self._children:
            node.parent = None
            self._children.remove(node)


    def depth_search(self, value):           
        if self._value == value:
            return self
    
        for child in self._children:
            node = child.depth_search(value)
            if node is not None:
                return node

    def breadth_first(self, value):
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return node
            queue.extend(node._children)

    def __repr__(self):
        # return f'<Node value: test, children: test>'
        return f'<Node value {self._value} children {self._children}>'
        


node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")
node4 = Node("root4")
node5 = Node("root5")
node6 = Node("root6")
node7 = Node("root7")

node5.parent = node2
node4.parent = node2 
node2.parent = node1 

node7.parent = node3 
node6.parent = node3
node3.parent = node1 





# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)

