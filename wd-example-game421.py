#!env python3
"""
Script MDP 421 
"""
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