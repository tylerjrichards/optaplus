from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md")

setup(name='optaplus',
      version='1.0',
      description='Optaplus package is a range of functions to act as helping hands for people working with Opta and Tracab data.',
      author='Joe Mulberry, Tyler Richards',
      author_email='tylerjrichards@gmail.com',
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://github.com/tylerjrichards/optaplus",
      license='MIT',
      packages=['optaplus'],
      install_requires=[
          'elementpath',
          'pandas',
          'numpy',
      ],
      zip_safe=False)
