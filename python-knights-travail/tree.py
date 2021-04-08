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
    
    def add_child(self, node):
        if node in self._children == None:
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

node_a.add_child(node_b)


print(node_a.children)

print(node_a)
        
        
