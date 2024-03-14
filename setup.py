from setuptools import find_packages, setup
from typing import List

HYPEHN_E_DOT='-e .'

def get_requirements(file_path:str) ->List[str]:
    '''
    This function will return a list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEHN_E_DOT in requirements:
            requirements.remove(HYPEHN_E_DOT)


setup( # sort of like metadata
    name='mlproject',
    version='0.01',
    author='chee-zy',
    author_email='alex.cheezy97@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas', 'numpy', 'seaborn'] # will do the installation automatically
    install_requires=get_requirements('requirement.txt')
)