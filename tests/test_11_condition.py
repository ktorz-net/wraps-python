import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  C O N D I T I O N            #
# ------------------------------------------------------------------------ #

import pyBbMm as bm

def test_BbMmCondition_init():
    cond= bm.Condition()
    assert type(cond) == bm.Condition
    assert cond.domain() == 1
    assert cond.parentSpace().list() == [1]
    assert str( cond.at([1]) ) == '[[1]:1.0]'

def test_BbMmCondition_init2():
    cond= bm.Condition( 4, [2, 3], [([1, 1], 0.6), ([1, 2], 0.4)] )
    assert cond.domain() == 4
    assert cond.parentSpace().list() == [2, 3]
    assert cond.at([1, 3]).list() ==  [([1, 1], 0.6), ([1, 2], 0.4)] 
