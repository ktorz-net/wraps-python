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
    assert tree.size() == 0

def test_BbMmTree_init2():
    stateSpace= bm.Code([2, 3])
    tree= bm.Tree( stateSpace.list(), 4 )
    assert tree.outputSize() == 4
    for c in stateSpace :
        assert tree.at(c) == 1
        assert tree.at_value(c) == 0.0    
    assert str( tree.asBench() ) == '[[0, 0, 1]:0.0]'

def test_BbMmTree_construct():
    tree= bm.Tree( [2, 4], 8 )
    tree.clear( 3 )
    assert str( tree.asBench() ) == '[[1, 0, 3]:0.0, [2, 0, 3]:0.0]'
    assert tree.size() == 1
    tree.at_set( [1, 2], 1 )
    tree.at_set( [1, 4], 4 )
    assert str( tree.asBench() ) == '[[1, 1, 3]:0.0, [1, 2, 1]:0.0, [1, 3, 3]:0.0, [1, 4, 4]:0.0, [2, 0, 3]:0.0]'
    assert tree.size() == 2

def test_BbMmTree_dump():
    tree= bm.Tree( [2, 4, 2], 8 )
    tree.clear( 2 )
    tree.at_set( [1, 0, 2], 1 )
    tree.at_set( [1, 4, 0], 4 )
    dump= tree.dump()
    
    assert type( dump ) == type({})
    assert list(dump.keys()) == ["input", "output", "branches"]
    assert dump["input"] == [2, 4, 2]
    assert dump["output"] == 8

    for b in dump["branches"] :
        print( b )

    assert dump["branches"] == [
        {'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 2)]},
        {'child': 1, 'iInput': 3, 'states': [('child', 2), ('child', 3)]},
        {'child': 2, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 2), ('leaf', 2), ('leaf', 4)]},
        {'child': 3, 'iInput': 2, 'states': [('leaf', 1), ('leaf', 1), ('leaf', 1), ('leaf', 4)]}
    ]
    
    print( tree.dumpStr() )
    assert tree.dumpStr().split("\n") == [
        "{",
        "  input: [2, 4, 2]",
        "  output: 8",
        "  branches: [{'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 2)]}, {'child': 1, 'iInput': 3, 'states': [('child', 2), ('child', 3)]}, {'child': 2, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 2), ('leaf', 2), ('leaf', 4)]}, {'child': 3, 'iInput': 2, 'states': [('leaf', 1), ('leaf', 1), ('leaf', 1), ('leaf', 4)]}]",
        "}"
    ]

def ttest_BbMmTree_load():
    descriptor= {
        "input": [],
        "output": 0,
        "bench": [([0, 1, 1, 2], 0.0), ([0, 1, 2, 1], 0.0), ([0, 2, 1, 2], 0.0), ([0, 2, 2, 1], 0.0), ([0, 3, 1, 2], 0.0), ([0, 3, 2, 1], 0.0), ([0, 4, 1, 4], 0.0), ([0, 4, 2, 4], 0.0), ([2, 0, 0, 2], 0.0)]
    }

    tree= bm.Tree().load( descriptor )
    
    dump= tree.dump()
    assert type( dump ) == type({})
    assert list(dump.keys()) == ["input", "output", "bench"]
    assert dump["input"] == []
    assert dump["output"] == 0
    assert dump["bench"] == [([0, 1, 1, 2], 0.0), ([0, 1, 2, 1], 0.0), ([0, 2, 1, 2], 0.0), ([0, 2, 2, 1], 0.0), ([0, 3, 1, 2], 0.0), ([0, 3, 2, 1], 0.0), ([0, 4, 1, 4], 0.0), ([0, 4, 2, 4], 0.0), ([2, 0, 0, 2], 0.0)]

    print( tree.dumpStr() )
    assert tree.dumpStr().split("\n") == [
        "{",
        "  input: []",
        "  output: 0",
        "  bench: [([0, 1, 1, 2], 0.0), ([0, 1, 2, 1], 0.0), ([0, 2, 1, 2], 0.0), ([0, 2, 2, 1], 0.0), ([0, 3, 1, 2], 0.0), ([0, 3, 2, 1], 0.0), ([0, 4, 1, 4], 0.0), ([0, 4, 2, 4], 0.0), ([2, 0, 0, 2], 0.0)]",
        "}"
    ]