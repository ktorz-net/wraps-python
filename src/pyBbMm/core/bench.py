from . import clibBbMm as cc
from .clibBbMm import c_digit, c_double
from .code import Code
from .vector import Vector

# BmBench wrap:
class Bench :
    # Construction destruction:
    def __init__(self, aListOfTuples=[], capacity= 16, cbench= None):
        if cbench is None :
            capacity= max( capacity, len(aListOfTuples) )
            self._cbench= cc.newBmBench( c_digit(capacity) )
            for codeList, v in aListOfTuples :
                if type(v) is list :
                    self.attachLast( Code( codeList ), Vector( v ) )
                else :
                    self.attachLast( Code( codeList ), Vector( [v] ) )
            self._cmaster= True
        else: 
            self._cbench= cbench
            self._cmaster= False
    
    def __del__(self):
        if self._cmaster :
            cc.deleteBmBench( self._cbench )
    
    def initialize( self, aListOfTuples=[], capacity= 16 ):
        capacity= max( capacity, len(aListOfTuples) )
        cc.BmBench_reinit( self._cbench, c_digit(capacity) )
        for codeList, vectorList in aListOfTuples :
            self.attachLast( Code( codeList ), Vector( vectorList ) )
        return self
            
    # Accessor
    def size( self ):
        return cc.BmBench_size( self._cbench )
    
    def codeAt(self, i):
        return Code( ccode= cc.BmBench_codeAt( self._cbench, c_digit(i) ) )
    
    def vectorAt( self, i ):
        return Vector( cvector=cc.BmBench_vectorAt( self._cbench, c_digit(i) ) )

    def digitAt( self, i ):
        return cc.BmBench_digitAt( self._cbench, c_digit(i) )
    
    def valueAt( self, i ):
        return cc.BmBench_valueAt( self._cbench, c_digit(i) )
    
    def range(self):
        return range(1, self.size()+1)
    
    def asCodeValueList( self ):
        return [ (self.codeAt(i).asList(), self.valueAt(i)) for i in self.range() ]
    
    def asList( self ):
        return [ (self.codeAt(i).asList(), self.vectorAt(i).asList() ) for i in self.range() ]
    
    # Construction
    def attachLast( self, newCode, newVector ):
        assert newCode._cmaster 
        cc.BmBench_attachCode_vector(
            self._cbench,
            newCode._ccode,
            newVector._cvector )
        newCode._cmaster= False
        newVector._cmaster= False
    
    def detachLast( self ):
        code= Code( ccode= cc.BmBench_detach( self._cbench ) )
        code._cmaster= True
        return code

    def attachFirst( self, newCode, newVector ):
        assert newCode._cmaster 
        cc.BmBench_attachFrontCode_vector(
            self._cbench,
            newCode._ccode,
            newVector._cvector )
        newCode._cmaster= False
        newVector._cmaster= False
    
    def detachFirst( self ):
        code= Code( ccode= cc.BmBench_detachFront( self._cbench ) )
        code._cmaster= True
        return code

    def at_setValue(self, i, value):
        cpointer= cc.BmBench_at_setValue(
                        self._cbench,
                        c_digit(i),
                        c_double(value)
        )
        return Code( ccode= cpointer )

    # dump and load:
    def dump(self):
        descriptor= self.asList()
        return descriptor
    
    def load(self, descriptor):
        return self.initialize( descriptor )
    
    # Print 
    def __str__(self):
        size= self.size()
        if size == 0 :
            return "bench[]"
        s= "bench["+ str( self.codeAt(1).asList() ) +":"+ str( self.vectorAt(1).asList() )
        for i in range(2, size+1) :
            s+= ", "+ str( self.codeAt(i).asList() ) +":"+ str( self.vectorAt(i).asList() )
        return s+"]"