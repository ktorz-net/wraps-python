from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibBbMm as cc
from .code import Code
from .bench import Bench
from .tree import Tree

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
    def range( self ):
        return cc.BmCondition_range( self._ccondition )
    
    def parentSpace( self ):
        return Code( ccode= cc.BmCondition_parents( self._ccondition ) )

    def fromCode( self, configuration ):
        return Bench( cbench=cc.BmCondition_from(
            self._ccondition,
            configuration._ccode )
        )
    
    def fromList( self, configurationList ):
        if len( configurationList ) == 0 :
            configurationList= [1]
        bench= self.fromCode( Code( configurationList ) )
        distrib= [ (output[0], value)
            for output, value in bench.asCodeValueList() ]
        return distrib

    def distributionSize( self ):
        return cc.BmCondition_distributionSize(self._ccondition)
    
    def distributionBenchAt( self, iDistribution ):
        return Bench(
            cbench= cc.BmCondition_distributionAt(
                self._ccondition,
                c_uint(iDistribution)
            )
        )
    def distributionAt( self, iDistribution ):
        bench= self.distributionBenchAt( iDistribution )
        distrib= [ (output[0], value)
            for output, value in bench.asCodeValueList() ]
        return distrib
    
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
    
    def addDistribution( self, distrib ):
        distribBench= Bench( [([int(output)], value) for output, value in distrib ] )
        iDistrib= cc.BmCondition_attach( self._ccondition, distribBench._cbench )
        distribBench._cmaster= False # Do not distroy the bench went distribDump will be distroyed. (aDistrib instance is not the master)
        return 

    # Dump & Load :
    def dump( self ):
        descriptor= {
            "range": self.range(),
            "selector": Tree( ctree= cc.BmCondition_selector( self._ccondition ) ).dump(),
            "distributions": [
                self.distributionAt(i)
                for i in range( 1, self.distributionSize()+1 )
            ]
        }
        return descriptor
    
    def load( self, descriptor ):

        # Re-initialize the intance:
        self.initialize( descriptor['range'], descriptor['selector']['input'], descriptor['distributions'][0] )
        
        # Generate all the distributions:
        for  distrib in descriptor['distributions'][1:]:
            self.addDistribution( distrib )
        
        # Generate the tree selector:
        Tree( ctree= cc.BmCondition_selector( self._ccondition ) ).load( descriptor['selector'] )
        
        return self