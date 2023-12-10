from ctypes import c_uint, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibCore as cc

# BmCode wrap:
class Code :

    # Construction destruction:
    def __init__(self, aList=[]):
        size= len(aList)
        if size == 0 :
            self.Bmcode= cc.newBmCode( c_uint(0) )
        else :
            self.Bmcode= cc.newBmCode_numbers(
                c_uint(size),
                clib.uintArrayAs( size, aList )
            )
        

    def __del__(self):
        cc.deleteBmCode( self.Bmcode )

    # initialize:
    def initialize(self, aList):
        size= len(aList)
        cc.BmCode_initialize_numbers(
            self.Bmcode, c_uint(size),
            clib.uintArrayAs( size, aList )
        )
        return self
    
    def copy(self):
        cpy= Code()
        cc.BmCode_copy( cpy.Bmcode, self.Bmcode )
        return cpy

    # Accessor
    def dimention(self):
        return (int)(cc.BmCode_dimention( self.Bmcode ) )

    def at(self, i):
        assert( 0 < i and i <= self.dimention() )
        return (int)(cc.BmCode_at( self.Bmcode, (c_uint)(i) ) )    

    def list(self):
        return clib.readUintLst( self.dimention(), cc.BmCode_numbers(self.Bmcode) )

    # comparizon:
    def __eq__(a, b):
        return (int)( cc.BmCode_isEqualTo(a.Bmcode, b.Bmcode) ) != 0
    def __ne__(a, b):
        return (int)( cc.BmCode_isEqualTo(a.Bmcode, b.Bmcode) ) == 0
    def __lt__(a, b):
        return (int)( cc.BmCode_isLighterThan(a.Bmcode, b.Bmcode) ) != 0
    def __gt__(a, b):
        return (int)( cc.BmCode_isGreaterThan(a.Bmcode, b.Bmcode) ) != 0
    def __le__(a, b):
        return (int)( cc.BmCode_isGreaterThan(a.Bmcode, b.Bmcode) ) == 0
    def __ge__(a, b):
        return (int)( cc.BmCode_isLighterThan(a.Bmcode, b.Bmcode) ) == 0

    # Modification
    def resize(self, size):
        cc.BmCode_resize(self.Bmcode, c_uint(size))
    
    def at_set(self, i, value):
        assert( 0 < i and i <= self.dimention() )
        cc.BmCode_at_set(self.Bmcode, c_uint(i), c_uint(value) )

    # Iterate
    def __iter__(self):
        self.a = 1
        return IterCode(self)

class IterCode :

    # Construction destruction:
    def __init__( self, aCode ):
        self.conf= Code( [1 for i in range(aCode.dimention())] )
        self.range= aCode

    # Iterate
    def __iter__(self):
        self.conf= Code( [1 for i in range(self.range.dimention())] )
        return self
    
    def __next__(self):
        if cc.BmCode_isIncluding( self.range.Bmcode, self.conf.Bmcode ) :
            lst= self.conf.list()
            cc.BmCode_nextCode( self.range.Bmcode, self.conf.Bmcode )
            return lst
        else:
            raise StopIteration
