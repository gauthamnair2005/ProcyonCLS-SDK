from setuptools import setup, find_packages

setup(
    name="ProcyonCLS-SDK",
    version="2.0.5",
    author="Gautham Nair",
    author_email="gautham.nair.2005@gmail.com",
    description="SDK for ProcyonCLS applications",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/gauthamnair2005/procyoncls-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
