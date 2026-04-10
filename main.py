from RBTree import RBTree
from dictionary import Dictionary
def test():
    tree = RBTree()
    tree.insert(122)
    tree.insert(0)
    tree.insert(123)
    tree.insert(12)
    tree.insert(11)

    print(tree.search(12))
    print(tree.search(1))
    print(tree.root.left.data)
    print("//////////////////////")
    print(tree.get_size())
    print(tree.get_black_height())
    print(tree.get_height())

def view_menu():
    print("English Dictionary Menu")
    print("1.Load Dictionary form file")
    print("2.Insert a new word")
    print("3.Search a word")
    print("4.Display Dictionary statistics")
    print("5.Exit")

def main():
    dic = Dictionary()
    while(True):
        print("===============================================")
        view_menu()
        choice = input("Enter your choice form 1 to 5: ").strip()
        if choice == "1":
            fileName = "/Users/amlegomaa/RedBlackTrees/Dictionary.txt"
            #fileName = input("Enter file name: ").strip()
            if fileName is None:
                print("INVALID FILE")
            else:
                dic.load_from_file(fileName)
        elif choice == "2":
            word = input("Enter the word to insert: ").strip()
            if word is None:
                print("INVALID input")
            else:
                dic.insert_word(word)
        elif choice == "3":
            word = input("Enter the word to search: ").strip()
            if word is None:
                print("INVALID input")
            else:
                dic.lookup_word(word)
        elif choice == "4":
            dic.print_stats()
        elif choice == "5":
            exit()
        else:
            print("INVALID input please choose form 1 to 5.")
main()