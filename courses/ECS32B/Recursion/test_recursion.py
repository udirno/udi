#!/usr/bin/env python3
import unittest
import recursion as rs

''' run as (example)
python -m unittest test_samples.PySampleTests.test_sort
'''

# Define a test fixture for pykatas
class PySampleTests(unittest.TestCase):
    def test_func3(self):
        self.assertEqual(rs.fun3(0), 5)
        self.assertEqual(rs.fun3(1), 7)
        self.assertEqual(rs.fun3(2), 11)
        self.assertEqual(rs.fun3(3), 23)
        self.assertEqual(rs.fun3(4), 41)
        self.assertEqual(rs.fun3(5), 75)
        self.assertEqual(rs.fun3(6), 139)        

    def test_binary_strings(self):
        self.assertEqual([bstr for bstr in rs.binary_strings('0XX1')],
                         ['0001', '0011', '0101', '0111'])
        self.assertEqual([bstr for bstr in rs.binary_strings('0X1X')],
                         ['0010', '0011', '0110', '0111'])
        
    def test_get_best_backpack(self):
        items = []
        self.assertEqual(rs.get_best_backpack(items, 0), items)
        self.assertEqual(rs.get_best_backpack(items, 10), items)        

        items = [rs.Item('Ring', 10, 500)]
        self.assertEqual(rs.get_best_backpack(items, 5), [])
        self.assertEqual(rs.get_best_backpack(items, 10), items)        
        
        items = [rs.Item('Ring', 10, 500),
                 rs.Item('Diamond', 25, 2),
                 rs.Item('Necklace', 68, 10000)]
        self.assertEqual(rs.get_best_backpack(items, 5), [])
        self.assertEqual(rs.get_best_backpack(items, 35), items[:-1])
        self.assertEqual(rs.get_best_backpack(items, 68), items[-1:])


        items = [rs.Item('Ring', 43, 43),
                 rs.Item('Earring', 36, 30),
                 rs.Item('Necklace', 80, 100),
                 rs.Item('Diamond', 70, 68)]
        self.assertEqual(rs.get_best_backpack(items, 5), [])
        self.assertEqual(rs.get_best_backpack(items, 35), [])
        self.assertEqual(rs.get_best_backpack(items, 79), items[:2])

        items = [Item('Ring', 43, 43),
                 Item('Earring', 36, 40),
                 Item('Necklace', 80, 80),
                 Item('Diamond', 70, 68)]
        self.assertEqual(rs.get_best_backpack(items, 5), [])
        self.assertEqual(rs.get_best_backpack(items, 35), [])
        self.assertEqual(rs.get_best_backpack(items, 80), items[:2])

        
        
if __name__ == '__main__':
    unittest.main()
