import unittest
from lab4 import *

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
        before = len(gc.get_objects())
        stack_allocation()
        after = len(gc.get_objects())
        self.assertEqual(before, after)

    def test_heap_allocation(self):
        tracemalloc.start()
        before = tracemalloc.get_traced_memory()[1]
        heap_allocation()
        after = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        self.assertGreater(after, before, "Heap should increase")

    def test_garbage_collection(self):
        large_object = bytearray(1024 * 1024 * 100)  

        process = psutil.Process()
        before_allocation = process.memory_info().rss  

        del large_object
     
        gc.collect()
        
        after_collection = process.memory_info().rss

        self.assertLess(after_collection, before_allocation)


if __name__ == '__main__':
    unittest.main()