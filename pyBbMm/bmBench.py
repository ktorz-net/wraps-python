from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibCore as cc
from .bmCode import Code

# BmBench wrap:
class Bench :
    # Construction destruction:
    def __init__(self, capacity= 16):
        self._cbench= cc.newBmBench( c_uint(capacity) )
        self._cmaster= True

    def __del__(self):
        if self._cmaster :
            cc.deleteBmBench( self._cbench )
    
    # Accessor
    def size( self ):
        return cc.BmBench_size( self._cbench )
    
    def capacity( self ):
        return cc.BmBench_capacity( self._cbench )
    
    def at_code(self, i):
        return Code( ccode= cc.BmBench_at_code( self._cbench, c_uint(i) ) )
    
    def at_value( self, i ):
        return cc.BmBench_at_value( self._cbench, c_uint(i) )

    # Construction
    def attachLast( self, newCode, value ):
        assert newCode._cmaster 
        cc.BmBench_attachLast(
            self._cbench,
            newCode._ccode,
            c_double(value) )
        newCode._cmaster= False
    
    def detachLast( self ):
        code= Code( ccode= cc.BmBench_detachLast( self._cbench ) )
        code._cmaster= True
        return code

    def attachFirst( self, newCode, value ):
        assert newCode._cmaster 
        cc.BmBench_attachFirst(
            self._cbench,
            newCode._ccode,
            c_double(value) )
        newCode._cmaster= False
    
    def detachFirst( self ):
        code= Code( ccode= cc.BmBench_detachFirst( self._cbench ) )
        code._cmaster= True
        return code

    def at_setValue(self, i, value):
        cpointer= cc.BmBench_at_setValue(
                        self._cbench,
                        c_uint(i),
                        c_double(value)
        )
        return Code( ccode= cpointer )

    # Print 
    def __str__(self):
        size= self.size()
        if size == 0 :
            return "[]"
        s= "["+ str( self.at_code(1) ) +":"+ str( self.at_value(1) )
        for i in range(2, size+1) :
            s+= ", "+ str( self.at_code(i) ) +":"+ str( self.at_value(i) )
        return s+"]"