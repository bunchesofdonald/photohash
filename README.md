This was mainly created just for my own use and education. It's a perceptual hash algorithm, used to find if two images are similar.

At the present time it only supports an Average Hash. Usage:

from ImageHash import ImageHash
hash = ImageHash('myimage.jpg').average_hash()

## TODO:
- Add hamming distance calculator and helper method to directly compare images.
- Add more hash algorithms.
