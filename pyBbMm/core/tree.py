from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibBbMm as cc
from .code import Code
from .bench import Bench

# BmTree wrap:
class Tree :
    # Construction destruction:
    def __init__(self, space=[1], ctree= None):
        if ctree is None :
            codeSpace= Code( space )
            self._ctree= cc.newBmTreeWith( codeSpace._ccode )
            codeSpace._cmaster= False
            self._cmaster= True
        else: 
            self._ctree= ctree
            self._cmaster= False
    
    def __del__(self):
        if self._cmaster :
            cc.deleteBmTree( self._ctree )

    # Accessor
    def size(self):
        return cc.BmTree_size( self._ctree )
    
    def inputs(self):
        return Code( ccode=cc.BmTree_inputRanges( self._ctree ) ).asList()
    
    def atCode( self, code ):
        return cc.BmTree_at( self._ctree, code._ccode)
    
    def at( self, codeList ):
        code= Code(codeList)
        return self.atCode( code )

    # Generating
    def asBench( self ):
        bench= Bench( cbench= cc.BmTree_asNewBench( self._ctree ) )
        bench._cmaster= True
        return bench

    # Construction
    def initialize( self, inputRanges ):
        codeSpace= Code( inputRanges )
        self._ctree= cc.BmTree_reinitWith(
            self._ctree,
            codeSpace._ccode
        )
        codeSpace._cmaster= False
        return self
    
    def clear( self, defaultOutput=1, iInput=1 ):
        cc.BmTree_clearWhith_on( self._ctree, c_uint(iInput), c_uint(defaultOutput) )

    def atCode_set( self, code, option ):
        cc.BmTree_at_set( self._ctree, code._ccode, c_uint(option) )

    def at_set( self, codeList, option ):
        return self.atCode_set( Code( codeList ), option )

    def option_setValue( self, iOption, value ):
        cc.BmTree_option_setValue(
            self._ctree,
            c_uint(iOption),
            c_double(value)
        )
    
    # branch manipulation
    def iBranch_variable(self, iBranch):
        return cc.BmTree_branchVariable( self._ctree, c_uint(iBranch) )

    def iBranch_size(self, iBranch):
        return cc.BmTree_branchSize( self._ctree, c_uint(iBranch) )

    def iBranch_state(self, iBranch, index):
        key= cc.BmTree_branch_state( self._ctree, c_uint(iBranch), c_uint(index) )
        leaf= cc.BmTreeLeaf(key)
        if leaf > 0 :
            return ( "leaf", leaf )
        return ( "child", cc.BmTreeChild(key) )

    def iBranch_states(self, iBranch):
        return [
            self.iBranch_state( iBranch, i+1 )
            for i in range( self.iBranch_size(iBranch) )
        ]
    
    # dump and load:
    def dump(self):
        descriptor= {
            "input": self.inputs(),
            "branches": [
                { "child": i, "iInput": self.iBranch_variable(i), "states": self.iBranch_states(i) }
                for i in range( self.size() )
            ]
        }
        return descriptor
    
    def load(self, descriptor):
        self.initialize( descriptor["input"] )
        iBranch= 0
        for bDes in descriptor["branches"] :
            r= cc.BmTree_newBranch_on( self._ctree, c_uint( bDes["iInput"] ), c_uint(1))
            assert( int(r) == iBranch )
            index= 1
            for sType, sValue in bDes["states"] :
                if sType == 'leaf' :
                    cc.BmTree_branch_state_set( self._ctree, r, c_uint(index), c_uint(sValue) )
                else :
                    cc.BmTree_branch_state_connect( self._ctree, r, c_uint(index), c_uint(sValue) )
                index+= 1
            iBranch+= 1
        return self
