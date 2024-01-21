from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibCore as cc
from .bmCode import Code
from .bmBench import Bench

class Condition:
    # Construction destruction:
    def __init__(self, domainSize=1, parentSpace=[1], defaultDistrib=[(1,1.0)], ccondition= None):
        if ccondition is None :
            codeParentSpace= Code( parentSpace )
            defaultDistrib= [ ([int(output)], value) for output, value in defaultDistrib ]
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

    # Accessor
    def domain( self ):
        return cc.BmCondition_domain( self._ccondition )
    
    def parentSpace( self ):
        return Code( ccode= cc.BmCondition_parents( self._ccondition ) )

    def fromCode( self, configuration ):
        return Bench( cbench=cc.BmCondition_from(
            self._ccondition,
            configuration._ccode )
        )
    
    def fromList( self, configurationList ):
        bench= self.fromCode( Code( configurationList ) )
        distrib= [ (output[0], value)
            for output, value in bench.list() ]
        return distrib

    def distributionSize( self ):
        return cc.BmCondition_distributionSize(self._ccondition)
    
    def distributionAt( self, iDistribution ):
        return Bench(
            cbench= cc.BmCondition_distributionAt(
                self._ccondition,
                c_uint(iDistribution)
            )
        )
    
    # Construction
    def initializeWith( self, domain, parentSpace, defaultDistrib ):
        assert( parentSpace._cmaster and defaultDistrib._cmaster )
        parentSpace._cmaster= False
        defaultDistrib._cmaster= False
        return cc.BmCondition_reinitWith(
            self._ccondition,
            c_uint(domain),
            parentSpace._ccode,
            defaultDistrib._cbench
        )
    
    def initialize( self, domain, parentSpaceList, defaultDistribList ):
        return self.initializeWith( domain,
            Code( parentSpaceList ),
            Bench( [ ([o], v) for o, v in defaultDistribList] )
        )

    def fromCode_set( self, configuration, distribution ):
        assert( configuration._cmaster and distribution._cmaster )
        configuration._cmaster= False
        distribution._cmaster= False
        return cc.BmCondition_from_attach(
            self._ccondition,
            configuration._ccode,
            distribution._cbench
        )
    
    def fromList_set( self, configList, distribList ):
        configuration= Code( configList )
        distribution= Bench( [([int(output)], value) for output, value in distribList ] )
        return self.fromCode_set(configuration, distribution)
    