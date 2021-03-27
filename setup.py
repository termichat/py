import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytermichat",
    version="1.0.0",
    author="Mineinjava",
    author_email="mineinjava@minein.me",
    description="Python powered chat in terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/termichat/py",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
        "Source": "https://github.com/termichat/py"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        # "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)
