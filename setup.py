from setuptools import find_packages,setup
from typing import List

Hypen_e_dot="-e ."
def get_requriments(file_path:str)->List[str]:
    
    requirements=[]

    with open('requirements.txt') as file_obj:

        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements ]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

    return requirements


setup(
    name="MLOps_Projects",
    version='0.0.1',
    author="Niraj",
    author_email='nirajkerkar8@gmail.com',
    packages=find_packages(),
    install_requires=get_requriments('requirements.txt')

)