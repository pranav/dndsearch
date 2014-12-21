from setuptools import setup, find_packages

setup(
    name='dndsearch',
    version='1.0',
    description='Search the DnD Books for something',
    author='Pranav Gandhi',
    author_email='me@pranav.io',
    packages=find_packages(),
    install_requires=[
        'pyPdf',
        'sqlalchemy',
        'MySQL-python',
        'Flask'
    ]
)
