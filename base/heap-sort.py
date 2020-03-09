# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-03-19 20:14:30


import random

def MAX_Heapify(heap,HeapSize,root):
    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    print heap
    if larger != root:
        heap[larger],heap[root] = heap[root],heap[larger]
        MAX_Heapify(heap, HeapSize, larger)

def Build_MAX_Heap(heap):
    HeapSize = len(heap)
    for i in xrange((HeapSize -2)/2,-1,-1):
        MAX_Heapify(heap,HeapSize,i)

def HeapSort(heap):
    Build_MAX_Heap(heap)
    print heap
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0)
    print heap
    return heap

def heap_sort(heap):
    l = len(heap)
    res = []
    for x in range(l):
        Build_MAX_Heap(heap)
        res.append(heap.pop(0))
    return res

if __name__ == '__main__':
    a = [30,50,57,77,62,78,94,80,84]
    HeapSort(a)
    heap_sort(a)
    # b = [random.randint(1,1000) for i in range(1000)]
    # print b
    # HeapSort(b)
    # print b

