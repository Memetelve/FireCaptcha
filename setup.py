from setuptools import setup
from os.path import abspath, dirname, join

# Fetches the content from README.md
# This will be used for the "long_description" field.
README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

setup(
    name="FireCaptcha",
    version="0.0.3.0",
    packages=["FireCaptcha"],
    description="Highly customizable captcha generator, written in python",
    long_description=README_MD,
    url="https://github.com/Memetelve/FireCaptcha",
    author="Memetelve",
    author_email="maciek@marszalkowski.pl",
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="captcha, security, image",
    requires=[
        "Pillow",
    ],
)
