from setuptools import setup, find_packages

setup(
    name="Jamf-SDK",
    version="0.0.1",
    description="Jamf SDK",
    author="sebastian",
    author_email="seba@cloudnative.co.jp",
    packages=find_packages(),
    install_requires=[
        "requests",
        "xmltodict"
    ],
    entry_points={
        "console_scripts": [
        ]
    },
)
