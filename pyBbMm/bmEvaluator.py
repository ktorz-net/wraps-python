from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibCore as cc
from .bmCode import Code

class Evaluator:
    # Construction destruction:
    def __init__(self, space=[2], numberOfCriteria=1, cevaluator= None):
        if cevaluator is None :
            codeSpace= Code( space )
            self._cevaluator= cc.newBmEvaluatorWith(
                codeSpace._ccode,
                c_uint( numberOfCriteria )
            )
            codeSpace._cmaster= False
            self._cmaster= True
        else: 
            self._cevaluator= cevaluator
            self._cmaster= False
    
    def __del__(self):
        if self._cmaster :
            cc.deleteBmEvaluator( self._cevaluator )
