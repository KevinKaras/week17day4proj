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
            print('Already the parent!')
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
            node._parent = self
    

    def remove_child(self, node):
        if node in self._children:
            node._parent = None
            self._children.remove(node)
 
    def __repr__(self):
        # return f'<Node value: test, children: test>'
        return f'<Node value {self._value} children {self._children}>'
        


node_a = Node('Anode')
node_b = Node('Bnode')
node_c = Node('Cnode')

# node_a.add_child(node_b)
# node_a.add_child(node_b)
# print(node_a.children)
# node_a.remove_child(node_b)
# print(node_b._parent)


# print(node_a.children)


node_b.parent = node_c
node_b.parent = node_c
node_b.parent = node_a

# print(node_b.parent)
# node_b.parent = node_c