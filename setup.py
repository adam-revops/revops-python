from setuptools import setup, find_namespace_packages

__version__ = None
with open('src/revops/__init__.py') as f:
    exec(f.read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="revops",
    version=__version__,
    author="RevOps",
    author_email="help@revops.io",
    keywords=["revops",],
    description="RevOps Python Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/revops-io/revops-python",
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src', exclude=['tests', 'tests.*']),
    install_requires=['requests'],
    install_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
