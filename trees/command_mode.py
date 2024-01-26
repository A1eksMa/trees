
root = Tree.Node(Tree.Node.Seed('root'), None,[])
print(root)

a = Tree.Node.Seed()
root.add_child(a)
print(a, 'add to root')

b = Tree.Node.Seed()
root.add_child(b)
print(b, 'add to root')

c = Tree.Node.Seed()
root.add_child(c)
print(c, 'add to root')


print(root)



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
