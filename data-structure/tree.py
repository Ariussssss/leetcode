# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-26 15:54:39


class TreeNode(object):
    def __init__(self, val, root=None, left=None, right=None):
        self.val = val
        self.root = root
        self.left = left
        self.right = right

    @property
    def head(self):
        root = self
        while root.root:
            root = root.root
        return root

    @property
    def depth(self):
        left = self.left.depth if self.left else 0
        right = self.right.depth if self.right else 0
        return 1 + (left if left > right else right)

    @property
    def width(self):
        right, left = 0, 0
        rightNode, leftNode = self.right, self.left
        while rightNode:
            right += 1
            rightNode = rightNode.right
        while leftNode:
            left += 1
            leftNode = leftNode.left
        return left + 1 + right

    @staticmethod
    def postOrder(fn, node):
        if node.left:
            TreeNode.postOrder(fn, node.left)
        if node.right:
            TreeNode.postOrder(fn, node.right)
        fn(node)

    @staticmethod
    def zOrder(node):
        res = {}
        def z_order_sup(node, idx=0):
            key = str(idx)
            if key not in res:
                res[key] = [str(node.val)]
            else:
                res[key].append(str(node.val))
            if node.left:
                z_order_sup(node.left, idx + 1)
            if node.right:
                z_order_sup(node.right, idx + 1)
        z_order_sup(node)
        for x in res:
            print(' '.join(res[x]))

    @staticmethod
    def bfs(fn, node):
        pass

"""
   e
  / \
 a   d
 /\   \ 
b  c   f
"""

def build():
    a, b, c, d, e, f = [TreeNode('a'),
        TreeNode('b'),
        TreeNode('c'),
        TreeNode('d'),
        TreeNode('e'),
        TreeNode('f')]
    e.left = a
    e.right = d
    a.root = e
    a.left = b
    a.right = c
    b.root = a
    c.root = a
    d.root = e
    d.right = f
    f.root = d
    return e

def printTree(tree):
    val = tree.val
    root = None if not tree.root else tree.root.val
    left = None if not tree.left else tree.left.val
    right = None if not tree.right else tree.right.val
    print ('node {0}: root {1} left {2} right {3}'.format(\
        val, root, left, right))

if __name__ == '__main__':
    tree = build()
    TreeNode.zOrder(tree)
    print (tree.depth)
    print (tree.width)