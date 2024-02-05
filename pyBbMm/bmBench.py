from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibCore as cc
from .bmCode import Code

# BmBench wrap:
class Bench :
    # Construction destruction:
    def __init__(self, aListOfTuples=[], capacity= 16, cbench= None):
        if cbench is None :
            capacity= max( capacity, len(aListOfTuples) )
            self._cbench= cc.newBmBench( c_uint(capacity) )
            for codeList, value in aListOfTuples :
                self.attachLast( Code( codeList ), value )
            self._cmaster= True
        else: 
            self._cbench= cbench
            self._cmaster= False
    
    def __del__(self):
        if self._cmaster :
            cc.deleteBmBench( self._cbench )
    
    def initialize( self, aListOfTuples=[], capacity= 16 ):
        capacity= max( capacity, len(aListOfTuples) )
        cc.BmBench_reinit( self._cbench, c_uint(capacity) )
        for codeList, value in aListOfTuples :
            self.attachLast( Code( codeList ), value )
        return self
            
    # Accessor
    def size( self ):
        return cc.BmBench_size( self._cbench )
    
    def capacity( self ):
        return cc.BmBench_capacity( self._cbench )
    
    def at(self, i):
        return Code( ccode= cc.BmBench_at( self._cbench, c_uint(i) ) )
    
    def valueAt( self, i ):
        return cc.BmBench_valueAt( self._cbench, c_uint(i) )

    def range(self):
        return range(1, self.size()+1)
    
    def list( self ):
        return [ (self.at(i).list(), self.valueAt(i)) for i in self.range() ]
    
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

    # dump and load:
    def dump(self):
        descriptor= self.list()
        return descriptor
    
    def dumpStr(self):
        return str( self.dump() )
    
    def load(self, descriptor):
        return self.initialize( descriptor )
    
    # Print 
    def __str__(self):
        size= self.size()
        if size == 0 :
            return "[]"
        s= "["+ str( self.at(1) ) +":"+ str( self.valueAt(1) )
        for i in range(2, size+1) :
            s+= ", "+ str( self.at(i) ) +":"+ str( self.valueAt(i) )
        return s+"]"