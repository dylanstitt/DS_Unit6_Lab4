# Implementation & testing of breadth traversal and get height
# Import file
from TEST_CODE import *
import os
from BinaryTree import BinaryTree

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''


def main():
    BT = BinaryTree()
    initialize(BT)

    # Tree Review!
    # This is not a test and has nothing to do with your code
    VIEW_tree()

    # TEST 1 - Test breadth_traversal()
    # BEFORE TESTING: implement breadth_traversal()
    TEST_breadth_traversal(BT)

    # TEST 2 - Test get_height()
    # BEFORE TESTING: implement get_height()
    TEST_get_height(BT)

    # TEST 3 - Test docstrings()
    # BEFORE TESTING: implement docstrings()
    TEST_docs(BT)


if __name__ == "__main__":
    os.system("cls")
    main()