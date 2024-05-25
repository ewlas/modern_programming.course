import unittest
import gc

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

class TestMemory(unittest.TestCase):
    def test_modify_value(self):
        x = 5
        result = modify_value(x)
        self.assertEqual(x, 5) 
        self.assertEqual(result, 6) 

    def test_modify_reference(self):
        lst = [1, 2, 3]
        modify_reference(lst)
        self.assertEqual(lst, [1, 2, 3, 1]) 

    def test_stack_allocation(self):
        stack_allocation() 

    def test_heap_allocation(self):
        heap_allocation() 

    def test_garbage_collection(self):
        create_objects() 

if __name__ == '__main__':
    unittest.main()
