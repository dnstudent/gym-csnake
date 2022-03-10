from setuptools import setup
from Cython.Build import cythonize

setup(
    name='gym-csnake',
    version='0.0.1',
    packages=['gym_csnake', 'gym_csnake.envs'],
    package_dir={'': 'src'},
    url='https://github.com/dnstudent/gym-csnake',
    license='AFL',
    author='davidenicoli',
    author_email='davide.nicoli1@studenti.unimi.it',
    description='Snake implemented in Cython',
    install_requires=['gym']
)
