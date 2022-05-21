def flatten(main_list):
    new_list = []
    for old_list in main_list: new_list.extend(old_list)
    return new_list
print(flatten([[1, 2], [3, 4]]))