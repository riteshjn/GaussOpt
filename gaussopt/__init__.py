"""Analyze quasi-optical systems using Gaussian beam analysis.

"""

from __future__ import division, absolute_import, print_function

from . import frequency
from . import component
from . import system
from . import util

from .frequency import *
from .component import *
from .system import System 
from .util import set_verbosity

import matplotlib as mpl 
import seaborn as sns
from cycler import cycler

sns.set_style("whitegrid",
              {'axes.edgecolor': '.2',
               'axes.facecolor': 'white',
               'axes.grid': True,
               'axes.linewidth': 0.5,
               'figure.facecolor': 'white',
               'grid.color': '.8',
               'grid.linestyle': u'-',
               'legend.frameon': True,
               'xtick.color': '.15',
               'xtick.direction': u'in',
               'xtick.major.size': 3.0,
               'xtick.minor.size': 1.0,
               'ytick.color': '.15',
               'ytick.direction': u'in',
               'ytick.major.size': 3.0,
               'ytick.minor.size': 1.0,
               })

sns.set_context("poster")
_default = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
            '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
mpl.rcParams['axes.prop_cycle'] = cycler(color=_default)

_ratio = 4./3.
_longaxis = 7.
_shortaxis = _longaxis / _ratio
mpl.rc("figure", figsize=(_longaxis, _shortaxis))

__author__ = "John Garrett"
__email__ = "garrettj403@gmail.com"
__version__ = "0.1"
