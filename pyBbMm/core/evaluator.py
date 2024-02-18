from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibBbMm as cc
from .code import Code
from .vector import Vector
from .tree import Tree
from .criterion import Criterion

class Evaluator:
    # Construction destruction:
    def __init__(self, inputSpace=[1], numberOfCriteria=1, cevaluator= None):
        if cevaluator is None :
            inputCode= Code( inputSpace )
            self._cevaluator= cc.newBmEvaluatorWith(
                inputCode._ccode,
                c_uint( numberOfCriteria )
            )
            inputCode._cmaster= False
            self._cmaster= True
        else: 
            self._cevaluator= cevaluator
            self._cmaster= False
    
    def __del__(self):
        if self._cmaster :
            cc.deleteBmEvaluator( self._cevaluator )

    # Accessor
    def inputRanges( self ):
        return Code( ccode= cc.BmEvaluator_space( self._cevaluator ) ).asList()
    
    def numberOfCriteria( self ):
        return cc.BmEvaluator_numberOfCriteria( self._cevaluator )
    
    def weights( self ):
        return Vector(
            cvector= cc.BmEvaluator_weights( self._cevaluator )
        ).asList()
    
    def weight( self, iCrit ):
        return cc.BmEvaluator_criterion_weight( self._cevaluator, c_uint(iCrit) )
    
    def criterion( self, iCrit ):
        return Criterion( ccriterion=cc.BmEvaluator_criterion(
            self._cevaluator,
            c_uint(iCrit)
        ) )

    def criterionWeight( self, iCrit ):
        return cc.BmEvaluator_criterion_weight(
            self._cevaluator,
            c_uint(iCrit)
        )

    def criterionMask( self, iCrit ):
        return Code( ccode=cc.BmEvaluator_criterion_mask(
            self._cevaluator,
            c_uint(iCrit) )
        ).asList()

    # Construction
    def criterion_intializeWith( self, iCrit, codeDependence, vectorValues ):
        assert( codeDependence._cmaster ) # free to attach...
        assert( vectorValues._cmaster ) # free to attach...
        cc.BmEvaluator_criterion_reinitWith(
            self._cevaluator,
            c_uint( iCrit ),
            codeDependence._ccode,
            vectorValues._cvector
        )
        codeDependence._cmaster= False
        vectorValues._cmaster= False
        return self.criterion( iCrit )
    
    def criterion_intialize( self, iCrit, dependenceList, possibleValues ):
        return self.criterion_intializeWith(
            iCrit,
            Code( dependenceList ),
            Vector( possibleValues )
        )

    def criterion_setWeight( self, iCrit, weight ):
        cc.BmEvaluator_criterion_setWeight(
            self._cevaluator, c_uint(iCrit), c_double(weight)
        )
        return self
    
    # Process
    def processMulti( self, input ):
        inputCode= Code( input )
        values= []
        for iCrit in range( 1, self.numberOfCriteria()+1 ) :
            values.append( cc.BmEvaluator_criterion_process( self._cevaluator, c_uint(iCrit), inputCode._ccode ) )
        return values

    def processCode( self, input ):
        return cc.BmEvaluator_process( self._cevaluator, input._ccode )
    
    def process( self, inputList ):
        return self.processCode( Code(inputList) )
    