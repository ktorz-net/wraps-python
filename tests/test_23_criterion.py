import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  C R I T E R I O N             #
# ------------------------------------------------------------------------ #

import pyBbMm.core as bm
from pyBbMm.core import clibBbMm as cc

def test_BbMmCriterion_init():
    instance= bm.Criterion()
    assert type(instance) == bm.Criterion
    assert instance.inputRanges() == [1]
    assert instance.outputs() == [0.0]

def test_BbMmCriterion_init2():
    instance= bm.Criterion( [2, 4], [0.0, 1.0, 0.5] )
    assert type(instance) == bm.Criterion
    assert instance.inputRanges() == [2, 4]
    assert instance.outputs() == [0.0, 1.0, 0.5]

def test_BbMmCriterion_construction():
    instance= bm.Criterion()
    instance.initialize( [2, 3], [0.01, 0.02, 0.03, 0.04] )

    assert instance.inputRanges() == [2, 3]
    assert instance.outputs() == [0.01, 0.02, 0.03, 0.04]

    assert instance.asList() == [([1, 0, 1], 0.01), ([2, 0, 1], 0.01)]

    assert instance.inputRanges() == [2, 3]
    assert instance.outputs() == [0.01, 0.02, 0.03, 0.04]

    instance.from_set( [1, 0], 1 )
    instance.from_set( [2, 0], 2 )
    instance.from_set( [1, 3], 3 )
    
    assert instance.asList() == [([1, 1, 1], 0.01), ([1, 2, 1], 0.01), ([1, 3, 3], 0.03), ([2, 0, 2], 0.02)]

if __name__ == "__main__" :
    test_BbMmCriterion_construction()