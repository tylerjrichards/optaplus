from setuptools import setup

setup(name='soccer_package',
      version='0.1',
      description='A package for soccer functions',
      url='http://github.com/tylerjrichards',
      author='Tyler Richards',
      author_email='tylerjrichards@gmail.com',
      license='MIT',
      packages=['soccer_package'],
      install_requires=[
          'elementpath',
          'pandas',
          'numpy',
      ],
      zip_safe=False)