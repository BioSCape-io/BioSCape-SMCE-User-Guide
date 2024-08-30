from setuptools import setup, find_packages
from os import path

this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, "README.md")) as f:
    long_description = f.read()

__version__ = "0.0.4"
for line in open(path.join("bioscape-smce-user-guide", "__init__.py")):
    if line.startswith("__version__"):
        exec(line.strip())

setup(
    name="shift-smce-user-guide",
    version=__version__,
    description="shift-smce-user-guide",
    url="https://github.com/BioSCape-io/BioSCape-SMCE-User-Guide",
    author="Evan Lang",
    author_email="evan.d.lang@nasa.gov",
    classifiers=[
        "License :: OSI Approved :: Apache-2.0",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
    ],
    packages=find_packages(),
    install_requires=[],
    entry_points={},
    zip_safe=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
