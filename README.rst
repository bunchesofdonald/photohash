=========
PhotoHash
=========

.. image:: https://travis-ci.org/bunchesofdonald/django-hermes.svg?branch=master
    :target: https://travis-ci.org/bunchesofdonald/photohash

This was mainly created just for my own use and education. It's a perceptual
hash algorithm, used to find if two images are similar.

Installation
============

::

    pip install PhotoHash


Usage
=====

average_hash
------------
Returns the hash of the image using an average hash algorithm. This algorithm
compares each pixel in the image to the average value of all the pixels.::

    import photohash
    hash = photohash.average_hash('/path/to/myimage.jpg')

distance
--------
Returns the hamming distance between the average_hash of the given images.::

    import photohash
    distance = photohash.distance('/path/to/myimage.jpg', '/path/to/myotherimage.jpg')

is_look_alike
-------------
Returns a boolean of whether or not the photos look similar.::

    import photohash
    similar = photohash.is_look_alike('/path/to/myimage.jpg', '/path/to/myotherimage.jpg')

is_look_alike also takes an optional tolerance argument that defines how strict
the comparison should be.::

    import photohash
    similar = photohash.is_look_alike('/path/to/myimage.jpg', '/path/to/myimage.jpg', tolerance=3)

hash_distance
-------------
Returns the hamming distance between two hashes of the same length::

    import photohash
    hash_one = average_hash('/path/to/myimage.jpg')
    hash_two = average_hash('/path/to/myotherimage.jpg')
    distance = photohash.hash_distance(hash_one, hash_two)

hashes_are_similar
------------------
Returns a boolean of whether or not the two hashes are within the given tolerance. Same as
is_look_alike, but takes hashes instead of image paths::

    import photohash
    hash_one = average_hash('/path/to/myimage.jpg')
    hash_two = average_hash('/path/to/myotherimage.jpg')
    similar = photohash.hash_are_similar(hash_one, hash_two)

hashes_are_similar also takes the same optional tolerance argument that is_look_alike does.
