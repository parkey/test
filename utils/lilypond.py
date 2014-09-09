# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=3>

# LILYPOND: Skapa musik-snippets från IPython

# <codecell>

from IPython.core.display import display
from IPython.core.display import Image

def show(data, filename='lilypond_temp'):
    '''denna skriver ut noter från lilypond-uppmärkning'''

    template='''\
\\version "2.14.2"
\\header {{
  tagline = ""  % removed
}}
{{
  {}
}}
'''
    with open('{}.ly'.format(filename), 'w') as f:
        f.write(template.format(data))

    get_ipython().run_cell_magic('bash', '', '''\
lilypond --png {0}.ly > /dev/null 2>&1
#lilypond --png {0}.ly
convert -trim {0}.png {0}.png
'''.format(filename))

    display(Image(filename='{}.png'.format(filename)))

#plocka ut sida från pdf
#from IPython.display import display
#from wand.image import Image as WImage
#img = WImage(filename='test1.pdf')
#display(img)

# <headingcell level=6>

# Testa, men inte om modulen är importerad

# <codecell>

if __name__ == '__main__':
    show("c'")

# <codecell>


