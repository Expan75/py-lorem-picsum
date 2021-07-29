import os
import unittest
import engine 


class TestGetEndpoint(unittest.TestCase):
    
    def test_return_url_w_seed(self):
        test_seed = 1337
        url = engine.get_image_url(test_seed)
        self.assertIsInstance(url, str)
        self.assertEqual(url[:5], 'https')
        self.assertTrue('seed' in url and str(test_seed) in url)
    
    def test_return_url_wo_seed(self):
        self.assertRaises(TypeError, engine.get_image_url)


class TestSeedGeneration(unittest.TestCase):

    seed = 10
    n_seeds = 100
    generated_seeds = engine.generate_seeds(seed, n_seeds)

    def test_generated_seeds(self):
        self.assertTrue(len(self.generated_seeds) == self.n_seeds)
    
    def test_sorting(self):
        self.assertTrue(sorted(self.generated_seeds) == self.generated_seeds)
    
    def test_uniqueness(self):
        unique_seeds = set(self.generated_seeds)
        self.assertTrue(len(unique_seeds) == len(self.generated_seeds))


class TestDirectoryValidation(unittest.TestCase):

    tmp_directory = 'tmp-image-directory-verify'

    @classmethod    
    def tearDown(self) -> None:
        for file in os.listdir(self.tmp_directory):
            filepath = os.path.join(self.tmp_directory, file)
            os.remove(filepath)
        os.removedirs(self.tmp_directory)

    def test_directory_not_exists(self):
        engine.verify_valid_directory(self.tmp_directory)
        self.assertTrue(os.path.isdir(self.tmp_directory))

    def test_directory_exists(self):
        os.makedirs(self.tmp_directory)
        self.assertTrue(os.path.isdir(self.tmp_directory))
        engine.verify_valid_directory(self.tmp_directory)
        self.assertTrue(os.path.isdir(self.tmp_directory))
        

class TestDownloadImages(unittest.TestCase):

    seed = 1
    n_images = 10
    tmp_directory = 'tmp-image-directory'

    @classmethod
    def setUp(self) -> None:
        engine.verify_valid_directory(self.tmp_directory)

    @classmethod    
    def tearDown(self) -> None:
        for file in os.listdir(self.tmp_directory):
            filepath = os.path.join(self.tmp_directory, file)
            os.remove(filepath)
        os.removedirs(self.tmp_directory)

    def test_image_downloads(self):
        engine.download_images(master_seed=self.seed, n_images=self.n_images, image_directory=self.tmp_directory)
        images = os.listdir(self.tmp_directory)
        self.assertTrue(len(images) == self.n_images)
    
if __name__ == '__main__':
    unittest.main()