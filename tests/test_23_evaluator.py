import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  E V A L U A T O R            #
# ------------------------------------------------------------------------ #

import pyBbMm.core as bm

def test_BbMmEvaluator_init():
    eval= bm.Evaluator()
    assert type(eval) == bm.Evaluator
    assert eval.inputSpace().list() == [1]
    assert eval.numberOfCriteria() == 1
    assert eval.weights().list() == [1.0]
    assert eval.criteriaWeight(1) == 1.0
    assert eval.criteria(1).asBench().list() == [([1], 0.0)]

def test_BbMmEvaluator_init2():
    eval= bm.Evaluator( [2, 4], 2 )
    assert type(eval) == bm.Evaluator
    assert eval.inputSpace().list() == [2, 4]
    assert eval.numberOfCriteria() == 2
    assert eval.weights().list() == [1.0, 1.0]
    assert eval.criteriaWeight(1) == 1.0
    assert eval.criteria(1).asBench().list() == [([1], 0.0)]
    assert eval.criteria(2).asBench().list() == [([1], 0.0)]

def test_BbMmEvaluator_construction():
    eval= bm.Evaluator( [2, 4, 4], 2 )

    eval.criteria_intialize( 1, [1, 3], [0.01, 0.02, 0.03, 0.04] )
    eval.criteria_intialize( 2, [2], [3.0, -1.0, 0.0] )
    assert type(eval) == bm.Evaluator
    assert eval.inputSpace().list() == [2, 4, 4]
    assert eval.numberOfCriteria() == 2
    assert eval.weights().list() == [1.0, 1.0]
    assert eval.criteriaWeight(1) == 1.0

    assert eval.criteria(1).asBench().list() == [([0, 0, 1], 0.01)]
    assert eval.criteria(2).asBench().list() == [([0, 1], 3.0)]

    eval.criteria(1).at_set( [1, 0], 1 )
    eval.criteria(1).at_set( [2, 0], 2 )
    eval.criteria(1).at_set( [1, 3], 3 )
    eval.criteria(2).at_set( [1], 2 )

    assert eval.criteria(1).asBench().list() == [([1, 1, 1], 0.01), ([1, 2, 1], 0.01), ([1, 3, 3], 0.03), ([1, 4, 1], 0.01), ([2, 0, 2], 0.02)]
    assert eval.criteria(2).asBench().list() == [([1, 2], -1.0), ([2, 1], 3.0), ([3, 1], 3.0), ([4, 1], 3.0)]


def test_BbMmEvaluator_process():
    eval= bm.Evaluator( [2, 4, 4], 2 )

    eval.criteria_intialize( 1, [1, 3], [0.01, 0.02, 0.03, 0.04] )
    eval.criteria(1).at_set( [1, 0], 1 )
    eval.criteria(1).at_set( [2, 0], 2 )
    eval.criteria(1).at_set( [1, 3], 3 )

    eval.criteria_intialize( 2, [2], [3.0, -1.0, 0.0] )
    eval.criteria(2).at_set( [1], 2 )
    eval.criteria_setWeight( 2, 2.0 )

    assert eval.processMulti( [1, 2, 4] ) == [0.01, 3.0]
    assert eval.process( [1, 2, 4] ) == 6.01
