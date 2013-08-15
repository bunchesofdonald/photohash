# ImageHash

This was mainly created just for my own use and education. It's a perceptual
hash algorithm, used to find if two images are similar.

## Average Hash:

    import imagehash
    hash = imagehash.average_hash('/path/to/myimage.jpg')

## Hamming Distance

    import imagehash
    distance = imagehash.distance('/path/to/myimage.jpg', '/path/to/myotherimage.jpg')

## Similar:

    import imagehash
    similar = imagehash.is_look_alike('/path/to/myimage.jpg', '/path/to/myotherimage.jpg')

You can also set how string `is_look_alike` should be when comparing images by
passing in `tolerance`. If the tolerance is 0 `is_look_alike` will only return
True if the images are identical. The default tolerance is 6.

    import imagehash
    similar = imagehash.is_look_alike('/path/to/myimage.jpg', '/path/to/myimage.jpg', tolerance=3)


## TODO:
- Add more hash algorithms.
- Create package for pypi
