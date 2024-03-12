import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                 T E S T   p y B b M m  : :  T R E E                      #
# ------------------------------------------------------------------------ #

import pyBbMm.core as bm

def test_BbMmTree_init():
    tree= bm.Tree()
    assert tree.at([1]) == 1
    assert tree.size() == 0

def test_BbMmTree_init2():
    stateSpace= bm.Code([2, 3])
    tree= bm.Tree( stateSpace.asList() )
    for c in stateSpace :
        assert tree.at(c) == 1
    assert str( tree.asBench() ) == 'bench[[0, 0, 1]:[0.0]]'

def ttest_BbMmTree_construct():
    tree= bm.Tree( [2, 4] )
    tree.clear( 3 )
    assert str( tree.asBench() ) == 'bench[[1, 0, 3]:[0.0], [2, 0, 3]:[0.0]]'
    assert tree.size() == 1
    tree.at_set( [1, 2], 1 )
    tree.at_set( [1, 4], 4 )
    assert str( tree.asBench() ) == 'bench[[1, 1, 3]:[0.0], [1, 2, 1]:[0.0], [1, 3, 3]:[0.0], [1, 4, 4]:[0.0], [2, 0, 3]:[0.0]]'
    assert tree.size() == 2

def test_BbMmTree_dump():
    tree= bm.Tree( [2, 4, 2] )
    tree.clear( 2 )
    tree.at_set( [1, 0, 2], 1 )
    tree.at_set( [1, 4, 0], 4 )
    dump= tree.dump()
    
    assert type( dump ) == type({})
    assert list(dump.keys()) == ["input", "branches"]
    assert dump["input"] == [2, 4, 2]

    for b in dump["branches"] :
        print( b )

    assert dump["branches"] == [
        {'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 2)]},
        {'child': 1, 'iInput': 3, 'states': [('child', 2), ('child', 3)]},
        {'child': 2, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 2), ('leaf', 2), ('leaf', 4)]},
        {'child': 3, 'iInput': 2, 'states': [('leaf', 1), ('leaf', 1), ('leaf', 1), ('leaf', 4)]}
    ]
    
def ttest_BbMmTree_load():
    descriptor= {
        "input": [2, 4, 2],
        "branches" : [
            {'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 2)]},
            {'child': 1, 'iInput': 3, 'states': [('child', 2), ('child', 3)]},
            {'child': 2, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 2), ('leaf', 2), ('leaf', 4)]},
            {'child': 3, 'iInput': 2, 'states': [('leaf', 1), ('leaf', 1), ('leaf', 1), ('leaf', 4)]}
        ]
    }
    
    tree= bm.Tree().load( descriptor )
    
    dump= tree.dump()
    assert type( dump ) == type({})
    assert list(dump.keys()) == ["input", "output", "branches"]
    assert dump["input"] == [2, 4, 2]
    assert dump["branches"] == [
        {'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 2)]},
        {'child': 1, 'iInput': 3, 'states': [('child', 2), ('child', 3)]},
        {'child': 2, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 2), ('leaf', 2), ('leaf', 4)]},
        {'child': 3, 'iInput': 2, 'states': [('leaf', 1), ('leaf', 1), ('leaf', 1), ('leaf', 4)]}
    ]