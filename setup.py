import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    version = fh.read()

setuptools.setup(
    name="metalite",
    version=version,
    author="Alex Nodet",
    author_email="dev.alexn@gmail.com",
    description="Simple game meta layer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexnsfx/metalite",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
