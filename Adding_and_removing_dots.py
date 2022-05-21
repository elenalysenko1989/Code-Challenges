def add_dots(test):
    return '.'.join(test)
    
def remove_dots(test):
    return test.replace('.', '')

print(remove_dots(add_dots('machine')))