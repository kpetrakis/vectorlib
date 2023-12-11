from pathlib import Path
import setuptools

directory = Path(__file__).resolve().parent
with open(directory / 'README.md', 'r') as f:
  long_description = f.read()

setuptools.setup(
  name='vectorlib',
  version='0.1.0',
  description='A simple 3D Vector Library',
  author='kpetrakis',
  long_description=long_description,
  long_description_content_type='text/markdown',
  packages=setuptools.find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3'
  ],
  install_requires=['numpy>=1.23.4'],
  python_requires='>=3.10'
)