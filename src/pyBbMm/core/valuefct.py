from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibBbMm as cc
from .code import Code
from .vector import Vector
from .bench import Bench
from .tree import Tree

class ValueFct:
    # Construction destruction:
    def __init__(self, inputRanges=[1], outputs=[0.0], cvaluefct= None):
        if cvaluefct is None :
            inputCode= Code( inputRanges )
            outputVector= Vector( outputs )
            self._cvaluefct= cc.newBmValueFctWith(
                inputCode._ccode,
                outputVector._cvector
            )
            inputCode._cmaster= False
            outputVector._cmaster= False
            self._cmaster= True
        else: 
            self._cvaluefct= cvaluefct
            self._cmaster= False
    
    def __del__(self):
        if self._cmaster :
            cc.deleteBmValueFct( self._cvaluefct )

    # Accessor
    def inputs( self ):
        return self.selector().inputs()
   
    def selector( self ):
        return Tree( ctree= cc.BmValueFct_selector( self._cvaluefct ) )
    
    def outputs( self ):
        return Vector( cvector= cc.BmValueFct_outputs( self._cvaluefct ) ).asList()

    def getFrom( self, input ):
        return cc.BmValueFct_from( self._cvaluefct, Code(input) )

    def asBench( self ):
        bench= Bench( cbench=cc.BmValueFct_asNewBench( self._cvaluefct ) )
        bench._cmaster= True
        return bench
        
    def asList( self ):
        return self.asBench().asCodeValueList()

    # Construction
    def initializeWith( self, inputCode, vectorValues ):
        assert( inputCode._cmaster ) # free to attach...
        assert( vectorValues._cmaster ) # free to attach...
        cc.BmValueFct_reinitWith(
            self._cvaluefct,
            inputCode._ccode,
            vectorValues._cvector
        )
        inputCode._cmaster= False
        vectorValues._cmaster= False
        return self
    
    def initialize( self, input, values ):
        return self.initializeWith( Code( input ), Vector( values ) )
    
    def addValue( self, value ):
        return cc.BmValueFct_addValue( self._cvaluefct, c_double(value) )

    def from_set(self, input, outputId ):
        inputCode= Code( input )
        cc.BmValueFct_from_set(
            self._cvaluefct,
            inputCode._ccode,
            c_uint(outputId)
        )
        inputCode._cmaster= False
        return self
    