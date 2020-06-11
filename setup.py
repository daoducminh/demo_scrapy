from setuptools import setup, find_packages

setup(
    name='it4853_nhom1',
    version='1.0',
    description='Web Crawler for Search Engine',
    author='minhdao',
    packages=find_packages(exclude=[
        'docs',
        'tests',
        'static',
        'temp',
        '.gitignore',
        'README.md',
        '.vscode',
        '.virtualenvs'
    ]),
    install_requires=[
        'scrapy',
        'scrapy-splash',
        'pymongo',
        'elasticsearch',
        'elasticsearch-dsl',
        'python-dotenv',
        'pylint',
        'autopep8'
    ],
)
