from os.path import abspath, dirname, join
import unittest

TESTS_ROOT = join(dirname(abspath(__file__)))
ASSETS_ROOT = join(TESTS_ROOT, 'assets')
MODULE_ROOT = join(TESTS_ROOT, '../')

from photohash.photohash import average_hash, distance, is_look_alike, _hamming_distance


class PhotoHashTestCase(unittest.TestCase):
    def setUp(self):
        self.photos = [
            {
                'path': join(ASSETS_ROOT, 'minneapolis.jpg'),
                'average_hash': 'ffffffffc7000000',
            },
            {
                'path': join(ASSETS_ROOT, 'santa_monica.jpg'),
                'average_hash': '01ffffff1f3f0008',
            },
            {
                'path': join(ASSETS_ROOT, 'snow.jpg'),
                'average_hash': '67047df9fcf0408f',
            },
            {
                'path': join(ASSETS_ROOT, 'santa_monica_small.jpg'),
                'average_hash': '01ffffff1f3f0008',
            },

        ]

    def test_average_hash(self):
        """average_hash should output the expected hash for each test image"""
        for photo in self.photos:
            self.assertEqual(photo['average_hash'], average_hash(photo['path']))

    def test_hamming_distance(self):
        """_hamming_distance should know the distance between two strings"""
        self.assertEqual(_hamming_distance('roses', 'toned'), 3)
        self.assertEqual(_hamming_distance('are', 'are'), 0)
        self.assertEqual(_hamming_distance('read', 'daer'), 4)

    def test_distance(self):
        """distance should know the distance between the average_hash of two test images"""
        for i in range(len(self.photos)):
            for j in range(i, len(self.photos)):
                hamming_distance = _hamming_distance(
                    self.photos[i]['average_hash'],
                    self.photos[j]['average_hash']
                )

                self.assertEqual(
                    hamming_distance,
                    distance(self.photos[i]['path'], self.photos[j]['path'])
                )

    def test_is_look_alike(self):
        """is_look_alike should know if two images look similar"""

        # Test that the same image will return True.
        self.assertTrue(is_look_alike(self.photos[2]['path'], self.photos[2]['path']))

        # And if we use the most strict tolerance.
        self.assertTrue(is_look_alike(self.photos[2]['path'], self.photos[2]['path'], tolerance=0))

        # And if we use the least strict tolerance.
        self.assertTrue(
            is_look_alike(self.photos[2]['path'], self.photos[2]['path'], tolerance=16)
        )

        # Test that different images return False
        self.assertFalse(is_look_alike(self.photos[0]['path'], self.photos[1]['path']))

        # Test that a scaled verision of the same image is within default tolerance.
        self.assertTrue(is_look_alike(self.photos[1]['path'], self.photos[3]['path']))
