from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibCore as cc
from .bmCode import Code
from .bmBench import Bench

class Inferer:
    # Construction destruction:
    def __init__(self, space=[2, 2], inputDimention=1, outputDimention=1, cinferer= None):
        if cinferer is None :
            codeSpace= Code( space )
            self._cinferer= cc.newBmInferer(
                     codeSpace._ccode,
                     c_uint(inputDimention),
                     c_uint(outputDimention)
            )
            codeSpace._cmaster= False
            self._cmaster= True
        else: 
            self._cinferer= cinferer
            self._cmaster= False

    def __del__(self):
        if self._cmaster :
            cc.deleteBmInferer( self._cinferer )

    # Accessor
    def distribution( self ):
        return Bench( cbench= cc.BmInferer_distribution(
            self._cinferer )
        )

    def inputDimention( self ):
        return cc.BmInferer_inputDimention( self._cinferer )
    
    def outputDimention( self ):
        return cc.BmInferer_outputDimention( self._cinferer )
    
    def shiftDimention( self ):
        return cc.BmInferer_shiftDimention( self._cinferer )
    
    def overallDimention( self ):
        return cc.BmInferer_overallDimention( self._cinferer )
