from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibCore as cc
from .bmCode import Code
from .bmBench import Bench

# BmBench wrap:
class Tree :
    # Construction destruction:
    def __init__(self, space=[1], optionSize=1, ctree= None):
        if ctree is None :
            codeSpace= Code( space )
            self._ctree= cc.newBmTreeWith( codeSpace._ccode, c_uint(optionSize) )
            codeSpace._cmaster= False
            self._cmaster= True
        else: 
            self._ctree= ctree
            self._cmaster= False
    
    def __del__(self):
        if self._cmaster :
            cc.deleteBmTree( self._ctree )

    # Accessor
    def outputSize(self):
        return cc.BmTree_outputSize( self._ctree )

    def atCode( self, code ):
        return cc.BmTree_at( self._ctree, code._ccode)
    
    def atCode_value( self, code ):
        return cc.BmTree_at_value( self._ctree, code._ccode)
    
    def at( self, codeList ):
        code= Code(codeList)
        return self.atCode( code )
    
    def at_value( self, codeList ):
        code= Code(codeList)
        return self.atCode_value( code )
    
    # Generating
    def asBench( self ):
        bench= Bench( cbench= cc.BmTree_asNewBench( self._ctree ) )
        bench._cmaster= True
        return bench

    # Construction
    def initialize( self, defaultOption ):
        cc.BmTree_reinitOn( self._ctree, c_uint(defaultOption) )
        return self

    def atCode_set( self, code, option ):
        cc.BmTree_at_set( self._ctree, code._ccode, c_uint(option) )

    def at_set( self, codeList, option ):
        return self.atCode_set( Code( codeList ), option )
