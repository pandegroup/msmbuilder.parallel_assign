Parallel assignment for MSMBuilder using IPython.parallel
=========================================================

Overview
--------
The AssignMPI.py script in MSMBuilder which I wrote a few months ago is embarringly bad. This module is my best attempt to provide a lastig, powerful, flexible, parallel solution to assigning big datasets.

Because it uses IPython.parallel as opposed to my own homegrown mpi4py code, this code is a lot more flexible. It also should be a lot more stable/bug free. It also checkpoints much faster by only writing the necessary incremental updates to the files on disk as opposed to completely rewriting them each time.

Workflow
--------
The flexibility of IPython.parallel comes at slight cost in complexity. IPython.parallel is basically a master-worker framework. The first step is thus to start workers.

To start 1 worker on your local node, you can use the command

   ipcluster start --n=1


