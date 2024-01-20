from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibCore as cc
from .bmCode import Code
from .bmBench import Bench

class Condition:
    # Construction destruction:
    def __init__(self, domainSize=1, parentSpace=[1], defaultDistrib=[([1],1.0)], ccondition= None):
        if ccondition is None :
            codeParentSpace= Code( parentSpace )
            benchDefaultDistrib= Bench( defaultDistrib )
            self._ccondition= cc.newBmConditionWith(
                c_uint(domainSize),
                codeParentSpace._ccode,
                benchDefaultDistrib._cbench
            )
            codeParentSpace._cmaster= False
            benchDefaultDistrib._cmaster= False
            self._cmaster= True
        else: 
            self._ccondition= ccondition
            self._cmaster= False
    
    def __del__(self):
        if self._cmaster :
            cc.deleteBmCondition( self._ccondition )
