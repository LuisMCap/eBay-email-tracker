from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name = 'eBay email tracker',
	version = '0.0.5',
	description = 'Scapes an entire search page of a particular item on eBay and sends regular updates to an email address',
	py_modules = ['ebay_email_tracker', 'compare_old_and_new_entry', 'email_module', 'scrape_get_data', 'user_prompt', 'wait_module', 'misc_module'],
	package_dir = {'': 'src'},
	classifiers = [
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		],
	long_description=long_description,
	long_description_content_type="text/markdown",
	install_requires = [
	"pandas~=1.3.5",
	"numpy~=1.22.0",
	"requests~=2.27.1",
	"beautifulsoup4~=4.10.0",
	"lxml~=4.7.1"],

	url="https://github.com/LuisMCap",
	author = "Luis M. Capdevielle",
	author_email='luismcapdevielle@gmail.com',

	extras_require = {
	"dev": [
	"pytest>=3.7",]
	},

)