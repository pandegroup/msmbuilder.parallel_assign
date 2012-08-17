import glob
from distutils.core import setup

setup(name='passign',
      version = '0.1',
      description = 'new methods being tested',
      packages=['passign'], #,'new_assigning.scripts'],
      package_dir={'passign':'lib'}, #,"new_assigning.scripts":'scripts'},
      scripts=filter(lambda elem: '_' not in elem, glob.glob('scripts/*'))
)
