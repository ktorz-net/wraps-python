#!env python3
"""
Script MDP 421 
"""

import pyBbMm as bbmm


# Initialize Domains:
diceDomain= range(1,7)
horizonDomain= range( 3 )
actionDomain= ["roll", "keep"]

# Initialize model with the variables:
model= bbmm.Model(
    stateVariables= {
        "H": horizonDomain,
        "D1": diceDomain,
        "D2": diceDomain,
        "D3": diceDomain
    },

    actionVariables= {
        "A1": actionDomain,
        "A2": actionDomain,
        "A3": actionDomain
    },

    shiftVariables= {
        "ID1": actionDomain,
        "ID2": actionDomain,
        "ID3": actionDomain
    }
)

exit()

# Initialize model with the variables:


for i in range(1, 4) :
    si= str(i)
    model.node("ID"+si).initialize( ["t0-D"+si, "A"+si], "A"+si, [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] )
    model.node("ID"+si).addConditionalDistribution( [1, "keep"], [(1, 1.0)] )
    model.node("ID"+si).addConditionalDistribution( [2, "keep"], [(2, 1.0)] )
    model.node("ID"+si).addConditionalDistribution( [3, "keep"], [(3, 1.0)] )
    model.node("ID"+si).addConditionalDistribution( [4, "keep"], [(4, 1.0)] )
    model.node("ID"+si).addConditionalDistribution( [5, "keep"], [(5, 1.0)] )
    model.node("ID"+si).addConditionalDistribution( [6, "keep"], [(6, 1.0)] )

model.node("t1-D1").initialize( ["ID1", "ID2", "ID3"], "ID1", [(1, 1.0)] )
model.node("t1-D2").initialize( ["ID1", "ID2", "ID3"], "ID2", [(1, 1.0)] )
model.node("t1-D3").initialize( ["ID1", "ID2", "ID3"], "ID3", [(1, 1.0)] )


import wanda as wd
import random

# Default game interface :
def main():
    game= Engine()
    print( game.dynamic.stateVariableNames() )
    print( game.dynamic.actionVariableNames() )
    print( game.dynamic.variableNames() )
    print( game.dynamic.network() )
    print( game.dynamic.dependency("ID1") )

# Game engine :
class Engine :

    def __init__( self, horizon=3 ):
        self.horizon= horizon
        # Initialize Domains:
        diceDomain= range(1,7)
        actionDomain= ["roll", "keep"]
        # Initialize Variables:
        stateVariable= {
            "H": range( self.horizon ),
            "D1": diceDomain,
            "D2": diceDomain,
            "D3": diceDomain
        }
        actionVariable= {
            "A1": actionDomain,
            "A2": actionDomain,
            "A3": actionDomain
        }
        intermediateVariable= {
            "ID1": actionDomain,
            "ID2": actionDomain,
            "ID3": actionDomain
        }
        self.dynamic= wd.Dynamic(stateVariable, actionVariable, intermediateVariable)
        # Set dependecy:
        self.dynamic.setDependencyFromFunction( "ID1", ["D1", "A1"], self.rollDependence )

        # Initialize state:
        self.initialize()
        
    def initialize(self, numberOfPlayers=1):
        self.state= [self.horizon-1, 1, 1, 1]

    # Node Dependances:
    def rollDependence( self, parents ):
        print( "Test: "+ str(parents) )
        if parents[1] == "roll" :
            return { 1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6 }
        else :
            return { parents[0]: 1.0 }

# Activate default interface :
if __name__ == '__main__':
    main()