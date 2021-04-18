import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pear_todo_cli",
    version="0.2",
    scripts=["todo_cli"] ,
    author="Gerrit Proessl",
    author_email="grproessl@web.de",
    description="A cli todo list",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/g3rrit/todo_cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
)
