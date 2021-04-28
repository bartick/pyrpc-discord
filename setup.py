import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pyrpc-discord",
    version="1.1.2",
    python_requires='>=3.5',
    description="A Small Project To Automate Discord Rich Presence using CLI",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bartick/pyrpc-discord",
    author="Bartick Maiti",
    platforms=['Windows', 'Linux', 'OSX'],
    author_email="blackmumba890@gmail.com",
    license="MIT",
    classifiers=[
    	"Framework :: AsyncIO",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["pyrpc"],
    include_package_data=True,
    install_requires=[
    	"pypresence>=4.2.0"
    ],
    entry_points={
        "console_scripts": [
            "pyrpc=pyrpc.__main__:main",
        ]
    },
)