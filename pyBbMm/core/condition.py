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
        bench= self.fromCode( Code( configurationList ) )
        distrib= [ (output[0], value)
            for output, value in bench.asList() ]
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
    
    # Dump & Load :
    def dump( self ):
        descriptor= {
            "range": self.range(),
            "selector": Tree( ctree= cc.BmCondition_selector( self._ccondition ) ).dump(),
            "distributions": [
                self.distributionAt(i).dump()
                for i in range( 1, self.distributionSize()+1 )
            ]
        }
        return descriptor
    
    def load(self, descriptor):
        # Generate all the distributions:
        distribs= [
            Bench().load( distribDump )
            for distribDump in descriptor['distributions']
        ]
        
        # Re-initialize the intance:
        self.initializeWith(
            descriptor['range'],
            Code( descriptor['selector']['input'] ),
            distribs[0]
        )

        # Generate all the distributions:
        for distrib in distribs[1:] :
            cc.BmCondition_attach( self._ccondition, distrib._cbench )
            distrib._cmaster= False # Do not distroy the bench went distribDump will be distroyed. (aDistrib instance is not the master)
        
        
        # Generate the tree selector:
        Tree( ctree= cc.BmCondition_selector( self._ccondition ) ).load( descriptor['selector'] )
        
        return self