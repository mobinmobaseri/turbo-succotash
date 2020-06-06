from setuptools import setup

with open("README.md", "r") as fh:
   long_description = fh.read()


setup(
    name='sayhello',  # this is what you command [ pip install name ]
    # and this name will appear on pypi,
    # it doesn't have to be the name that people import
    version='0.0.1',
    description='say hello',
    py_modules=["hello"],  # this is the list of pyhthon actual code,
    # and this is what peole import.
    package_dir={'': 'SRC'},  # this is telling the setuptools that our
    # code is under the SRC directory
    classifiers=[
        "Programming Language :: python :: 3"
        "Programming Language :: python :: 3.6"
        "Programming Language :: python :: 3.7"
        "Programming Language :: python :: 3.8"
        # the codes above mean that our programing language is python and it's working 
        # on python 3.6, 3.7, 3.8
        "License :: OSI Approved :: GNU General Public License v3.0 or later(GNU GPLv3 +)"
        # we talked about license before
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
    author="momoclub",
    author_email = "momoclub@yahoo.com",
)
