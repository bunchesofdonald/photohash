from setuptools import setup, find_packages

setup(
    author='Chris Pickett',
    author_email='chris.pickett@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    description='A Python Perceptual Image Hashing Module',
    license='MIT',
    long_description=open('README.rst').read(),
    name='Photohash',
    packages=find_packages(),
    url='https://github.com/bunchesofdonald/photohash',
    version='0.3.2',
    install_requires=[
        'Pillow>=2.1.0',
    ],
)
