import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  E V A L U A T O R            #
# ------------------------------------------------------------------------ #

import pyBbMm.core as bm

def test_BbMmEvaluator_init():
    instance= bm.Evaluator()
    assert type(instance) == bm.Evaluator
    assert instance.inputRanges() == [1]
    assert instance.numberOfCriteria() == 1
    assert instance.weights() == [1.0]
    assert instance.criterion(1).inputRanges() == [2]
    assert instance.criterion(1).outputs() == [0.0]
    assert instance.criterionWeight(1) == 1.0
    assert instance.criterionMask(1) == []

def test_BbMmEvaluator_init2():
    instance= bm.Evaluator(  [2, 4, 3], 2  )
    assert type(instance) == bm.Evaluator
    assert instance.inputRanges() == [2, 4, 3]
    assert instance.numberOfCriteria() == 2
    assert instance.weights() == [1.0, 1.0]
    for i in range(1, instance.numberOfCriteria()+1) :
        assert instance.criterion(i).inputRanges() == [2]
        assert instance.criterion(i).outputs() == [0.0]
        assert instance.criterionWeight(i) == 1.0
        assert instance.criterionMask(i) == []

def test_BbMmEvaluator_construction():
    instance= bm.Evaluator( [2, 4, 3], 2 )

    criterion= instance.criterion_intialize( 1, [1, 3], [0.01, 0.02, 0.03, 0.04] )
    
    assert type(instance) == bm.Evaluator
    assert instance.inputRanges() == [2, 4, 3]
    assert instance.numberOfCriteria() == 2
    assert instance.weights() == [1.0, 1.0]

    criterion.from_set( [1, 0], 1 )
    instance.criterion(1).from_set( [2, 0], 2 )
    instance.criterion(1).from_set( [1, 3], 3 )

    criterion= instance.criterion_intialize( 2, [2], [3.0, -1.0, 0.0] )
    criterion.from_set( [1], 2 )

    assert instance.criterion(1).inputRanges() == [2, 3]
    assert instance.criterion(1).outputs() == [0.01, 0.02, 0.03, 0.04]
    assert instance.criterionWeight(1) == 1.0
    assert instance.criterionMask(1) == [1, 3]

    assert instance.criterion(2).inputRanges() == [4]
    assert instance.criterion(2).outputs() == [3.0, -1.0, 0.0]
    assert instance.criterionWeight(2) == 1.0
    assert instance.criterionMask(2) == [2]

    assert instance.criterion(1).asList() == [([1, 1, 1], 0.01), ([1, 2, 1], 0.01), ([1, 3, 3], 0.03), ([2, 0, 2], 0.02)]
    assert instance.criterion(2).asList() == [([1, 2], -1.0), ([2, 1], 3.0), ([3, 1], 3.0), ([4, 1], 3.0)]

def test_BbMmEvaluator_process():
    instance= bm.Evaluator( [2, 4, 4], 2 )

    criterion= instance.criterion_intialize( 1, [1, 3], [0.01, 0.02, 0.03, 0.04] )
    criterion.from_set( [1, 0], 1 )
    criterion.from_set( [2, 0], 2 )
    criterion.from_set( [1, 3], 3 )
    
    instance.criterion_intialize( 2, [2], [3.0, -1.0, 0.0] )
    instance.criterion(2).from_set( [1], 2 )
    instance.criterion_setWeight( 2, 2.0 )

    assert instance.processMulti( [1, 2, 4] ) == [0.01, 3.0]
    assert instance.process( [1, 2, 4] ) == 6.01

