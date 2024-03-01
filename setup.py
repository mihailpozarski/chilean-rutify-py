from setuptools import find_packages, setup

setup(
    name='chileanrutify',
    packages=find_packages(include=['chileanrutify']),
    version='0.1.0',
    description='Chilean rut Python package - Chilean Rut/Run validator and formatter library',
    author='mihailpozarski',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)