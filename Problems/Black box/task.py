# use the function blackbox(lst) that is already defined
lst = [1, 2, 3]
if id(lst) == id(blackbox(lst)):
    print('modifies')
else:
    print('new')