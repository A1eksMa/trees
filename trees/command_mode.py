

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
