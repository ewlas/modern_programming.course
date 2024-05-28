import unittest
import gc
import tracemalloc
import psutil

def modify_value(x):
    x += 1
    return x

def modify_reference(lst):
    lst.append(1)

def stack_allocation():
    x = 5  

def heap_allocation():
    x = [5]  

def create_objects():
    a = [1, 2, 3]
    b = a
    del a
    gc.collect()  

