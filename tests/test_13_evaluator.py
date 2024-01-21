import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  E V A L U A T O R            #
# ------------------------------------------------------------------------ #

import pyBbMm as bm

def test_BbMmEvaluator_init():
    reward= bm.Evaluator()
    assert type(reward) == bm.Evaluator
