from setuptools import setup

setup(
    name='Freshsales',
    url='https://github.com/jladan/package_demo',
    author='Bhagirath Goud',
    author_email='bhagirath@freshdesk.com',
    # Needed to actually package something
    packages=['measure'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='1.0.0',
    # The license can be anything you like
    license='MIT',
    description='Freshsales python package',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)