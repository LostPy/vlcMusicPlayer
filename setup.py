"""setup for vlcMusicPlayer package
Author: LostPy
Date: 2021/02/07
"""

from setuptools import setup, find_packages

import vlcMusicPlayer

__doc__ = """A small package to create a MusicPlayer with vlc."""


setup(
	name='vlcMusicPlayer',
	version='1.20210207',
	author='LostPy',
	description=__doc__,
	long_description=__doc__,
    package_dir = {'vlcMusicPlayer': './vlcMusicPlayer'},
    package_data = {'': ['LICENSE.txt']},
	include_package_data=True,
	url='https://github.com/LostPy/VLCMusicPlayer',
	classifiers=[
        "Programming Language :: Python",
        "Development Status :: Functionnal - improvement in progress",
        "License :: MIT",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5+",
        "Topic :: MusicPlayer :: vlc",
    ],
    license='MIT',
    packages = find_packages()
    )