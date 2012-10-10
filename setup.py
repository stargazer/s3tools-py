from setuptools import setup, find_packages

setup(
    name='s3tools-py',
    version='0.1',
    author='C. Paschalides',
    author_email='already.late@gmail.com',
    url='http://github.com/stargazer/s3tools-py',
    packages=find_packages(),
    install_requires=(
        'boto',
    ),
)  


