from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='quickrsa',
    version='0.0.3',
    description='A concise implementation of a textbook version RSA.',
    url='https://github.com/ericlearning/Quick-RSA',
    author='ericlearning',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)