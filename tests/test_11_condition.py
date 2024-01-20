import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  C O N D I T I O N            #
# ------------------------------------------------------------------------ #

import pyBbMm as bm

def test_BbMmCondition_init():
    cond= bm.Condition()
    assert type(cond) == bm.Condition
