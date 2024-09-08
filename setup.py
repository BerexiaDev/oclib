from setuptools import setup, find_packages

setup(
    name='oc_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask-SQLAlchemy==2.3.2',
        'SQLAlchemy==1.3.18'
    ],
    author='Yassine Bouhm',
    author_email='yassinebouhm@gmail.com',
    description='OC Global Library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
