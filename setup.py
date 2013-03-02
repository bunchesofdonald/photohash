from distutils.core import setup

setup(
    name='ImageHash',
    version='0.1',
    author='Johannes Buchner',
    author_email='buchner.johannes@gmx.at',
    packages=['imagehash'],
    scripts=['find_similar_images.py'],
    url='http://pypi.python.org/pypi/imagehash/',
    license='LICENSE',
    description='Image Hashing library',
    long_description=open('README.rst').read(),
    install_requires=[
        "scipy",
        "numpy",
        "Image",
    ],
)

