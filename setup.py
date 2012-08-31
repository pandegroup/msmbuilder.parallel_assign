import sys
import glob
from distutils.core import setup

try:
    import msmbuilder
except ImportError:
    print >> sys.stderr, 'You need to install msmbuilder to use this package.'


setup(name='msmbuilder.parallel_assign',
      version = '1.0',
      description = 'Parallel Assignment MSMBuilder',
      packages=['msmbuilder.parallel_assign',
                'msmbuilder.parallel_assign.scripts'],
      package_dir={'msmbuilder.parallel_assign':'lib',
                   'msmbuilder.parallel_assign.scripts':'scripts'},
      scripts=filter(lambda elem: '_' not in elem, glob.glob('scripts/*'))
)
