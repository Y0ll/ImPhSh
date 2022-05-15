from setuptools import setup, find_packages
 
setup(name="Image_Photo_Shop",
      version="0.0.1",
      license="MIT",
      author="Letavin Artem, Galkin Maxim",
      description="Contains various functions that help to process the image",
      packages=find_packages(exclude=["tests"]),
      long_description=open("README.md").read(),
      zip_safe=False)