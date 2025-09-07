# setup.py

from setuptools import setup, find_packages

setup(
    name="recon",
    version="0.1.0",
    description="CLI tool to convert between JSON, YAML, XML, and Markdown",
    author="Thomas Croucher",
    packages=find_packages(),  # includes the 'recon' package
    include_package_data=True,
    install_requires=[
        "PyYAML>=6.0",      # YAML parsing/emitting
        "xmltodict>=0.15.0",# XML to dict conversion
        "Markdown>=3.0"     # Markdown parsing
    ],
    entry_points={
        'console_scripts': [
            'recon=recon.cli:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
