=========
PhotoHash
=========

This was mainly created just for my own use and education. It's a perceptual
hash algorithm, used to find if two images are similar.

average_hash
============
Returns the hash of the image using an average hash algorithm. This algorithm
compares each pixel in the image to the average value of all the pixels.::

    import photohash
    hash = photohash.average_hash('/path/to/myimage.jpg')

distance
========
Returns the hamming distance between the average_hash of the given images.::

    import photohash
    distance = photohash.distance('/path/to/myimage.jpg', '/path/to/myotherimage.jpg')

is_look_alike
=============
Returns a boolean of whether or not the photos look similar.::

    import photohash
    similar = photohash.is_look_alike('/path/to/myimage.jpg', '/path/to/myotherimage.jpg')

is_look_alike also takes an option tolerance argument that to define how strict
the comparison should be.::

    import photohash
    similar = photohash.is_look_alike('/path/to/myimage.jpg', '/path/to/myimage.jpg', tolerance=3)


TODO
====
* Add more hash algorithms.
