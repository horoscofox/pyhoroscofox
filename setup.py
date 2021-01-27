from setuptools import setup, find_packages


setup(
    name='horoscofox',
    version='1.1.1',
    url='https://github.com/horoscofox/pyhoroscofox',
    license='MIT',
    author='Owanesh',
    description='',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=[
        "requests>=2.22.0"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
