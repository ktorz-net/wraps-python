import sys
sys.path.insert( 1, __file__.split('tests')[0] )
from pprint import pprint

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  I N F E R E R                 #
# ------------------------------------------------------------------------ #

import pyBbMm.core as bbmm

def test_BbMmInferer_init():
    trans= bbmm.Inferer()
    assert type(trans) == bbmm.Inferer
    assert( trans.inputDimention() == 1 )
    assert( trans.outputDimention() == 1 )
    assert( trans.shiftDimention() == 0 )
    assert( trans.overallDimention() == 2 )

def test_BbMmInferer_init2():
    trans= bbmm.Inferer( [2, 3, 4, 6], 2, 1 )
    assert( trans.inputDimention() == 2 )
    assert( trans.outputDimention() == 1 )
    assert( trans.shiftDimention() == 1 )
    assert( trans.overallDimention() == 4 )
    assert trans.inputs() == [2, 3]
    assert trans.outputs() == [6]
    assert trans.shifts() == [4]
    for iVar, dom in zip(range(1, 5), [2, 3, 4, 6]) :
        assert( trans.node(iVar).range() == dom )
        assert( trans.node(1).parentSpace().asList() == [1] )
        assert( trans.parents(1).asList() == [] )

def test_BbMmInferer_construction():
    trans= bbmm.Inferer( [6, 3, 4, 6], 2, 1 )
    trans.node_setDependancy( 3, [1], [(1, 0.25), (2, 0.25), (3, 0.25), (4, 0.25)] )
    trans.node_setDependancy( 4, [2, 3], [(1, 1.0)] )

    assert( trans.node(1).range() == 6 )
    assert( trans.parents(1).asList() == [] )
    assert( trans.node(1).parentSpace().asList() == [1] )
    
    assert( trans.node(2).range() == 3 )
    assert( trans.parents(2).asList() == [] )
    assert( trans.node(2).parentSpace().asList() == [1] )

    assert( trans.node(3).range() == 4 )
    assert( trans.parents(3).asList() == [1] )
    assert( trans.node(3).parentSpace().asList() == [6] )

    assert( trans.node(4).range() == 6 )
    assert( trans.parents(4).asList() == [2, 3] )
    assert( trans.node(4).parentSpace().asList() == [3, 4] )


def test_BbMmInferer_dump():
    trans= bbmm.Inferer( [6, 3, 4, 6], 2, 1 )
    condition= trans.node_setDependancy( 3, [1], [(1, 0.25), (2, 0.25), (3, 0.25), (4, 0.25)] )
    condition.fromList_set( [1], [(1, 1.0)] )
    condition.fromList_set( [2], [(2, 1.0)] )
    condition.fromList_set( [3], [(3, 1.0)] )
    condition= trans.node_setDependancy( 4, [2, 3], [(1, 0.7), (4, 0.3)] )
    condition.fromList_set( [1, 0], [(1, 1.0)] )
    condition.fromList_set( [0, 2], [(2, 1.0)] )

    assert( trans.overallDimention() == 4 )

    dump= trans.dump()
    #pprint( dump )
    dumpRef= {
        "inputs": [6, 3],
        "outputs": [6],
        "shifts": [4],
        'nodes': [
            { "nodeId": 1, 'parents': [], 'distributions': [[(1, 1.0)]], 'selector': [] },
            { "nodeId": 2, 'parents': [], 'distributions': [[(1, 1.0)]], 'selector': [] },
            {
                "nodeId": 3, 
                'parents': [1],
                'distributions': [
                    [(1, 0.25), (2, 0.25), (3, 0.25), (4, 0.25)],
                    [(1, 1.0)],
                    [(2, 1.0)],
                    [(3, 1.0)]
                ],
                'selector': [ {'child': 0, 'iInput': 1, 'states': [('leaf', 2), ('leaf', 3), ('leaf', 4), ('leaf', 1), ('leaf', 1), ('leaf', 1)]} ]
            },
            {
                "nodeId": 4, 
                'parents': [2, 3],
                'distributions': [[(1, 0.7), (4, 0.3)], [(1, 1.0)], [(2, 1.0)]],
                'selector': [
                        { 'child': 0, 'iInput': 1, 'states': [('child', 1), ('child', 2), ('child', 3)] },
                        { 'child': 1, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 3), ('leaf', 2), ('leaf', 2)] },
                        { 'child': 2, 'iInput': 2, 'states': [('leaf', 1), ('leaf', 3), ('leaf', 1), ('leaf', 1)] },
                        { 'child': 3, 'iInput': 2, 'states': [('leaf', 1), ('leaf', 3), ('leaf', 1), ('leaf', 1)] }
                    ]
            }
        ]
    }
    assert dump == dumpRef 
    #transBis= bbmm.Inferer().load( dump )
    #assert transBis.dump() == dumpRef

def test_BbMmInferer_process():
    trans= bbmm.Inferer( [6, 3, 4, 6], 2, 1 )
    condition= trans.node_setDependancy( 3, [1], [(1, 0.25), (2, 0.25), (3, 0.25), (4, 0.25)] )
    condition.fromList_set( [1], [(1, 1.0)] )
    condition.fromList_set( [2], [(2, 1.0)] )
    condition.fromList_set( [3], [(3, 1.0)] )
    condition= trans.node_setDependancy( 4, [2, 3], [(1, 0.7), (4, 0.3)] )
    condition.fromList_set( [1, 0], [(1, 1.0)] )
    condition.fromList_set( [0, 2], [(2, 1.0)] )

    bench= trans.distribution()
    assert bench.asList() == []
    assert( trans.inputDimention() == 2 )
    bench= trans.processFrom( [1, 1] )
    assert bench.asList() == [([1], 1.0)]
    trans.processFrom( [4, 2] )
    assert bench.asList() == [([1], 0.25), ([2], 0.25), ([3], 0.25), ([4], 0.25)]

    trans.processBench( bbmm.Bench( [([4, 2], 0.7), ([1, 3], 0.3)] ) )
    assert bench.asList() == [([1], 0.475), ([2], 0.175), ([3], 0.175), ([4], 0.175)]
