
# # Global variable
# min_max_prompt = True

# def change_prompt():
#     if min_max_prompt:
#         min_max_prompt = False
#     else:
#         min_max_prompt = True

def min_max_instructions():
    print("** INSTRUCTIONS **")
    print("******************")
    print("****************************************************")
    print("*                     (3)                         |*")
    print("*                     /|\                         |*")
    print("*                    / |  \                       |*")
    print("*                  /   |    \                     |*")
    print("*                /     |      \                   |*")
    print("*              /       |        \                 |*")
    print("*            /         |          \               |*")
    print("*          /           |            \             |*")
    print("*        /             |              \           |*")
    print("*       (3)           (0)              (2)        |*")
    print("*      /   \          / \             /   \       |*")
    print("*     /     \        /   \           /     \      |*")
    print("*    /       \      /     \         /       \     |*")
    print("*   (3)      (9)   (0)    (7)      (2)      (6)   |*")
    print("*   / \      / \    |     / \      / \      / \   |*")
    print("* (2) (3)  (5) (9) (0)  (7) (4)  (2) (1)  (5) (6) |*")
    print("****************************************************")

    print("\n* Look at the example tree above and note the number of rows.")
    print("* For this Tree, there are 4 rows.")
    print("*---------------------------------------------------")
    input("Enter any key to continue...")
    print("\n* After entering the number of rows.")
    print("* You will be required to enter the number of nodes in each row.")
    print("* For this Tree:")
    print("* \t Row 1 - 1 node (always)")
    print("* \t Row 2 - 3 nodes")
    print("* \t Row 3 - 6 nodes")
    print("* \t Row 4 - 11 nodes")
    print("*---------------------------------------------------")
    input("Enter any key to continue...")
    print("\n* After entering the number of nodes for each row.")
    print("* You will be required to enter the numbers for each node.")
    print("* Since there are 11 nodes, you should enter eleven numbers separated by a comma (,)")
    print("* \t Example: 2,3,5,9,0,7,4,2,1,5,6")
    print("*---------------------------------------------------")
    print("* The program will do the rest.")
    input("Enter any key to go back to the menu...")

def get_tree_details():
    print("* Enter the number of rows.")

def make_min_max_tree(details):
    test = [[],[],[],[2,3,5,9,0,7,4,2,1,5,6]]