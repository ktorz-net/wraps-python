#!env python3
"""
Script MDP CofeeRobot

example from : Craig Boutilier, Richard Dearden, Moisés Goldszmidt - Stochastic dynamic programming with factored representations - 2000
"""

import wanda as wd
import random

# Default game interface :
def main():
    game= Engine()
    print( game.dynamic )
    print( game.dynamic.node("location'").conditionalDistributionDico() )

# Game engine :
class Engine :

    def __init__( self, horizon=3 ):
        self.horizon= horizon

        # Initialize Domains:
        booleanDomain= ["F", "T"]

        # Initialize Variables:
        stateVariable= {
            "location": ["office", "cafe"],
            "wet": booleanDomain,
            "umbrella": booleanDomain,
            "raining": booleanDomain,
            "robotCofee": booleanDomain,
            "ownerCofee": booleanDomain
        }
        self.state= ["office", "F", "F", "F", "F", "F"]
        actionVariable= { "action": ["move", "buyCofee", "giveCofee", "getUmbrella"] }

        self.dynamic= wd.Dynamic(stateVariable, actionVariable)

        # Location and action: move:
        self.dynamic.node("location'").setParents( ["location", "action"] )
        for l, a in self.dynamic.node("location'").parentSpace().tuples() :
            if a == 'move' and l == 'office'  :
                self.dynamic.node("location'").setDistribution( [l, a], { 'cafe' : 1 } )
            if a == 'move' and l == 'cafe'  :
                self.dynamic.node("location'").setDistribution( [l, a], { 'office' : 1 } )
            else :
                self.dynamic.node("location'").setDistribution( [l, a], { l : 1 } )

# Activate default interface :
if __name__ == '__main__':
    main()