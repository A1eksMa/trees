import random


def sid(n=3):
    ''' Generate random system id '''
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    id = ''.join(random.choice(string) for i in range(n))
    return id


class Node:
    def __init__(self, node, parent=None, children=None):
        self.node = node
        self.parent = parent
        self.children = children if children is not None else []

    def add_child(self, child):
        if not self.children:
            self.children = [child]
        elif child in self.children:
            print(f'Chid {child} already exist')
        else:
            self.children.append(child)

    def remove_child(self, child):
        try:
            self.children.remove(child)
        except Exception as e:
            print(f'Impossible to remove child {child}:', e)

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def __repr__(self):
        return f"'{self.node}' : ({self.parent}, {self.children})"


class Root(Node):
    '''
    It's a Root of Tree, singleton class, that parent is None always
    '''

    # Singleton pattern
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self, node, parent=None, children=None):
        # node need save as a primary singleton object node !!!
        pass
        super().__init__(node, parent, children)
        self.parent = None


    def set_parent(self, parent):
        print('The Root element has no parent')
        self.parent = None


class Branch(Node):
    '''
    It's a Branch of Tree class, that must have a parent
    '''

    def __init__(self, node, parent=None, children=None):
        ''' Set up defaults attributes '''
        super().__init__(node, parent, children)
         
        while parent is None:
            parent = input('Set parent: ')
            self.set_parent(parent)


class Tree:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def get_node(self, name):
        return self.nodes[name]

    def remove_node(self, name):
        pass
