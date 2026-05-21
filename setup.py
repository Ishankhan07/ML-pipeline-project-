from setuptools import find_packages,setup
from typing import List

hyp_e_dot = "-e ."
def get_requirements(file_path:str)->list[str]:
    "this func return list of requirements "
    requirements =[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requiremnts=[req.replace("\n","") for req in requirements]
        if hyp_e_dot in requirements:
            requirements.remove(hyp_e_dot)
    return requirements


setup(
name = "mlproject",
version="0.0.1",
author = " ISHAN ",
author_email="mohdisaankhan07@gmail.com",
package = find_packages(),
install_requires=get_requirements("requirements.txt")

)
