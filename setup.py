from distutils.core import setup
import setuptools


setup(
    name='phpdoc',
    version='1.0',
    install_requires=[
        'requests',
        'bs4'
    ],
    packages=[
        'phpdoc'
    ],
    entry_points={
        "console_scripts": [
            "phpdoc = phpdoc.bin:run"
        ]
    }
)
