from setuptools import setup, find_packages

"""
setuptools documentation: https://pypi.org/project/setuptools/
"""

setup(
    name='logrun',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests'
    ],
    entry_points='''
    [console_scripts]
    logr=logruncli:logruncli
    '''
)