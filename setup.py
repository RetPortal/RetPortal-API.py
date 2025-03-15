from setuptools import setup, find_packages

setup(
    name="RetPortal API",
    version="1.0.0",
    author="夜桜れと",
    packages=find_packages(),
    install_requires=["requests"],
    include_package_data=True,
)
