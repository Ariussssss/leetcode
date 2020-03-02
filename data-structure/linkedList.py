# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-26 17:30:03


class LinkNode:
    def __init__(self, val, child=None):
        self.val = val
        self.child = child

    @property
    def tail(self):
        return self if not self.child\
            else self.child.tail

    def traversal(self, fn):
        rnow = self
        while rnow:
            fn(rnow)
            rnow = rnow.child

    def reverse(self):
        parent = self.child
        self.child = None
        if parent:
            result = parent.reverse()
            parent.child = self
            return result
        else:
            return self

class DuLNode(LinkNode):
    """Doubly linked list"""
    def __init__(self, val, child=None, parent=None):
        super(DuLNode, self).__init__(val, child)
        self.parent = parent

    @property
    def head(self):
        return self if not self.parent\
            else self.parent.head

    def reverse(self):
        parent = None
        ancestor = self.head
        while ancestor:
            parent, ancestor.child, ancestor.parent, ancestor =\
                ancestor, parent, ancestor.child, ancestor.child
        return parent.head

    @staticmethod
    def transfer_duLNode(node):
        parent = None
        rnow = node
        while rnow:
            nnow = DuLNode(rnow.val, rnow.child, parent)
            if parent:
                parent.child = nnow
            parent = nnow
            rnow = rnow.child
        return parent.head

def build():
    def createLinkNode(key):
        if key == 0:
            return LinkNode(key)
        return LinkNode(key, createLinkNode(key - 1))
    length = 10
    return createLinkNode(length)

def printLinkNode(node):
    child_val = None if not node.child else node.child.val
    print('[val:{0},child:{1}]'.format(node.val, child_val))

def printDuLinkList(node):
    child_val = None if not node.child else node.child.val
    parent_val = None if not node.parent else node.parent.val
    print('[val:{0},child:{1},parent:{2}]'.format(node.val, child_val, parent_val))

if __name__ == '__main__':
    head = build()
    head.traversal(printLinkNode)
    res = []
    print()
    head = head.reverse()
    head.traversal(printLinkNode)
    print()
    head = DuLNode.transfer_duLNode(head)
    head.traversal(printDuLinkList)
    print()
    head = head.reverse()
    [printDuLinkList(x) for x in res]
    head.traversal(printDuLinkList)
