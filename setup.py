import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pretty",
    version="0.0.1",
    author="David Levy Sousa Oliveira",
    author_email="sdavidlevy@gmail.com",
    description="Open source project that aims to create a theme for the admin that is simple and nice.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DavidLSO/pretty",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
