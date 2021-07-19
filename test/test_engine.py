import unittest
from engine import get_endpoint

class TestGetEndpoint(unittest.TestCase):
    
    def test_return_url(self):
        endpoint = get_endpoint(1337)
        self.assertIsInstance(endpoint, str)
        self.assertEqual(endpoint[:5], 'https')

if __name__ == '__main__':
    unittest.main()