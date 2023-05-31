from setuptools import find_packages,setup
from typin import List

def get_requirements(file_path:str)->List[str]:

setup(
    name='mlproject',
    version='0.0.1',
    author='Mirul Patel',
    author_email='mirulpatel1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)