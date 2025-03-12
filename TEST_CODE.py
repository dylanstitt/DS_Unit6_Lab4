##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN
Y = Fore.YELLOW

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################

def result(flag):
    if flag:
        return f"{G}PASSED{W}"

    return f"{R}FAILED{W}"


def initialize(BT):
    a = BT.add_root("A")
    b = BT.add_left(a, "B")
    c = BT.add_right(a, "C")
    d = BT.add_left(b, "D")
    e = BT.add_right(b, "E")
    f = BT.add_left(e, "F")


def VIEW_tree():
    print("~" * 50)
    print(f"{P}This is what your tree will look\nlike for the next round of tests. {W}\n")

    print("""
            (A)
            / \\
          (B) (C)
          / \\ 
        (D) (E)
            /
          (F)

    """)
    print("~" * 50, "\n\n")


def TEST_breadth_traversal(BT):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Breadth First Traversal{W}\n")

    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    res = BT.breadth_traversal()

    print(f"Expected Output: {expected}")
    print(f"Actual Output: {Y}{res}{W}\n")

    test = res == expected
    print(f"Result matches expected output: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_get_height(BT):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: get height{W}\n")

    expected = 3
    res = BT.get_height()

    print(f"Expected Output: {expected}")
    print(f"Actual Output: {Y}{res}{W}\n")

    test = res == expected
    print(f"Result matches expected output: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_docs(BT):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    doc = BT.breadth_traversal.__doc__
    if doc != None:
        print(f"{B}breadth_traversal() Documentation:{W} {doc}\n")
    else:
        print(f"{R}breadth_traversal() Documentation Missing{W}\n")

    doc = BT.get_height.__doc__
    if doc != None:
        print(f"{B}get_height() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_height() Documentation Missing{W}\n")

    print("~" * 50, "\n\n")

# print(f": {result(test)}")