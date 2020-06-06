# Say Hello

This is an example project demonstrating how to publish a   # ( a small paragraph describing what the project does )
python module to PyPI

## Installation

run the following to install

'''python
pip install sayhello
'''

## Usage

'''python
from hello import say_hello

# Generate "hello, World"
say_hello

# Generate "Hello, Everybody!"
say_hello("Everybody")
'''

# Developing Say World

to install sayhello, along with the tools you 
need to develop and run tests, run the following
in your virtualenv

'''python
pip install -e .[dev]