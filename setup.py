import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# TODO author_email, README, classifiers
setuptools.setup(
        name="cipy",
        version="0.0.1",
        author="fairu1024, whzup",
        author_email="",
        description="A cipher package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/fire-ferrets/cipy",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: something :: something",
            "Operating System :: OS Independent",
        ],
        setup_requires=["pytest-runner"],
        tests_require=["pytest"],
)
