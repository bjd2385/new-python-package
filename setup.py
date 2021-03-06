# For reference ~ https://github.com/pypa/sampleproject/blob/main/setup.py

import pathlib

from setuptools import setup, find_packages


here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='newpythonpackage',
    version='0.1.0',
    description='An example package.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Brandon Doyle',
    author_email='bjd2385.linux@gmail.com',
    keywords='',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.10, <4',
    url = 'https://github.com/bjd2385/new-package-package',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'cli=new-python-package:package.main',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/bjd2385/wildmatch/issues',
        'Source': 'https://github.com/bjd2385/wildmatch'
    },
    include_package_data=True
)
