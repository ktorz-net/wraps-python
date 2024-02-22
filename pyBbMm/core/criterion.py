from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibBbMm as cc
from .code import Code
from .vector import Vector
from .bench import Bench
from .tree import Tree

class Criterion:
    # Construction destruction:
    def __init__(self, inputRanges=[1], outputs=[0.0], ccriterion= None):
        if ccriterion is None :
            inputCode= Code( inputRanges )
            outputVector= Vector( outputs )
            self._ccriterion= cc.newBmCriterionWith(
                inputCode._ccode,
                outputVector._cvector
            )
            inputCode._cmaster= False
            outputVector._cmaster= False
            self._cmaster= True
        else: 
            self._ccriterion= ccriterion
            self._cmaster= False
    
    def __del__(self):
        if self._cmaster :
            cc.deleteBmCriterion( self._ccriterion )

    # Accessor
    def inputs( self ):
        return self.selector().inputs()
   
    def selector( self ):
        return Tree( ctree= cc.BmCriterion_selector( self._ccriterion ) )
    
    def outputs( self ):
        return Vector( cvector= cc.BmCriterion_outputs( self._ccriterion ) ).asList()

    def getFrom( self, input ):
        return cc.BmCriterion_from( self._ccriterion, Code(input) )

    def asBench( self ):
        bench= Bench( cbench=cc.BmCriterion_asNewBench( self._ccriterion ) )
        bench._cmaster= True
        return bench
        
    def asList( self ):
        return self.asBench().asList()

    # Construction
    def initializeWith( self, inputCode, vectorValues ):
        assert( inputCode._cmaster ) # free to attach...
        assert( vectorValues._cmaster ) # free to attach...
        cc.BmCriterion_reinitWith(
            self._ccriterion,
            inputCode._ccode,
            vectorValues._cvector
        )
        inputCode._cmaster= False
        vectorValues._cmaster= False
        return self
    
    def initialize( self, input, values ):
        return self.initializeWith( Code( input ), Vector( values ) )
    
    def addValue( self, value ):
        return cc.BmCriterion_addValue( self._ccriterion, c_double(value) )

    def from_set(self, input, outputId ):
        inputCode= Code( input )
        cc.BmCriterion_from_set(
            self._ccriterion,
            inputCode._ccode,
            c_uint(outputId)
        )
        inputCode._cmaster= False
        return self
    