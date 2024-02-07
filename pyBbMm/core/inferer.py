from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibBbMm as cc
from .code import Code
from .bench import Bench
from .condition import Condition

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

    def node(self, iVar):
        return Condition( ccondition= cc.BmInferer_node(
            self._cinferer, c_uint(iVar) )
        )
    
    def parents( self, iVar ):
        return Code( ccode=cc.BmInferer_node_parents(
            self._cinferer, c_uint(iVar) )
        )
    
    # Construction :
    def variable_setDependancyBm( self, iVar, parents, defaultDistrib ):
        assert( parents._cmaster and defaultDistrib._cmaster )
        parents._cmaster= False
        defaultDistrib._cmaster= False
        return Condition( ccondition= cc.BmInferer_node_reinitWith(
            self._cinferer,
            c_uint(iVar),
            parents._ccode,
            defaultDistrib._cbench )
        )
    
    def variable_setDependancy( self, iVar, parentList, defaultDistribList ):
        return self.variable_setDependancyBm(
            iVar,
            Code( parentList ),
            Bench( [ ([o], v) for o, v in defaultDistribList ] )
        )
    
    # Processing
    def processBench( self, inputDistribution ):
        cc.BmInferer_process(
            self._cinferer,
            inputDistribution._cbench
        )
        return self.distribution()
    
    def processFrom( self, inputList ):
        return self.processBench( Bench( [(inputList, 1.0)] ) )
