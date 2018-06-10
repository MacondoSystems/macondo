
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='macondo',
    version='0.0.0.1',
    author='Andres Lujan',
    author_email='info@andresroot.co',
    description='A CMS',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MacondoSystems/macondo/',
    packages=['macondo'],
    keywords=['cms', 'django', 'privacy'],
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ),
)
