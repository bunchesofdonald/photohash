from PIL import Image
from bitarray import bitarray


def _hamming_distance(string, other_string):
    return sum(map(lambda x: 0 if x[0] == x[1] else 1, zip(string, other_string)))


class ImageHash(object):
    def __init__(self, path, size=8):
        self.image_path = path
        self.hash_size = size
        self.image = Image.open(path)

    def average_hash(self):
        image = self.image.resize((self.hash_size, self.hash_size), Image.ANTIALIAS).convert("1")
        pixels = list(image.getdata())
        avg = sum(pixels) / len(pixels)

        diff = []
        for pixel in pixels:
            value = 1 if pixel > avg else 0
            diff.append(str(value))

        ba = bitarray("".join(diff), endian='little')
        return ba.tobytes().encode('hex')


def distance(image_path, other_image_path):
    image_hash = ImageHash(image_path).average_hash()
    other_image_hash = ImageHash(other_image_path).average_hash()

    return _hamming_distance(image_hash, other_image_hash)


def is_look_alike(image_path, other_image_path, tolerance=6):
    return distance(image_path, other_image_path) < tolerance
