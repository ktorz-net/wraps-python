import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  E V A L U A T O R            #
# ------------------------------------------------------------------------ #

import pyBbMm as bm

def test_BbMmEvaluator_init():
    eval= bm.Evaluator()
    assert type(eval) == bm.Evaluator
    assert eval.inputSpace().list() == [2]
    assert eval.numberOfCriteria() == 1
    assert eval.weights().list() == [1.0]
    assert eval.criteriaWeight(1) == 1.0
