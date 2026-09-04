# test_driftnook.py
"""
Tests for DriftNook module.
"""

import unittest
from driftnook import DriftNook

class TestDriftNook(unittest.TestCase):
    """Test cases for DriftNook class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DriftNook()
        self.assertIsInstance(instance, DriftNook)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DriftNook()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
