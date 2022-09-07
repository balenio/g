from setuptools import setup

setup(
    name="g",
    version="0.0.0",
    description="An informal AWK-like thing for python",
    author="balenio",
    author_email="pypi@ruf.mozmail.com",
    url="https://github.com/balenio/g",
    py_modules=["g"],
    entry_points={
        "console_scripts": [
            "g=g:main",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    ]
)