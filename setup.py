
from setuptools import setup, find_packages

setup(
    name='databridge',
    version='0.1',
    description='A versatile data library for cloud and analytics',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'boto3',
        'requests'
    ],
)
    