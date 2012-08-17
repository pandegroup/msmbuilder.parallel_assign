from assigning import partition

def test_chunks_0():
    project = {'TrajLengths': [2,5]}
    chunk_size = 3
        
    got = partition(project, chunk_size)
    
    
    correct = [[(0, 0, 2), (1, 0, 1)],
               [(1, 1, 4)],
               [(1, 4,5)]]

    assert [e.canonical() for e in got] == correct
    assert sum(len(e) for e in got) == sum(project['TrajLengths'])

def test_chunks_1():
    project = {'TrajLengths': [2,1,10]}
    chunk_size = 4

    got = partition(project, chunk_size)
    correct = [[(0,0,2), (1,0,1), (2,0,1)],
               [(2,1,5)],
               [(2,5,9)],
               [(2,9,10)]]

    assert [e.canonical() for e in got] == correct
    assert sum(len(e) for e in got) == sum(project['TrajLengths'])
    