# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-26 17:38:30

from tree import TreeNode, printTree

class BinarySearchTree(TreeNode):
    def find(self, val):
        if self.val == val:
            return self
        elif self.val > val:
            if self.left:
                return self.left.find(val)
        else:
            if self.right:
                return self.right.find(val)
        return None

    def join(self, node):
        if node.val >= self.val:
            if self.right:
                self.right.join(node)
            else:
                self.right = node
                node.root = self
        else:
            if self.left:
                self.left.join(node)
            else:
                self.left = node
                node.root = self

    def suicide(self):
        if self.root:
            root = self.root
            if root.left == self:
                root.left = None
            else:
                root.right = None
            res = []
            if self.left:
                BinarySearchTree.postOrder(res.append, self.left)
            if self.right:
                BinarySearchTree.postOrder(res.append, self.right)
            def join(x):
                x.left = None
                x.right = None
                root.join(x)
            [join(x) for x in res]

    def delByKey(self, key):
        traversal = BinarySearchTree.postOrder
        sui_list = []
        def findNode(node):
            if node.val == key:
                sui_list.append(node)
        traversal(findNode, self)
        [x.suicide() for x in sui_list]

def bstbuild():
    a, b, c, d, e, f = [BinarySearchTree(1),
        BinarySearchTree(2),
        BinarySearchTree(3),
        BinarySearchTree(4),
        BinarySearchTree(5),
        BinarySearchTree(6)]
    [e.join(x) for x in [a,b,c,d,f]]
    return e

def printTree(tree):
    val = tree.val
    root = None if not tree.root else tree.root.val
    left = None if not tree.left else tree.left.val
    right = None if not tree.right else tree.right.val
    print ('node {0}: root {1} left {2} right {3}'.format(\
        val, root, left, right))

if __name__ == '__main__':
    tree = bstbuild()
    tree.delByKey(1)
    TreeNode.postOrder(printTree, tree)
    print (tree.depth)
    print (tree.width)