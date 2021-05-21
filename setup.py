from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'yash',         
  packages = find_packages(),
  version = '0.0.1',
  license='MIT',
  description = 'Yet Another SHell emulator (YASH) written in python',
  author = 'Prateek Kesavarapu',
  author_email = 'kesavarapu.prateek@gmail.com',
  url = 'https://github.com/neodrags/yash',
  download_url = 'https://github.com/neodrags/yash/archive/v0.0.1-alpha.tar.gz',
  keywords = ['Shell'],
  install_requires=[
          'termcolor',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Terminal Emulators',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
