import re
from setuptools import setup, find_packages

with open("README.rst", "rb") as f:
	long_descr = f.read().decode("utf-8")

setup(
	name = "mdtohtml",
	packages = find_packages(),
	entry_points = {
 			"console_scripts": ["mdtohtml = src.mdtohtml:main"]
		},
	version = version,
	description = "Duplicates folder and converts markdown files to html files",
	long_description = long_descr,
	author = "Oscar Vazquez",
	author_email = "oscar.vazquez2012@gmail.com",
	url = ""
)