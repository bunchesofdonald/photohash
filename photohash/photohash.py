from PIL import Image


def _hamming_distance(string, other_string):
    """ Computes the hamming distance between two strings. """
    return sum(map(lambda x: 0 if x[0] == x[1] else 1, zip(string, other_string)))


def average_hash(image_path, hash_size=8):
    """ Computes the average hash of the given image. """
    with open(image_path, 'rb') as f:
        # Open the image, resize it and convert it to black & white.
        image = Image.open(f).resize((hash_size, hash_size), Image.ANTIALIAS).convert('L')
        pixels = list(image.getdata())

    avg = sum(pixels) / len(pixels)

    # Compute the hash based on each pixels value compared to the average.
    bits = "".join(map(lambda pixel: '1' if pixel > avg else '0', pixels))
    hashformat = "0{hashlength}x".format(hashlength=hash_size * 2)
    return int(bits, 2).__format__(hashformat)


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

    return distance(image_path, other_image_path) <= tolerance
