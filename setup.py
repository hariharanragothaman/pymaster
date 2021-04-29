from setuptools import setup, find_packages

setup(
    name="pymaster",
    packages=find_packages(exclude=["tests", "docs"]),
    version="1.0.0",
    description="Quick Recipes for interview problems",
    author="Hariharan Ragothaman",
    classifiers=[
        "Topic:: Utilities",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
    ],
)
