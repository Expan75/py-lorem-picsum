import unittest
from engine import get_image_url

class TestGetEndpoint(unittest.TestCase):
    
    def test_return_url_w_seed(self):
        url = get_image_url(1337)
        self.assertIsInstance(url, str)
        self.assertEqual(url[:5], 'https')
        self.assertEqual(len(url.split('/')) == 3)
    
    def test_return_url_wo_seed(self):
        url = get_image_url()
        self.assertIsInstance(url, str)
        self.assertEqual(url[:5], 'https')
        self.assertEqual(len(url.split('/')) == 2)

#class TestSeedGeneration(unittest.TestCase):
    #pass

if __name__ == '__main__':
    unittest.main()