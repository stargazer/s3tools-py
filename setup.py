from setuptools import setup, find_packages

setup(
    name='s3tools-py',
    version='0.1',
    author='C. Paschalides',
    url='http://github.com/stargazer/s3tools-py',
    packages=find_packages(),
    namespace_packages=('s3tools',),
    install_requires=(
        'boto',
    ),
)  


