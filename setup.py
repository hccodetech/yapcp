import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name = "YAPCP",
    version="0.0.0.5",
    author="hccodetech",
    url = "https://github.com/hccodetech/yapcp",
    download_url = "https://github.com/hccodetech/yapcp",
    install_requires = [ 'aospdtgen', 'backports.lzma', 'extract-dtb', 'protobuf', 'pycryptodome', 'docopt', 'zstandard' ],
    packages = [ 'yapcp' ],
    classifiers = [
        "Programming Language :: Python :: 3"
    ],
    long_description = (this_directory / "README.md").read_text(),
    long_description_content_type='text/markdown'
)
