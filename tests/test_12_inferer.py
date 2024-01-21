import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  I N F E R E R                 #
# ------------------------------------------------------------------------ #

import pyBbMm as bm

def test_BbMmInferer_init():
    trans= bm.Inferer()
    assert type(trans) == bm.Inferer
    assert( trans.inputDimention() == 1 )
    assert( trans.outputDimention() == 1 )
    assert( trans.shiftDimention() == 0 )
    assert( trans.overallDimention() == 2 )

def test_BbMmInferer_init2():
    trans= bm.Inferer( [2, 3, 4, 6], 2, 1 )
    assert( trans.inputDimention() == 2 )
    assert( trans.outputDimention() == 1 )
    assert( trans.shiftDimention() == 1 )
    assert( trans.overallDimention() == 4 )
    for iVar, dom in zip(range(1, 5), [2, 3, 4, 6]) :
        assert( trans.node(iVar).domain() == dom )
        assert( trans.node(1).parentSpace().list() == [1] )
        assert( trans.parents(1).list() == [] )

def test_BbMmInferer_construction():
    trans= bm.Inferer( [6, 3, 4, 6], 2, 1 )
    trans.variable_setDependancy( 3, [1], [(1, 0.25), (2, 0.25), (3, 0.25), (4, 0.25)] )
    trans.variable_setDependancy( 4, [2, 3], [(1, 1.0)] )

    assert( trans.node(1).domain() == 6 )
    assert( trans.parents(1).list() == [] )
    assert( trans.node(1).parentSpace().list() == [1] )
    
    assert( trans.node(2).domain() == 3 )
    assert( trans.parents(2).list() == [] )
    assert( trans.node(2).parentSpace().list() == [1] )

    assert( trans.node(3).domain() == 4 )
    assert( trans.parents(3).list() == [1] )
    assert( trans.node(3).parentSpace().list() == [6] )

    assert( trans.node(4).domain() == 6 )
    assert( trans.parents(4).list() == [2, 3] )
    assert( trans.node(4).parentSpace().list() == [3, 4] )

def test_BbMmInferer_infers():
    trans= bm.Inferer( [6, 3, 4, 6], 2, 1 )
    condition= trans.variable_setDependancy( 3, [1], [(1, 0.25), (2, 0.25), (3, 0.25), (4, 0.25)] )
    condition.fromList_set( [1], [(1, 1.0)] )
    condition.fromList_set( [2], [(2, 1.0)] )
    condition.fromList_set( [3], [(3, 1.0)] )
    condition= trans.variable_setDependancy( 4, [2, 3], [(1, 0.7), (4, 0.3)] )
    condition.fromList_set( [1, 0], [(1, 1.0)] )
    condition.fromList_set( [0, 2], [(2, 1.0)] )

    bench= trans.distribution()
    assert bench.list() == []
    assert( trans.inputDimention() == 2 )
    trans.processFrom( [1, 1] )
    bench= trans.distribution()
    assert bench.list() == [([1], 1.0)]
    trans.processFrom( [4, 2] )
    assert bench.list() == [([1], 0.25), ([2], 0.25), ([3], 0.25), ([4], 0.25)]

    trans.processBench( bm.Bench( [([4, 2], 0.7), ([1, 3], 0.3)] ) )
    assert bench.list() == [([1], 0.475), ([2], 0.175), ([3], 0.175), ([4], 0.175)]
