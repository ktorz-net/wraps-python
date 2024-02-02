# Core LibBbMm Wraps:

## LibBbMm :: STRUCTURE MODULE :
from . import bmCode, bmVector, bmBench, bmTree
Code= bmCode.Code
Vector= bmVector.Vector
Bench= bmBench.Bench
Tree= bmTree.Tree

## LibBbMm :: FUNCTION MODULE :
from . import bmCondition, bmInferer, bmEvaluator
Condition= bmCondition.Condition
Inferer= bmInferer.Inferer
Evaluator= bmEvaluator.Evaluator

## LibBbMm :: SOLVER MODULE :

## User friendly API :

### Model Node (A node in a Dynamic Bayesian Network)
class Node():
    # Construction destruction:
    def __init__( self, model= None, iVar=0 ) -> None:
        self._model= model
        self._id= iVar
    
    # Accessor:
    def id(self):
        return self._id
    
    def name(self):
        return self._model._varNames[ self._id-1 ]

    def domain(self):
        return self._model._domains[ self._id-1 ]

    def parents(self):
        idParents= self._model._trans.parents( self._id ).list()
        return [ self._model._varNames[ ip-1 ] for ip in idParents ]

    def distribution( self, configuration=[] ):
        return self._model.inode_distribution( self._id, configuration )
    
    # Construction:
    def initialize( self, parents, defaultDistrib ):
        return self._model.inode_initialize( self._id, parents, defaultDistrib )
    
    def setConditionalDistribution( self, configuration, distribution ):
        return self._model.inode_setConditionalDistribution( self._id, configuration, distribution )

class Model():
    # Construction destruction:
    def __init__( self, stateVariables= {}, actionVariables= {}, shiftVariables= {} ) -> None:
        # Initialize variable enumeration :
        self._varNames= [ 't0-'+var for var in stateVariables ]
        self._varNames+= [ var for var in actionVariables ]
        self._varNames+= [ var for var in shiftVariables ]
        self._varNames+= [ 't1-'+var for var in stateVariables ]
        nbVariable= len(self._varNames)
        self._varIds= { name: i for name, i in zip( self._varNames, range(1, nbVariable+1) ) }
        
        # List Domains :
        self._domains= list(stateVariables.values()) + list(actionVariables.values()) + list(shiftVariables.values()) + list(stateVariables.values())

        # Transition function:
        nbStateVar= len(stateVariables)
        nbActVar= len(actionVariables)
        self._trans= Inferer( [len(d) for d in self._domains ], nbStateVar+nbActVar, nbStateVar )

    # Accessor
    def variables(self):
        return self._varNames

    def domains(self):
        return self._domains

    def node( self, variableName ):
        return Node( self, self._varIds[variableName] )
    
    # Construction:
    def inode_initialize( self, iNode, parents, defaultExplicitDistrib ):
        domain= self._domains[ iNode-1 ]
        parentsIds= [ self._varIds[p] for p in parents ]
        defaultDigitDistrib= [ (domain.index(val)+1, proba) for val, proba in defaultExplicitDistrib ]

        self._trans.variable_setDependancy( iNode, parentsIds, defaultDigitDistrib )
    
    def inode_distribution( self, iNode, configuration ):
        idParents= self._trans.parents( iNode ).list()
        condition= self._trans.node( iNode )
        digitConf= [ self._domains[p-1].index(val)+1 for p, val in zip(idParents, configuration) ]
        domain= self._domains[ iNode-1 ]
        return [ (domain[id-1], proba) for id, proba in condition.fromList( digitConf ) ]
    
    def inode_setConditionalDistribution( self, iNode, configuration, distribution ):
        condition= self._trans.node( iNode )
        idParents= self._trans.parents( iNode ).list()
        digitConf= [ self._domains[p-1].index(val)+1 for p, val in zip(idParents, configuration) ]
        domain= self._domains[ iNode-1 ]
        digitDistrib= [ (domain.index(val)+1, proba) for val, proba in distribution ]
        condition.fromList_set( digitConf, digitDistrib )
