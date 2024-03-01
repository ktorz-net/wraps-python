from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibBbMm as cc

# BmVector wrap:
class Vector :

    # Construction destruction:
    def __init__(self, aList=[], cvector= None ):
        if cvector is None :
            size= len(aList)
            if size == 0 :
                self._cvector= cc.newBmVector( c_uint(0) )
            else :
                self._cvector= cc.newBmVector_values(
                    c_uint(size),
                    clib.doubleArrayAs( size, aList )
                )
            self._cmaster= True
        else : 
            self._cvector= cvector
            self._cmaster= False


    def __del__(self):
        if self._cmaster :
            cc.deleteBmVector( self._cvector )

    # initialize:
    def initialize(self, aList):
        size= len(aList)
        cc.BmVector_reinit( self._cvector, c_uint(size) )
        cc.BmVector_setValues( self._cvector, clib.doubleArrayAs( size, aList ) )
        return self
    
    def copy(self):
        cpy= Vector()
        cc.BmVector_copy( cpy._cvector, self._cvector )
        return cpy

    # Accessor
    def dimention(self):
        return (int)(cc.BmVectorDimention( self._cvector ) )

    def value(self, i):
        assert( 0 < i and i <= self.dimention() )
        return (float)(cc.BmVector_value( self._cvector, (c_uint)(i) ) )    

    def asList(self):
        return [ self.value(i) for i in range(1, self.dimention()+1) ]
    
    # comparizon:
    def __eq__(a, b):
        return (int)( cc.BmVector_isEqualTo(a._cvector, b._cvector) ) != 0
    def __ne__(a, b):
        return (int)( cc.BmVector_isEqualTo(a._cvector, b._cvector) ) == 0
    def __lt__(a, b):
        return (int)( cc.BmVector_isSmallerThan(a._cvector, b._cvector) ) != 0
    def __gt__(a, b):
        return (int)( cc.BmVector_isGreaterThan(a._cvector, b._cvector) ) != 0
    def __le__(a, b):
        return (int)( cc.BmVector_isGreaterThan(a._cvector, b._cvector) ) == 0
    def __ge__(a, b):
        return (int)( cc.BmVector_isSmallerThan(a._cvector, b._cvector) ) == 0

    # Modification
    def resize(self, size):
        cc.BmVector_redimention(self._cvector, c_uint(size))
    
    def at_set(self, i, value):
        assert( 0 < i and i <= self.dimention() )
        cc.BmVector_at_set(self._cvector, c_uint(i), c_double(value) )

    # dump and load:
    def dump(self):
        descriptor= self.asList()
        return descriptor
    
    def load(self, descriptor):
        return self.initialize( descriptor )