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
