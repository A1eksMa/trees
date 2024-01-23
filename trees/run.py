#!/usr/bin/python3
import random


def sid(n=4):
    ''' Generate random system id '''
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    id = ''.join(random.choice(string) for i in range(n))
    return id


def singleton(cls):
    '''
    This decorator uses Singleton pattern,
    and sets the attributes of a new object based on a previously instance,
    if one exists
    '''

    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        else:
            existing_instance = instances[cls]
            for key, value in existing_instance.__dict__.items():
                if key not in kwargs:
                    kwargs[key] = value
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class Tree():
    '''
    It's a final class - The Tree.
    '''

    def __init__(self):
        self.root = self.Root()

        # Tree like a list of Nodes
        self.list_nodes = []
        self.list_nodes.append(self.root)

        # Tree like a dictionary:
        self.dict_nodes = {}
        self.dict_nodes.update(self.root.get_dict())

    def __repr__(self):
        print("Tree like a dict:", self.dict_nodes)
        print("Tree like a list:", self.list_nodes)


    def add_branch(self, parent=None):
        self.node = self.Branch(parent=parent)

        # Tree like a list of Nodes
        for i in range(len(self.list_nodes)):
            if self.list_nodes[i].node == self.node.parent:
                self.list_nodes[i].add_child(self.node.node)
                self.list_nodes.append(self.node)
            else:
                raise ValueError("Parent's element not found")

        # Tree like a dictionary:
        for i in range(len(self.list_nodes)):
            self.dict_nodes.update(self.list_nodes[i].get_dict())

        del self.node


    class Node():
        '''
        This abstract node of Tree
        '''
        class Seed():
             def __init__(self):
                self.sid = sid()

        class Children():
            pass

        def __init__(self, node=None, parent=None, children=None):
            self.node = node if node is not None else sid()
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

        def get_dict(self):
            return {self.node: (self.parent, self.children)}

    @singleton
    class Root(Node):
        '''
        It's a Root of Tree, singleton class, that parent is None always
        '''

        def __init__(self, node=None, parent=None, children=None):
            super().__init__(node if node is not None else sid(),
                             parent,
                             children)

            # We have one root,-> we can give it unique name
            self.node = 'root'


            # The Root has no parent
            self.parent = None


            def set_parent(self, parent):
                print('The Root element has no parent')


    class Branch(Node):
        '''
        It's a Branch of Tree class, that must have a parent
        '''

        def __init__(self, node=None, parent=None, children=None):
            ''' Set up defaults attributes '''
            super().__init__(node if node is not None else sid(),
                             parent,
                             children)

            while parent is None:
                parent = input('Set parent: ')
                self.set_parent(parent)

    class Leaf(Branch):
        '''
        Leaf class have no children.
        This is endpoint of Tree.
        '''

        def __init__(self, node=None, parent=None, children=None):
            ''' Set up defaults attributes '''
            super().__init__(node if node is not None else sid(),
                             parent,
                             children)

            # The Root has no parent
            self.children = []

        def add_child(self, child):
            print('The Leaf element has no children')




def command_mode(unit = ''):
    q = None
    command = ''
    while command != 'q':
        command = input(unit + ' >>> ')
        try:
            exec(command)
        except Exception as e:
            print('Error:', e)
    return


command_mode('main')
