from setuptools import setup, find_packages

setup(
    name='gambit',
    version="0.1.5",
    description='A micro library for performing multi queries in elasticsearch',
    keywords='elasticsearch elastic',
    author='Avichal Pandey',
    author_email='pandeyavichal7@gmail.com',
    license='MIT License',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True
)
