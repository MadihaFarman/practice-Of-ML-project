## This file helps create entire ML project as a package that can be imported and deployed.

from setuptools import find_packages,setup     # automatically finds out all the packages used in entire ml project
from typing import List

HYPHEN_E_DOT='-e .'    # This is written in requirements.txt to automatically trigger the setup.py file
def get_requirements(file_path:str)->List[str]:     # [file_path:str # it gives hint related
                                                    #  to the datatype of the parameter file_path . This doesn’t force Python to  only accept strings, it just suggests to other developers (and tools like linters/IDEs) what type is expected.]
                                                    # ->List[str] : -> : return type hint , List[str] : The function will return string type
    """
    This function will return the list of requirements

    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]  #replace the newline character with an empty string

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='Practice-ML-Project',
    version='0.0.1',
    author='Madiha Farman',
    author_email='madihashah834@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)
