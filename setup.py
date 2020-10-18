import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ezz_mizan", # Replace with your own username
    version="0.0.2",
    author="Mohamed Omar",
    author_email="omar@mohamedomar.me",
    description="Ezz Mizan is an arabic alphabet count based on an alphabet numbering reference ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohomar84/ezz_mizan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)