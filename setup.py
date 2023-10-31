from setuptools import find_namespace_packages, setup

setup(
    name="personal_assistant",
    version="1",
    description="Program includes features: address book; notes; sorting files",
    url="https://github.com/the10or/personal_assistant",
    author="DRY_KISS.py team",
    author_email="the10or@gmail.com",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["colorama"],
    entry_points={"console_scripts": ["start-bot = src.main:main"]},
)
