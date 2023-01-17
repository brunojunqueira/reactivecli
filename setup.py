import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='reactivecli',
    version='0.1',
    author="Bruno Junuqeira",
    author_email="brunosdsj@gmail.com",
    description="A CLI framework library to build responsive console interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brunojunqueira/ReactiveCLI",
    packages=setuptools.find_packages(
        exclude=["__tests__"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7.1",
    install_requires=[
        "sshkeyboard"
    ]

)
