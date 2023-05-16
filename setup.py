from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """"
    this function will return a list of requirements
    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]            
    return requirements


setup(
    name="ml-project-end-to-end",
    version='0.0.1',
    author='Raga Jai Santhosh',
    author_email='raga.j.santhosh@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)