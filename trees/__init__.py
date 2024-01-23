class Tree():
    '''
    It's a main class - The Tree.
    '''

    class Node():
        '''
        This abstract node of Tree
        '''
        class Seed():
            pass

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
