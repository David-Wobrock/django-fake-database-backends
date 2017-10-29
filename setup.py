from codecs import open
from os import path
from setuptools import setup, find_packages


PROJECT_DIR = path.abspath(path.dirname(__file__))

with open(path.join(PROJECT_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-fake-database-backends',
    version='0.0.1',

    description='Fake django database backends to generate sql without real database',
    long_description=long_description,
    url='https://github.com/David-Wobrock/django-fake-database-backends',
    author='David Wobrock',
    author_email='david.wobrock@gmail.com',
    # license='',  # TODO

    packages=find_packages(exclude=['tests/']),

    keywords='django database backend',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        # TODO verify Python 3 compatible
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
    ]
)
