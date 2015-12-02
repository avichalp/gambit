import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

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
    zip_safe=True,
    tests_require=['tox'],
    cmdclass = {'test': Tox},
)
