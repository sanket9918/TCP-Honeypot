from setuptools import setup


def read_file():
    with open("README.rst") as readme_file:
        data = readme_file.read()
    return data


setup(
    name="Sanpot",
    version="1.0",
    description="TCP Honeypot",
    long_description=read_file(),
    author="Sanket Mohapatra",
    author_email="sanketmohapatra13@gmail.com",
    license="MIT",
    packages=['sanpot'],
    zip_safe=False,
    install_requires=[
        'docopt'
    ]

)
