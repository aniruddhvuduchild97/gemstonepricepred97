from setuptools import find_packages,setup
x = '-e .'
def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace('\n','') for r in requirements]
        requirements = [r for r in requirements if r != x]
        return requirements
    

setup(name='gemstonepriceprediction',
      version='0.0.1',
      author='Andy Mike',
      author_email='aniruddhneptune@gmail.com',
      install_requires = get_requirements('requirements.txt'),
      packages=find_packages())


    