# Example Python project structure.

* With thanks and apologies to Tebeka.  Thanks Miki.

## Getting started:
1. set the project name in Makefile. `PROJECT = myproject`
2. rename bugs/ directory to match your project name.
3. set the project name in setup.py, replacing `bugs`.
4. set version in `__init__.py`
4. replace the silly default module and `misc/flux_capacitor`
5. replace this file with a README for your project.
6. Add requirements to `requirements.txt` and `test-requirements.txt`
7. install requirements for testing:
   `pip install -r test-requirements.txt`
8. start writing code:
  * check syntax with `make validate`
  * test it with `make test`
  * build a wheel module with `make wheel`
...
99. Profit?
