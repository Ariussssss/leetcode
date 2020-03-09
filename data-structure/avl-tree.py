# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-26 17:38:30

from tree import printTree
import random
from bstree import BinarySearchTree

class AVLTreeNode(BinarySearchTree):

    @staticmethod
    def changeRoot(root, old, new):
        if root == None:
            pass
        elif root.left == old:
            root.left = new
        else:
            root.right = new
        new.root = root

    def singleRotate(self, toRight: bool=True):
        # print()
        # printTree(self)
        if toRight:
            root = self.root
            right = self
            mid = self.left
            left = mid.left
            self.changeRoot(root, self, mid)
            right.left = mid.right
            mid.root, mid.left, mid.right = root, left, right
        else:
            root = self.root
            left = self
            mid = self.right
            right = mid.right
            self.changeRoot(root, self, mid)
            left.right = mid.left
            mid.root, mid.left, mid.right = root, left, right
        if left:
            left.root = mid
        if right:
            right.root = mid

    def doubleRoute(self, toRight: bool=True):
        target = self.right if toRight else self.left
        target.singleRotate(toRight)
        self.singleRotate(not toRight)

    def check(self):
        left = self.left.depth if self.left else 0
        right = self.right.depth if self.right else 0
        return (left - right) in [-1, 0, 1]

    def joinAVL(self, node):
        self.join(node)
        if not self.check():
            target = node
            while target.check():
                target = target.root
            if target.left and target.left.find(node.val):
                if target.left.left and target.left.left.find(node.val):
                    target.singleRotate(True)
                else:
                    target.doubleRoute(False)
            else:
                if target.right.left and target.right.left.find(node.val):
                    target.doubleRoute(True)
                else:
                    target.singleRotate(False)
        return self.head
    # bug
    def dele(self, node):
        if node.left == None and node.right == None:
            if node.root:
                if node.root.left == node:
                    node.root.left = None
                else:
                    node.root.right = None
        elif node.left != None and node.right != None:
            target = node.left
            while target.right:
                target = target.right
            self.dele(target)
            self.changeRoot(node.root, node, target)
            target.left = node.left
            target.right = node.right
        else:
            child = node.left if node.left else node.right
            self.changeRoot(node.root, node, child)

            

def bstbuild():
    a, b, c, d, e, f = [AVLTreeNode(x) for x in range(1, 7)]
    [e.join(x) for x in [a,b,c,d,f]]
    return e

def avlbuild():
    head = AVLTreeNode(1)
    for y in [AVLTreeNode(x) for x in range(2, 6)]:
        print(y.val)
        head = head.joinAVL(y)
    return head.head

if __name__ == '__main__':
    # e = bstbuild()
    # e.zOrder(e)
    e = avlbuild()
    e.zOrder(e)
    a = AVLTreeNode(5)
    e.joinAVL(a)
    e.dele(a)
    e.head.zOrder(e)
    e.postOrder(printTree, e)
