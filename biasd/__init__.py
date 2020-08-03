#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import likelihood
from . import laplace
from . import distributions
from . import mix_laplace

try:
	from . import mcmc

except:
	print("Could not import MCMC - install emcee and corner?")

try:
#if True:
	from . import mix_mcmc
except:
	print("Could not import mix MCMC")

#if 1:
try:
	from . import glob_mcmc
except:
	print("Could not import global MCMC")

from . import smd
try:
	from . import gui
except:
	print('Could not import gui - install PyQt5?')

__version__ = "0.1.1"
