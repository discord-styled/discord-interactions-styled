from codecs import open
from setuptools import find_packages, setup

with open("README.md", "r", encoding="UTF-8") as f:
    README = f.read()

setup(
    name="discord-interactions-styled",
    version="0.4.1",
    author="gammx",
    author_email="gammxplus@gmail.com",
    description="A simple set of tools to write easier code using discord-py-interactions",
    install_requires=["discord.py", "discord-py-slash-command"],
    license="MIT License",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/discord-styled/discord-interactions-styled",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)