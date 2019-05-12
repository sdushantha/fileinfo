import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name='file-info',
  version='1.2',
  author='Siddharth Dushantha',
  author_email='siddharth.dushantha@gmail.com',
  description='Get information on over 10,000 file extensions right from the terminal',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='http://https://github.com/sdushantha/fileinfo',
  packages=setuptools.find_packages(),
  scripts=['fileinfo/fileinfo'],
  install_requires=['requests']
)

