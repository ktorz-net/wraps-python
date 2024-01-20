import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                 T E S T   p y B b M m  : :  T R E E                      #
# ------------------------------------------------------------------------ #

import pyBbMm as bm

def test_BbMmTree_init():
    tree= bm.Tree()
    assert tree.outputSize() == 1
    assert tree.at([1]) == 1
    assert tree.at_value([1]) == 0.0

def test_BbMmTree_init2():
    stateSpace= bm.Code([2, 3])
    tree= bm.Tree( stateSpace.list(), 4 )
    assert tree.outputSize() == 4
    for c in stateSpace :
        assert tree.at(c) == 1
        assert tree.at_value(c) == 0.0    
    assert str( tree.asBench() ) == '[[0, 0, 1]:0.0]'

def test_BbMmtree_construct():
    tree= bm.Tree( [2, 4], 8 )
    tree.initialize( 3 )
    assert str( tree.asBench() ) == '[[1, 0, 3]:0.0, [2, 0, 3]:0.0]'
    tree.at_set( [1, 2], 1 )
    tree.at_set( [1, 4], 4 )
    assert str( tree.asBench() ) == '[[1, 1, 3]:0.0, [1, 2, 1]:0.0, [1, 3, 3]:0.0, [1, 4, 4]:0.0, [2, 0, 3]:0.0]'