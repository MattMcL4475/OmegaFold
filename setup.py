from setuptools import setup, find_packages
import sys

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="OmegaFold",
    description="OmegaFold Release Code",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    packages=find_packages(exclude=["tests", "tests.*"]),
    entry_points={"console_scripts": ["omegafold=omegafold.__main__:main",],},
    install_requires=[
        "biopython",
        "torch==2.4.0"
    ],
    python_requires=">=3.8",
)
