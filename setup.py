from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python :: 3'
]

setup(
    name='python_redex',
    version='1.0.1',
    description='User friendly version of regex.',
    long_description='More information available at https://github.com/TimoKats/redex',
    url='',  
    author='Timo Kats',
    author_email='tpakats@gmail.com',
    license='MIT', 
    classifiers=classifiers,
    keywords='regex', 
    packages=['redex'],
    install_requires=[''] 
)