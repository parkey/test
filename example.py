# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Basic IPython Notebook Experiments

# <headingcell level=3>

# Test run nbinclude

# <markdowncell>

# "nbinclude" runs all cells in a notebook and puts the output in the calling notebook.

# <markdowncell>

# nbinclude needs the code below in the header of the notebook where include will be done.

# <codecell>

# Cross-notebook include shim
with open("/home/sysadm/ipynb/nbinclude.ipynb") as nbinclude_f: # don't rename nbinclude_f
    import IPython.nbformat.current
    get_ipython().run_cell(IPython.nbformat.current.read(nbinclude_f, 'json').worksheets[0].cells[0].input)
    
#There is also a magic macro, #NBINCLUDE_STOP (exact spelling).
#The remainder of the cell containing the macro, and any cells after it, will not be read by the nbinclude system.

# <codecell>

nbinclude('utils/pandas/demo');

# <headingcell level=2>

# The "utils" package can be used like this

# <headingcell level=3>

# The very basic notebook functions in utils can be called like this

# <codecell>

from utils import (
    lilypond as lp,
    plot as pl,
)

# <headingcell level=3>

# Test lilypond inline snippet

# <codecell>

lp.show "c'"

# <headingcell level=3>

# Test the plot functions

# <codecell>

pl.run()

# <headingcell level=3>

# Run pandas demo

# <codecell>

import utils.pandas.demo
d.test()

