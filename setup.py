import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cm-rgb",
    version = "0.3.3",
    author = "gfduszynski",
    author_email = "gfduszynski@gmail.com",
    description = ("Utility to control RGB on AMD Wraith Prism"),
    license = "MIT",
    keywords = "rgb hid wraith",
    url = "http://github.com/gfduszynski/cm-rgb",
    packages=['cm_rgb'],
    scripts=['scripts/cm-rgb-cli','scripts/cm-rgb-monitor'],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
          'hidapi',
          'click' ,
          'psutil',
          'PyGObject'
    ],
)