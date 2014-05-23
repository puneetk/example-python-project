import bugs

from setuptools import setup
from os.path import dirname, realpath, join
import re

# A comment is a line starting with # or --
is_comment = re.compile('^\s*(#|--).*').match


def load_requirements(fname):
    here = dirname(realpath(__file__))
    fname = join(here, fname)

    with open(fname) as fo:
        return [line.strip() for line in fo
                if not is_comment(line) and line.strip()]

setup(
    name='bugs',
    version=bugs.__version__,
    packages=['bugs'],
    install_requires=load_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'bugs = bugs.__main__:main',
        ]
    },
    tests_require=load_requirements('test-requirements.txt'),
)
