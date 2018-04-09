from setuptools import setup, find_packages

def get_requirements():
    with open('requirements.txt') as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


install_requires = get_requirements()

setup(
    name='blueprint',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
)