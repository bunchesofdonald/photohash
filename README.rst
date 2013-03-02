ImageHash
===========

A image hashing library written in Python.
Supports:

* average hashing (aHash)
* perception hashing (pHash)
* difference hashing (dHash)

Requirements
-------------
Based on PIL Image, numpy and scipy.fftpack (for pHash)

Basic usage
------------
::

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


Demo script find_similar_images illustrates how to find similar images in a directory.

References::

  * pHash implementation following http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html
  * dHash implementation following http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html


