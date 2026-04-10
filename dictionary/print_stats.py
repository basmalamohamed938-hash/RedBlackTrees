def print_stats(dictionary):
    print("===============================================")
    print(f"The size of tree is: {dictionary.tree.get_size()}")
    print(f"The height of tree is: {dictionary.tree.get_height()}")
    print(f"The black height of tree is: {dictionary.tree.get_black_height()}")