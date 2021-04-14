from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
