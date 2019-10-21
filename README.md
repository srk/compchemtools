# compchemtools
Miscellaneous utilities for Computational Chemistry/Quantum Chemistry/Molecular Dynamics codes and calculations.

Installation: For all these utilities, download the relevant subdirectory tree, then use 'python setup.py install', or use 'python setup.py sdist' to make a pip-installable .tar.gz file in a 'dist' subdirectory.

* opthelp - Find the current best structure in a Gaussian 09 geometry optimization run, then create a new input file starting from that geometry. Useful if you run out of optimization steps and/or patience during a geometry optimization run. 'Best' in this case is defined by the current lowest value of a figure of merit score, calculated as the product of the ratios of the usual 4 numerical optimization parameters to their set target values, with upward rounding to avoid zero values of the figure of merit score.
