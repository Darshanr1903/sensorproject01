from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
    return requirements

setup(
    name='Fault detection',
    version='0.0.1',
    author='Darshan',
    author_email='darshanr974151@gmail.com',
    install_requires=get_requirements('requirements.txt'),  # ✅ Fixed key
    packages=find_packages()  # ✅ Added parentheses to call the function
)
