#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='cric_score',
    version='0.1.0',
    description='Live Cricket Scores in Command Line.',
    author='Sourav Verma',
    license='MIT',
    keywords="Cricket score cricbuzz scores cli",
    author_email='souravverma095@gmail.com',
    url='https://github.com/sourav0007/cric_score',
    packages=find_packages(),
    include_package_data = True,
    install_requires=[
        "beautifulsoup4",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'cric_score = cric_score.main:main'
        ],
    }
)
