# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Börja med Pandas

# <codecell>

from IPython.display import display
import pandas

# <codecell>

from pandas import DataFrame

# <codecell>

frame = DataFrame(
    index=(
        'Sverige', 'Österrike',
    ),
    data={
        '2012': (255000, 412000,),
        '2013': (9000000, 4120000,),
    },
    #columns=('land', 'area',),
)

# <codecell>

display(frame)

# <codecell>

frame.plot(kind='barh');

# <codecell>


