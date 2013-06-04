#!/usr/bin/env python

from setuptools import setup

setup(
	name="csssprite",
	version="0.9",
	description="A simple class for merging images into a sprite with accompanying css",
	author="Kailash Nadh",
	author_email="kailash.nadh@gmail.com",
	url="http://github.com/knadh/csssprite",
	packages=['csssprite'],
	download_url="http://github.com/knadh/csssprite",
	license="GPL v2",
	entry_points = {
		'console_scripts': [
			'csssprite = csssprite.csssprite:main'
		],
	},
	classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Programming Language :: Python",
		"Natural Language :: English",
		"License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Utilities",
		"Topic :: Multimedia :: Graphics",
		"Topic :: Software Development :: Libraries"
	],
	install_requires=["PIL"]
)
