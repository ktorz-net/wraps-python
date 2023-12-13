import sys
sys.path.insert( 1, __file__.split('tests')[0] )
# ------------------------------------------------------------------------ #
#               T E S T   p y B b M m  C l i b C o r e                     #
# ------------------------------------------------------------------------ #
from ctypes import c_uint, c_void_p, c_ulong
from numpy import empty
from pyBbMm import clib, clibCore as cc

def test_ccCode_init():
    cCode= cc.newBmCode_all(2, 3)
    assert cc.BmCode_dimention( cCode ) == 2
    for i in range(1, 3) :
        assert cc.BmCode_at( cCode, i ) == 3
    cc.deleteBmCode( cCode )

def test_ccVector_init():
    cVector= cc.newBmVector_all(2, 3.0)
    assert cc.BmVector_dimention( cVector ) == 2
    for i in range(1, 3) :
        assert cc.BmVector_at( cVector, i ) == 3.0
    cc.deleteBmVector( cVector )

def test_ccBench_init():
    cBench= cc.newBmBench(2)
    assert cc.BmBench_size(cBench) == 0
    assert cc.BmBench_capacity(cBench) == 2
    cc.deleteBmBench( cBench )

def test_ccTree_init():
    cTree= cc.newBmTree(2, 4)
    assert cc.BmTree_outputSize(cTree) == 4
    cc.deleteBmTree(cTree)

def test_ccCondition_init():
    cCondition= cc.newBmConditionBasic(4)
    assert cc.BmCondition_output(cCondition) == 4
    cc.deleteBmCondition(cCondition)

def test_ccInferer_init():
    cCode= cc.newBmCode_all(3, 3)
    cInf= cc.newBmInferer( cCode, 2, 1)
    assert cc.BmInferer_inputDimention(cInf) == 2
    assert cc.BmInferer_outputDimention(cInf) == 1
    cc.deleteBmInferer(cInf)
    cc.deleteBmCode( cCode )

def test_ccEvaluator_init():
    cEval= cc.newBmEvaluatorBasic(3, 2)
    assert cc.BmEvaluator_numberOfCriteria(cEval) == 2
    cc.deleteBmEvaluator(cEval)
