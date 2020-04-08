from setuptools import setup
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(name='elasticsearch-service',
      version='0.15',
      description='easy access to elastic based on elasticsearch-dsl',
      url='http://github.com',
      author='The data handyman team',
      author_email='bertrand.chevrier@orange.com',
      license='MIT',
      classifiers=['Development Status :: 3 - Alpha'],
      long_description=long_description,
     # long_description_content_type="text/markdown",
      packages=['elasticsearch_service'],
      install_requires=[
          'elasticsearch','elasticsearch-dsl','pandas'
      ],
      include_package_data=True,
      zip_safe=False,
      python_requires='>=3.5')