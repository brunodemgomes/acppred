from setuptools import setup, find_packages

setup(
    name='acppred',
    version='0.0.1',
    packages=find_packages(),
    author='Bruno Gomes',
    entry_points = {
        'console_scripts': [
            'acppred_train = acppred.train:main',
            'acppred_predict = acppred.predict:main'
        ]
    }
)
