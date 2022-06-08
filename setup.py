#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(META)>:
DOCid: <(UUID)>
name: <[document_name]>
description: >
version: <[version]>
path: <[LEXIvrs]><[path]>.yaml
outline: <[outline]>
authority: <[authority]>
security: <[seclvl]>
<(WT)>: -32
'''
#-*- coding: utf-8 -*
#=======================================================================||
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from os.path import abspath, dirname, join
import codecs, io, os, re, sys
#=======================================================================||
here = abspath(dirname(__file__))
version_file = open(join(here, 'qt5pandas', '__init__.py'), 'r')
__version__ = re.sub(r".*\b__version__\s+=\s+'([^']+)'.*", r'\1',
	[line.strip() for line in version_file if '__version__' in line].pop(0))
version_file.close()
short_description = """Utilities to use pandas (the data analysis / manipulation
library for Python) with Qt."""
try:
	long_description = read('README.md')
except IOError:
	long_description = "See README.md where installed."
#=======================================================================||
def read(*filenames, **kwargs):
	encoding = kwargs.get('encoding', 'utf-8')
	sep, buf = kwargs.get('sep', '\n'), []
	for filename in filenames:
		with io.open(filename, encoding=encoding) as f:
			buf.append(f.read())
	return sep.join(buf)
class PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True
	def run_tests(self):
		import pytest
		errcode = pytest.main(self.test_args)
		sys.exit(errcode)
tests_require = ["pandas >= 0.17.1", 'easygui', 'pyqt', 'pytest', 'pytest-qt', 'pytest-cov', 'future',]
setup(name='qt5pandas',
	version=__version__,
	url='https://github.com/solutionsbrewer/qt5pandas',
	license='MIT License',
	namespace_packages=['qt5pandas'],
	author='Matthias Ludwig,Marcel Radischat,Zeke Barge,James Draper','Solubrew'
	tests_require=tests_require,
	install_requires=["pandas >= 0.17.1", 'easygui', 'pytest', 'pytest-qt>=1.2.2',
					  'qtpy', 'future', 'pytest-cov',],
	cmdclass={'test': PyTest},
	author_email='qt5pandas@solutionsbrewer.com',
	description=short_description,
	long_description=long_description,
	include_package_data=True,
	packages=['qt5pandas'],
	platforms='any',
	test_suite='tests',
	classifiers=['Programming Language :: Python',
		'Development Status :: 4 - Beta',
		'Natural Language :: English',
		'Environment :: X11 Applications :: Qt',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Software Development :: User Interfaces'],
	extras_require={'testing': tests_require,})
