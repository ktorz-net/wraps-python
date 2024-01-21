from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibCore as cc
from .bmCode import Code
from .bmVector import Vector
from .bmTree import Tree

class Evaluator:
    # Construction destruction:
    def __init__(self, inputSpace=[2], numberOfCriteria=1, cevaluator= None):
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
    def inputSpace( self ):
        return Code( ccode= cc.BmEvaluator_space( self._cevaluator ) )
    
    def numberOfCriteria( self ):
        return cc.BmEvaluator_numberOfCriteria( self._cevaluator )
    
    def criteria( self, iCrit ):
        return Tree( ctree= cc.BmEvaluator_crit(
            self._cevaluator,
            c_uint(iCrit) )
        )
    
    def weights( self ):
        return Vector(
            cvector= cc.BmEvaluator_weights( self._cevaluator )
        )
    
    def criteriaWeight( self, iCrit ):
        return cc.BmEvaluator_crit_weight(
            self._cevaluator,
            c_uint(iCrit)
        )
    
