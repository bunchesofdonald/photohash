from PIL import Image
from bitarray import bitarray


def _hamming_distance(string, other_string):
    """ Computes the hamming distance between two strings. """
    return sum(map(lambda x: 0 if x[0] == x[1] else 1, zip(string, other_string)))


def average_hash(image_path, hash_size=8):
    """ Computes the average hash of the given image. """

    # Open the image, resize it and convert it to black & white.
    image = Image.open(image_path)
    image = image.resize((hash_size, hash_size), Image.ANTIALIAS).convert("1")

    # Get the average value of a pixel in the image.
    pixels = list(image.getdata())
    avg = sum(pixels) / len(pixels)

    # Compute the hash based on each pixels value compared to the average.
    diff = map(lambda pixel: '1' if pixel > avg else '0', pixels)
    bits = bitarray("".join(diff), endian='little')

    return bits.tobytes().encode('hex')


def distance(image_path, other_image_path):
    """ Computes the hamming distance between two images. """
    image_hash = average_hash(image_path)
    other_image_hash = average_hash(other_image_path)

    return _hamming_distance(image_hash, other_image_hash)


def is_look_alike(image_path, other_image_path, tolerance=6):
    """
    Returns True if the hamming distance between
    the image hashes are less than the given tolerance.
    """

    return distance(image_path, other_image_path) < tolerance
