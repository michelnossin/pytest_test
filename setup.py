import sys
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

test_dependencies = [
    'pytest==3.8.2',
    'pytest-cov==2.5.1',
]

setup_dependencies = []
if {'test'}.intersection(sys.argv):
    setup_dependencies = ['pytest-runner==4.2']

setup(
    name="ptest_test",
    version="0.0.1",
    description="pytest michel",
    author="michel",
    long_description=long_description,
    author_email="michel.nossin@gmail.com",
    packages=["tdd_checkout_example"],
    install_requires=[],
    setup_requires=setup_dependencies,
    extras_require={
        'test': test_dependencies,
        'lint': ['flake8==3.5.0']
    },
    tests_require=test_dependencies
)
