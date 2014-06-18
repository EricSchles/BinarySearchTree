from bst_pure import BinarySearchTree as bst

bt = bst(1)
for i in xrange(50):
    bt.insert(i)

for i in xrange(50):
    if not bt.contains(i):
        print "contains failed"

x =bt.delete(5)

print bt.contains(1)
