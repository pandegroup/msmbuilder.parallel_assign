Parallel assignment for MSMBuilder using IPython.parallel
=========================================================

Overview
--------
The AssignMPI.py script in MSMBuilder which I wrote a few months ago is
embarrassingly bad. This module is my best attempt to provide a lasting,
powerful, flexible, parallel solution to assigning big datasets.

Because it uses `IPython.parallel` as opposed to my own homegrown mpi4py
code, this code is a lot more flexible. It also should be a lot more stable/bug
free. It also checkpoints much faster by only writing the necessary incremental
updates to the files on disk as opposed to completely rewriting them each time.

Workflow
--------
The flexibility of `IPython.parallel` comes at slight cost in complexity.
`IPython.parallel` is basically a master-worker framework. The first step
is thus to start workers.

To start 1 worker on your local node, you can use the command

    ipcluster start --n=1

The `ipcluster` command does two things. First, it starts something called a
controller, and next it starts a bunch of engines (in this case only one since
we gave it n=1). The engines' job is to actually do our work. The controller is
not as interested. Its job is to coordinate with the engines and handle things
like task scheduling.

Once the controller/engines are up and running, we can run `AssignIPP.py`.
One of the first things the script will try to do is connect to the controller.
Then it will prepare the jobs, submit then, and save the results as they return.

PBS Workers
-----------

Simply starting a single engine on your local node is pretty boring. Instead, you
probably want your engine to be on other nodes.

On Stanford's certainty cluster, I can do the following from two DIFFERENT nodes
    
    rmcgibbo@certainty-a:
    $ ipcontroller --ip '*'
    
    rmcgibbo@certainty-b:
    $ ipengine
    
On certainty-a, I see

    2012-08-17 00:14:07.051 [IPControllerApp] registration::finished registering engine 0:'661ecce8-8d2e-41d2-97f4-6715fe4a8692'
    2012-08-17 00:14:07.052 [IPControllerApp] engine::Engine Connected: 0
    





