"""
Image hashing library
======================

Example:

>>> import Image
>>> import ImageHash
>>> hash = ImageHash.average_hash(Image.open('test.png'))
>>> print hash
d879f8f89b1bbf
>>> otherhash = ImageHash.average_hash(Image.open('other.bmp'))
>>> print otherhash
ffff3720200ffff
>>> print hash == otherhash
False
>>> print hash - otherhash
36
>>> for r in range(1, 30, 5):
...     rothash = ImageHash.average_hash(Image.open('test.png').rotate(r))
...     print 'Rotation by %d: %d Hamming difference' % (r, hash - rothash)
... 
Rotation by 1: 2 Hamming difference
Rotation by 6: 11 Hamming difference
Rotation by 11: 13 Hamming difference
Rotation by 16: 17 Hamming difference
Rotation by 21: 19 Hamming difference
Rotation by 26: 21 Hamming difference
>>>
>>> # another example is find_similar_images, see find_similar_images??

"""

import Image
import numpy
import scipy.fftpack

def binary_array_to_hex(arr):
	h = 0
	s = []
	for i,v in enumerate(arr.flatten()):
		if v: h += 2**(i % 8)
		if (i % 8) == 7:
			s.append(hex(h)[2:])
			h = 0
	return "".join(s)
	return hex(numpy.sum([2**i for i,v in enumerate(arr.flatten()) if v]))

def binary_array_to_int(arr):
	return sum([2**(i % 8) for i,v in enumerate(arr.flatten()) if v])

"""
Hash encapsulation. Can be used for dictionary keys and comparisons.
"""
class ImageHash(object):
	def __init__(self, binary_array):
		self.hash = binary_array

	def __str__(self):
		return binary_array_to_hex(self.hash)

	def __repr__(self):
		return repr(self.hash)

	def __sub__(self, other):
		return (self.hash != other.hash).sum()

	def __eq__(self, other):
		return numpy.array_equal(self.hash, other.hash)

	def __ne__(self, other):
		return not numpy.array_equal(self.hash, other.hash)

	def __hash__(self):
		return binary_array_to_int(self.hash)
    

"""
Average Hash computation

Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

@image must be a PIL instance.
"""
def average_hash(image, hash_size=8):
	image = image.convert("L").resize((hash_size, hash_size), Image.ANTIALIAS)
	pixels = numpy.array(image.getdata()).reshape((hash_size, hash_size))
	avg = pixels.mean()
	diff = pixels > avg
	# make a hash
	return ImageHash(diff)

"""
Perceptual Hash computation.

Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

@image must be a PIL instance.
"""
def phash(image, hash_size=32):
	image = image.convert("L").resize((hash_size, hash_size), Image.ANTIALIAS)
	pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((hash_size, hash_size))
	dct = scipy.fftpack.dct(pixels)
	dctlowfreq = dct[:8, 1:9]
	avg = dctlowfreq.mean()
	diff = dctlowfreq > avg
	return ImageHash(diff)

"""
Difference Hash computation.

following http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html

@image must be a PIL instance.
"""
def dhash(image, hash_size=8):
	image = image.convert("L").resize((hash_size + 1, hash_size), Image.ANTIALIAS)
	pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((hash_size + 1, hash_size))
	# compute differences
	diff = pixels[1:,:] > pixels[:-1,:]
	return ImageHash(diff)



__dir__ = [average_hash, phash, ImageHash]

"""
Demo of hashing
"""
def find_similar_images(userpath, hashfunc = average_hash):
	import os
	def is_image(filename):
		f = filename.lower()
		return f.endswith(".png") or f.endswith(".jpg") or \
			f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif")
	
	image_filenames = [os.path.join(userpath, path) for path in os.listdir(userpath) if is_image(path)]
	images = {}
	for img in sorted(image_filenames):
		hash = hashfunc(Image.open(img))
		images[hash] = images.get(hash, []) + [img]
	
	for k, img_list in images.iteritems():
		if len(img_list) > 1:
			print " ".join(img_list)


if __name__ == '__main__':
	import sys, os
	def usage():
		sys.stderr.write("""SYNOPSIS: %s [avg|phash] [<directory>]

Identifies similar images in the directory.

(C) Johannes Buchner, 2013
""" % sys.argv[0])
		sys.exit(1)
	
	hashmethod = sys.argv[1] if len(sys.argv) > 1 else usage()
	if hashmethod == 'ahash':
		hashfunc = average_hash
	elif hashmethod == 'phash':
		hashfunc = phash
	elif hashmethod == 'dhash':
		hashfunc = dhash
	else:
		usage()
	userpath = sys.argv[2] if len(sys.argv) > 2 else "."
	find_similar_images(userpath=userpath, hashfunc=hashfunc)
	

