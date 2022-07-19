import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylibrm",
    version="0.0.1",
    author="Alan Huang",
    author_email="alanhuang@rmaxis.com",
    description="Python lib for RobustMotion axis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        'pymodbus==2.5.3'
    ],
)