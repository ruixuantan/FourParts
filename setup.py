import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="fourparts",
    version="0.0.1",
    author="rxtan",
    description="A package related to all things 4 parts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ruixuantan/fourparts",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'py-midicsv',
        'MIDIUtil'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.0'
)
