import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                 T E S T   p y B b M m  : :  B E N C H                    #
# ------------------------------------------------------------------------ #

import pyBbMm as bm

def test_BbMmBench_init():
    bench= bm.Bench()
    assert bench.size() == 0

def test_BbMmBench_init2():
    bench= bm.Bench(capacity=24)
    assert bench.size() == 0
    assert bench.capacity() == 24

def test_BbMmBench_attach():
    bench= bm.Bench(capacity=24)
    c1= bm.Code([1])
    bench.attachLast( c1, 1.0 )
    c2= bench.at( 1 )
    assert c1._ccode == c2._ccode 
    assert c2.dimention() == 1 
    assert c2.at(1) == 1
    assert bench.valueAt( 1 ) == 1.0
    assert str(bench) == "[[1]:1.0]"

    bench.attachLast( bm.Code([1, 2]), 1.2 )
    assert str(bench) == "[[1]:1.0, [1, 2]:1.2]"

    bench.attachLast( bm.Code([2, 4]), 100.2 )
    bench.attachFirst( bm.Code([0, 0]), 0.1 )

    assert str(bench) == "[[0, 0]:0.1, [1]:1.0, [1, 2]:1.2, [2, 4]:100.2]"

    c= bench.detachLast()
    assert str(c) == "[2, 4]"

    c= bench.detachFirst()
    assert str(c) == "[0, 0]"
    
def test_BbMmBench_initFull():
    bench= bm.Bench( [([0, 0], 1.0), ([1], 0.2), ([1, 2], 3), ([2, 4], 0)] )
    assert str(bench) == "[[0, 0]:1.0, [1]:0.2, [1, 2]:3.0, [2, 4]:0.0]"
    
    assert list( bench.range() ) == [ 1, 2, 3, 4 ]
    assert bench.list() == [([0, 0], 1.0), ([1], 0.2), ([1, 2], 3), ([2, 4], 0)]
