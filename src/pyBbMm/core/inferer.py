from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clib, clibBbMm as cc
from .code import Code
from .bench import Bench
from .tree import Tree
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
        return Bench( cbench= cc.BmInferer_distribution( self._cinferer ) )

    def inputDimention( self ):
        return cc.BmInferer_inputDimention( self._cinferer )
    
    def outputDimention( self ):
        return cc.BmInferer_outputDimention( self._cinferer )

    def shiftDimention( self ):
        return cc.BmInferer_shiftDimention( self._cinferer )
    
    def stateDimention( self ):
        return cc.BmInferer_outputDimention( self._cinferer )
    
    def actionDimention( self ):
        return cc.BmInferer_inputDimention( self._cinferer ) - cc.BmInferer_outputDimention( self._cinferer )

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
    def space( self ):
        return [ cc.BmInferer_node_size( self._cinferer, c_uint(i) ) for i in range( 1, self.inputDimention()+1 ) ]
    
    def inputs( self ):
        inputBound= self.inputDimention()+1
        return [ cc.BmInferer_node_size( self._cinferer, c_uint(i) ) for i in range( 1, inputBound ) ]
    
    def outputs( self ):
        overBound= self.overallDimention()+1
        outputStart= overBound - self.outputDimention()
        return [ cc.BmInferer_node_size( self._cinferer, c_uint(i) ) for i in range( outputStart, overBound ) ]
    
    def shifts( self ):
        inputBound= self.inputDimention()+1
        shiftBound= inputBound + self.shiftDimention()
        return [ cc.BmInferer_node_size( self._cinferer, c_uint(i) ) for i in range( inputBound, shiftBound ) ]
    
    # Construction :
    def initialize( self, inputs, outputs, shifts= [] ):
        spaceCode= Code( inputs+shifts+outputs )
        cc.BmInferer_destroy( self._cinferer )
        cc.BmInferer_create(
            self._cinferer,
            spaceCode._ccode,
            c_uint( len(inputs) ), c_uint( len(outputs) )
        )
        return self
    
    def node_setDependancyBm( self, iVar, parents, defaultDistrib ):
        assert( parents._cmaster and defaultDistrib._cmaster )
        assert( parents.dimention() > 0 )
        ccond= cc.BmInferer_node_reinitWith_withDefault(
            self._cinferer,
            c_uint(iVar),
            parents._ccode,
            defaultDistrib._cbench
        )
        parents._cmaster= False
        defaultDistrib._cmaster= False
        return Condition( ccondition= ccond )
         
    
    def node_setDependancy( self, iVar, parentList, defaultDistribList ):
        return self.node_setDependancyBm(
            iVar,
            Code( parentList ),
            Bench( [ ([o], [v]) for o, v in defaultDistribList ] )
        )
    
    # Processing
    def processBench( self, inputDistribution ):
        cc.BmInferer_process(
            self._cinferer,
            inputDistribution._cbench
        )
        distrib= self.distribution()
        return distrib
    
    def processFrom( self, inputList ):
        return self.processBench( Bench( [(inputList, 1.0)] ) )

    # Dump & Load
    def dump( self ):
        size= self.overallDimention()
        dumpNodes= []
        for i in range(1, size+1) :
            condDump= self.node(i).dump()
            dumpNodes.append({
                'nodeId': i,
                'parents': Code( ccode= cc.BmInferer_node_parents( self._cinferer, c_uint(i) ) ).asList(),
                'distributions': condDump['distributions'],
                'selector': condDump['selector']
            })
        return { 
            'inputs': self.inputs(),
            'outputs': self.outputs(),
            'shifts': self.shifts(),
            'nodes': dumpNodes
        }

    def load( self, dump ):
        self.initialize( dump['inputs'], dump['outputs'], dump['shifts'] )
        for nodeDump in dump['nodes'] :
            if len(nodeDump['parents']) > 0 :
                condition= self.node_setDependancy( 
                    nodeDump['nodeId'],
                    nodeDump['parents'],
                    nodeDump['distributions'][0]
                )
                # Generate all the distributions:
                for  distrib in nodeDump['distributions'][1:]:
                    condition.addDistribution( distrib )
                        
                # Generate the tree selector:
                Tree( ctree= cc.BmCondition_selector( condition._ccondition ) ).load( nodeDump['selector'] )
        return self
