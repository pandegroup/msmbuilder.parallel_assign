import sys, os, shutil
import subprocess
import tempfile
import time
import numpy.testing as npt
from nose.tools import eq_, ok_
import IPython as ip

from msmbuilder import Serializer
from common import fixtures_dir
from msmbuilder.parallel_assign.scripts import AssignParallel

def test_setup_logger():
    progname = 'TEST PROGNAME'
    message = 'TEST MESSAGE'
    sys.argv[0] = progname

    fid, path = tempfile.mkstemp()
    stream = open(path, 'w')

    logger = AssignParallel.setup_logger(console_stream=stream)
    logger.info(message)
    
    stream.flush()
    line = open(path).readlines()[0]
    os.unlink(path)

    ok_(line.startswith(progname))
    ok_(line.endswith(message + '\n'))

class test_main:
    class Args:
            metric = 'dihedral'
            dihedral_metric = 'euclidean'
            dihedral_p = 2
            dihedral_angles = 'phi'
            project = os.path.join(fixtures_dir(), 'ProjectInfo.h5')
            generators = os.path.join(fixtures_dir(), 'Gens.lh5')
            profile = 'default'
            cluster_id = ''
            chunk_size=10

    def test_1(self):
        try:
            subprocess.Popen('ipcluster start --n=1 --daemonize', shell=True)
            time.sleep(5)
            
            args = self.Args()
            args.output_dir = tempfile.mkdtemp()

            logger = AssignParallel.setup_logger()
            AssignParallel.main(args, logger)

            assignments = Serializer.LoadData(os.path.join(args.output_dir, 'Assignments.h5'))
            r_assignments = Serializer.LoadData(os.path.join(fixtures_dir(), 'Assignments.h5'))
            distances = Serializer.LoadData(os.path.join(args.output_dir, 'Assignments.h5.distances'))
            r_distances = Serializer.LoadData(os.path.join(fixtures_dir(), 'Assignments.h5.distances'))
            
            npt.assert_array_equal(assignments, r_assignments)
            npt.assert_array_almost_equal(distances, r_distances)
        
        except:
            raise
        finally:
            shutil.rmtree(args.output_dir)
            subprocess.Popen('ipcluster stop', shell=True).wait()

    def test_2(self):
        try:
            subprocess.Popen('ipcluster start --cluster-id=testclusterid --n=1 --daemonize', shell=True)
            time.sleep(5)
            
            args = self.Args()
            args.output_dir = tempfile.mkdtemp()
            args.cluster_id = 'testclusterid'

            logger = AssignParallel.setup_logger()
            AssignParallel.main(args, logger)

            assignments = Serializer.LoadData(os.path.join(args.output_dir, 'Assignments.h5'))
            r_assignments = Serializer.LoadData(os.path.join(fixtures_dir(), 'Assignments.h5'))
            distances = Serializer.LoadData(os.path.join(args.output_dir, 'Assignments.h5.distances'))
            r_distances = Serializer.LoadData(os.path.join(fixtures_dir(), 'Assignments.h5.distances')) 

            npt.assert_array_equal(assignments, r_assignments)
            npt.assert_array_almost_equal(distances, r_distances)
        
        except:
            raise
        finally:
            shutil.rmtree(args.output_dir)
            subprocess.Popen('ipcluster stop', shell=True).wait()
