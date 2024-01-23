import random


class Tree():
    '''
    It's a main class - The Tree.
    '''

    class Node():
        '''
        This abstract node of Tree
        '''


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
                return id

            def __init__(self, id=None):
                self.sid = id if id is not None else self.sid()


        class Children():
            pass


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
