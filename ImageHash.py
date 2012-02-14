import Image
from bitarray import bitarray

class ImageHash(object):
    def __init__(self, path, size=8):
        self.image_path = path
        self.hash_size = size
        self.image = Image.open(path)

    def average_hash(self):
        image = self.image.resize((self.hash_size, self.hash_size), Image.ANTIALIAS).convert("L")
        pixels = list(image.getdata())
        avg = sum(pixels) / len(pixels)

        diff = []
        for pixel in pixels:
            value = 1 if pixel > avg else 0
            diff.append(str(value))

        ba = bitarray("".join(diff), endian='little')
        return ba.tobytes().encode('hex')
