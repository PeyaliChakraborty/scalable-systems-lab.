import unittest
from algorithms_practice import binary_search

class TestSearchAlgorithms(unittest.TestCase):
    
    def test_element_found(self):
        """Verify the algorithm finds an existing element."""
        data = [10, 20, 30, 40, 50]
        self.assertEqual(binary_search(data, 30), 2)
        
    def test_element_not_found(self):
        """Verify the algorithm returns -1 for missing elements."""
        data = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(data, 99), -1)

    def test_empty_list(self):
        """Verify the algorithm handles empty input gracefully."""
        self.assertEqual(binary_search([], 10), -1)

if __name__ == "__main__":
    unittest.main()
