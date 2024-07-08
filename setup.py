from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of requirements from the specified file_path.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT.strip() in requirements:
            requirements.remove(HYPHEN_E_DOT.strip())

    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='vinayak',
    author_email='vinayak99anadinni@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
