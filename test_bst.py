from bst_pure import BinarySearchTree

# def test_insert():
#     bst = BinarySearchTree(1)
#     for i in xrange(955):
#         bst.insert(i)

#     assert bst.contains(1) == True
#     assert bst.contains(5) == True
#     assert bst.contains(250) == True
#     assert bst.contains(500) == True
#     assert bst.contains(754) == True
#     assert bst.contains(930) == True
    
# def test_pretty_print():
#     bst = BinarySearchTree(1)
#     for i in xrange(50):
#         bst.insert(i)
#     bst.pretty_print()


def test_delete():
    bst = BinarySearchTree(1)
    for i in xrange(10):
        bst.insert(i)
    x = bst.delete(5)
    assert bst.contains(5) == False
    assert x == 5
