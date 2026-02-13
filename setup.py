from setuptools import find_packages, setup
from typing import List

def get_requirements() -> list[str]:     #output will be in the list(list of string)
    requirements_list : list[str] = []
    return requirements_list

setup(

name= "sensor",
version= "0.0.1",
author= "Sameen",
author_email="sameenkainaat1512@gmail.com",
packages= find_packages(),
install_requires = get_requirements(),  #["pymongo"]
)