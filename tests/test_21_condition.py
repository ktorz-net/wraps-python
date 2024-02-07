import sys
sys.path.insert( 1, __file__.split('tests')[0] )
import pprint

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  C O N D I T I O N            #
# ------------------------------------------------------------------------ #

import pyBbMm.core as bm

def test_BbMmCondition_init():
    cond= bm.Condition()
    assert type(cond) == bm.Condition
    assert cond.domain() == 1
    assert cond.parentSpace().list() == [1]
    assert cond.distributionSize() == 1
    assert cond.distributionAt(1).list() == [([1], 1.0)]
    assert cond.fromList([1]) == [(1, 1.0)]

def test_BbMmCondition_init2():
    cond= bm.Condition( 4, [2, 3], [(1, 0.6), (2, 0.4)] )
    assert cond.domain() == 4
    assert cond.parentSpace().list() == [2, 3]
    assert cond.fromList([1, 3]) == [(1, 0.6), (2, 0.4)] 

def test_BbMmCondition_construction():
    cond= bm.Condition( 4, [2, 3], [(1, 0.6), (2, 0.4)] )
    assert cond.fromList([1, 3]) == [(1, 0.6), (2, 0.4)]
    # From: parent-1 on 1 and whatever parent-2 Set: 3 certain. 
    cond.fromList_set( [1, 0], [(3, 1.0)] )
    # From: parent exactly on 1, 3 Set: 4 certain.
    cond.fromList_set( [1, 3], [(4, 1.0)] )
    assert cond.distributionSize() == 3
    # Test it:
    assert cond.fromList([1, 3]) == [(4, 1.0)]
    for parent in bm.Code([2, 3]):
        if parent[0] != 1 :
            assert cond.fromList(parent) == [(1, 0.6), (2, 0.4)]
        elif parent != [1, 3] :
            assert cond.fromList(parent) == [(3, 1.0)]

def test_BbMmCondition_construction2():
    cond= bm.Condition( 4, [2, 3], [(1, 0.6), (2, 0.4)] )
    cond.fromList_set( [1, 0], [(3, 1.0)] )
    assert cond.distributionSize() == 2
    cond.initialize( 4, [2, 3], [(1, 1.0)] )
    assert cond.distributionSize() == 1
    for parent in bm.Code([2, 3]):
        assert cond.fromList(parent) == [(1, 1.0)]

def test_BbMmCindition_dump():
    cond= bm.Condition( 4, [2, 3], [(1, 0.6), (2, 0.4)] )
    cond.fromList_set( [1, 0], [(3, 1.0)] )
    cond.fromList_set( [1, 3], [(4, 1.0)] )
    dump= cond.dump()
    pprint.pprint(dump)
    assert dump == {
        'distributions': [
            [([1], 0.6), ([2], 0.4)],
            [([3], 1.0)],
            [([4], 1.0)]
        ],
        'selector': {
            'input': [2, 3],
            'output': 6,
            'branches': [
                {'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 1)] },
                {'child': 1, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 2), ('leaf', 3)]}
            ]
        }
    }

def test_BbMmCindition_load():
    dump= {
        'distributions': [
            [([1], 0.6), ([2], 0.4)],
            [([3], 1.0)],
            [([4], 1.0)]
        ],
        'selector': {
            'input': [2, 3],
            'output': 6,
            'branches': [
                {'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 1)] },
                {'child': 1, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 2), ('leaf', 3)]}
            ]
        }
    }
    cond= bm.Condition().load( dump )
    assert cond.dump == dump
