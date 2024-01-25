import random


class Tree():
    '''
    It's a main class - The Tree.
    '''

    class Node():
        '''
        This abstract node of Tree
        '''
        def __init__(self, node=None, parent=None, children=None):
            self.validate(node, parent, children)
            self.node = node if node is not None else self.Seed()
            self.parent = parent
            self.children = children if children is not None else []

        def validate(self, node, parent, children):
            self.valid(node)
            self.valid(parent)
            self.valid(children)
            
        def valid(self, node):
            pass
                
        def valid(self, parent):
            pass

        def valid(self, children):
            pass 

        def __repr__(self):
            return f"Node: {self.node}\nParent: {self.parent}\nChildren: {self.children})\n"

        def __str__(self):
            return self.node.sid

        def __eq__(self, other):
            if isinstance(other, Tree.Node):
                return self.node.sid == other.node.sid
            return False

        def __hash__(self):
            return hash(self.node.sid)

        class Seed():
            '''
            Unique system id (sid): random chars
            '''

            # Set default longsize of sid
            __n = 4

            def sid(self, n=__n):
                '''
                Generate random system id
                '''
                string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                id = ''.join(random.choice(string) for i in range(n))
                while hash(id) <= 0:
                    id = ''.join(random.choice(string) for i in range(n))
                return id

            def __init__(self, id=None):
                self.sid = id if id is not None else self.sid()

            def __repr__(self):
                return ('Object type: ' +  str(self.__class__)  + '\n' +
                        'Object ID: ' + str(id(self)) + '\n' +
                        'System Identificator (sid): ' + self.sid)

            def __str__(self):
                return self.sid

            def __eq__(self, other):
                if isinstance(other, Tree.Node.Seed):
                    return self.sid == other.sid
                return False

            def __hash__(self):
                return hash(self.sid)

            def __bool__(self):
                if isinstance(self.sid, str) and len(self.sid) == self.__n and hash(self.sid) > 0:
                    allowed_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    if all(char in allowed_chars for char in self.sid):
                        return True
                return False


    # And other classes, based on Node() class:

    class Root(Node):
        '''
        It's a Root of Tree, singleton class, that parent is None always
        '''
        pass


    class Branch(Node):
        '''
        It's a Branch of Tree class, that must have a parent
        '''
        pass


    class Leaf(Branch):
        '''
        Leaf class have no children.
        This is endpoint of Tree.
        '''
        pass
