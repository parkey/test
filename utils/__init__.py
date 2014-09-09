# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import display
import textwrap, os, markdown

github_user = 'parkey'
github_repo = 'test'
localgitbasepath = '/home/sysadm/ipynb/parkey/test'
basepath = 'http://nbviewer.ipython.org/github/{}/{}/blob/master/'.format(github_user, github_repo)

class md(str):
    def _repr_html_(self):
        return markdown.markdown(self, extensions=['tables'])

# <codecell>

def git_status():
    '''returnerar ett dict med listor på filnamn från git status -s'''
    try:
        curdir = os.getcwd()
        os.chdir(localbasepath)
        get_ipython().run_cell_magic('bash', '--out output', 'git status -s')
        stats = {'modified':[], 'deleted':[], 'other':[]}
        for f in output.split('\n'):
            if f.startswith(' M'):
                stats['modified'].append(f[3:])
            elif f.startswith(' D'):
                stats['deleted'].append(f[3:])
            if f.startswith('??'):
                stats['other'].append(f[3:])
    finally:
        os.chdir(curdir)
    return stats

# <codecell>

def _git_list():
    '''returnerar filer i arkivet men med sökväg relativt aktuell sökväg'''
    get_ipython().run_cell_magic('bash', '--out output', 'git ls-files {}'.format(localgitbasepath))
    return output.split('\n')

def git_list():
    '''returnerar filer i arkivet relativt rotkatalogen i filförrådet'''
    try:
        curdir = os.getcwd()
        os.chdir(localbasepath)
        get_ipython().run_cell_magic('bash', '--out output', 'git ls-files')
    finally:
        os.chdir(curdir)
    return output.split('\n')

# <codecell>

if __name__ == '__main__':
    display(git_list())

# <codecell>

def get_index(write_readme=False):
    '''generate content for README.md as MarkDown with links that render the directory contents as IPython notebooks'''

    table = textwrap.dedent('''\
        # IPython Notebook

        Fil|Beskrivning
        ---|-----------
    ''')
    
    for f in git_list():
        #print(f)
        if f.endswith('.ipynb') and f != 'index.ipynb':
            table += textwrap.dedent('''\
                [{0}]({1}{0})|
            '''.format(f, basepath))
    if write_readme:
        with open(os.path.join(localgitbasepath, 'README.md'), 'w') as f:
            f.write(table)
    return md(table)

# <codecell>

if __name__ == '__main__':
    display(get_index(True))

