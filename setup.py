""" Sphinx extension to build json files with an additional metadata
as structured JSON objects as well as a `toctree` key containing a 
full toctree (similar to RTD html theme).
"""

from setuptools import setup, find_packages

VERSION = '0.01'
DOCLINES = (__doc__ or '').split("\n")

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    'Topic :: Documentation :: Sphinx',
]

def run_setup():
    setup(
        name='sphinxcontrib-metajson',
        version=VERSION,
        description=DOCLINES[0],
        long_description="\n".join(DOCLINES[2:]),
        classifiers=CLASSIFIERS,
        author='George Reynolds',
        author_email='george.reynolds@cybereason.com',
        license='apache',
        url='https://github.com/cr-GeorgeReynolds1/sphinx-metajson-builder.git',
        download_url = 'https://github.com/cr-GeorgeReynolds1/sphinx-metajson-builder.git/releases',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=['Sphinx>=1.0'],
        namespace_packages=['sphinxcontrib'],
    )

run_setup()
