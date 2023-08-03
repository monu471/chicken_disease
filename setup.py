import setuptools
with open("README.md", encoding="Utf-8") as f:
    long_description = f.read()


__version__ ="0.0.0"
repo_name = "chicken_disease"
author = "Monu Joshi"
src_repo  = "cnnClassifier"
author_email = "monujoshi471@gmail.com"


setuptools.setup(
    name= src_repo,
    version=__version__,
    author= author,
    author_email= author_email,
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where ="src")
)