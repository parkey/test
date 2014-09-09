# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import matplotlib
matplotlib.use('nbagg')
#%matplotlib inline
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
import numpy as np
from IPython.html.widgets import interact
from sympy.utilities.lambdify import lambdify
from sympy import *

# <codecell>

def set_size(width, height):
    'sätter bredd och höjd i centimeter'
    plt.figure(figsize=(width/2.54, height/2.54), dpi=600)

def set_ax():
    'sätter upp koordinatsystemet'
    plt.axis('equal')
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

def set_ticks():
    'sätter ut värden på axlarna'

    plt.xticks(
        (-np.pi, -np.pi/2,0,np.pi/2, np.pi),
        ('$-\pi$', '$-\pi/2$', '', '$\pi/2$', '$\pi$'),
    )

    plt.yticks(
        (-1, -1/2, 0, 1/2, 1),
        ('$-1$', '', '', '', '$1$'),
    )

# <headingcell level=3>

# Plotta trigonometrisk funktion med dess derivata och primitiva funktion

# <codecell>

from sympy.abc import x
import re

def l(f):
    return lambdify(x, f, modules=('numpy',))

X = np.linspace(-np.pi, np.pi)

def _lt(expr):
    '''denna snyggar till latex från sympy'''
    l = latex(expr)
    # ta bort ett överflödigt par parenteser ur latex-strängen
    e = re.sub('\\\\left \((.*) \\\\right \)', '\, \\1', l)
    # infoga lite utrymme före funktionen
    e = re.sub('(\\\\[sin|cos|tan])', '\, \\1', e)
    return e

def run():
    @interact(i=(1,5))
    def run(i):
        set_size(40,20)
        #figsize(40,20)
        set_ax()
        f0 = sin(x)
        f1 = f0.replace(x, x*i)
        f2 = diff(f1)
        f3 = integrate(f1)
        plt.plot(X, l(f0)(X), label='$ f\,(x) = \, {} $'.format(_lt(f0)))
        plt.plot(X, l(f1)(X), label='$ f\,(x) = \, {} $'.format(_lt(f1)))
        plt.plot(X, l(f2)(X), label='$ f \, \prime \, (x) = \, \mathrm{{D}} \, {} \, = \, {}$'.format(_lt(f1), _lt(f2)))
        plt.plot(X, l(f3)(X), label='$ F\,(x) = \int \,\, {} \, \mathrm{{d}}x \, = \, {} $'.format(_lt(f1), _lt(f3)))
        plt.legend();

# <codecell>

if __name__ == '__main__':
    run()

