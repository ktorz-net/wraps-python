import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  M O D E L                     #
# ------------------------------------------------------------------------ #

from pyBbMm import Model, Node
import json

buffer= None

def test_BbMmModel_init():
    model= Model()
    assert type(model) == Model
    assert( model.variables() == [] )
    assert( model.domains() == [] )

def test_BbMmModel_init2():
    model= Model(
        { "H": range(0, 3), "D": range(1, 7) },
        { "A": ["keep", "roll"] }
    )
    
    assert( model.variables() == [ "H-0", "D-0", "A" , "H-1", "D-1" ] )
    for dModel, dRef in zip( model.domains(), [range(0, 3), range(1, 7), ["keep", "roll"], range(0, 3), range(1, 7)] ) :
        assert( dModel == dRef )
    
    aNode= model.node('H-0')
    assert( type(aNode) == Node )
    assert( aNode.id() == 1 )
    assert( aNode.name() == 'H-0' )
    assert( aNode.domain() == range(0, 3) )
    assert( aNode.parents() == [] )
    assert( aNode.distribution() == [(0, 1.0)] )
    assert( model.node('A').distribution() == [("keep", 1.0)] )

    nodeA= model.node("A")
    assert( nodeA.domain() == ["keep", "roll"] )
    assert( nodeA.index("keep") == 1 )
    assert( nodeA.value(2) == "roll" )

def test_BbMmModel_construction_transition():
    global buffer
    model= Model(
        { "H": range(0, 3), "D": range(1, 7) },
        { "A": ["keep", "roll"] }
    )

    nodeD= model.node("D-1")
    nodeD.initialize( ["A", "D-0"], [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] )
    
    assert( nodeD.parents() == [ "A", "D-0" ] )
    assert( nodeD.distribution( ["roll", 1] ) == [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] )
    assert( nodeD.distribution( ["keep", 5] ) == [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] )

    nodeD.setConditionalDistribution( ["keep", 1], [(1, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 2], [(2, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 3], [(3, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 4], [(4, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 5], [(5, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 6], [(6, 1.0)] )
    
    assert( nodeD.distribution( ["roll", 1] ) == [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] )
    assert( nodeD.distribution( ["keep", 5] ) == [(5, 1.0)]  )

    assert( [ model._varIds[p] for p in ["H-0"] ] == [1] )
    
    nodeH= model.node( "H-1" )
    nodeH.create( ["H-0"], lambda config: [(max( config[0]-1, 0 ), 1.0)] )
    
    assert( nodeH.distribution( [0] ) == [(0, 1.0)]  )
    assert( nodeH.distribution( [2] ) == [(1, 1.0)]  )

    assert( model.digit( [1, 5, "roll"] ) == [2, 5, 2] )
    
    buffer= model.dump()
    print( json.dumps( buffer, indent=2 ) )
    assert buffer == {
  "H-0": {
    "domain": [0, 1, 2],
    "parents": [],
    "condition": {
      "input": [1],
      "output": 3,
      "distributions": []
    }
  },
  "D-0": {
    "domain": [1, 2, 3, 4, 5, 6],
    "parents": [],
    "condition": {
      "input": [1],
      "output": 6,
      "distributions": []
    }
  },
  "A": {
    "domain": ["keep", "roll"],
    "parents": [],
    "condition": {
      "input": [1],
      "output": 2,
      "distributions": []
    }
  },
  "H-1": {
    "domain": [0, 1, 2 ],
    "parents": ["H-0"],
    "condition": {
      "input": [3],
      "output": 3,
      "distributions": []
    }
  },
  "D-1": {
    "domain": [1, 2, 3, 4, 5, 6],
    "parents": ["A", "D-0"],
    "condition": {
      "input": [2, 6],
      "output": 6,
      "distributions": []
    }
  }
}

def ttest_BbMmModel_transition():
    global buffer
    model= Model()
    ### model.load( buffer )
    model= Model(
        { "H": range(0, 3), "D": range(1, 7) },
        { "A": ["keep", "roll"] }
    )

    nodeD= model.node("D-1")
    nodeD.initialize( ["A", "D-0"], [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] )

    nodeD.setConditionalDistribution( ["keep", 1], [(1, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 2], [(2, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 3], [(3, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 4], [(4, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 5], [(5, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 6], [(6, 1.0)] )

    model.node( "H-1" ).create( ["H-0"], lambda config: [(max( config[0]-1, 0 ), 1.0)] )

    ###
    print( model.digitTransition( [2, 5], [2] ) )
    
    assert( model.digitTransition( [2, 5], [1] ) == [
        ([1, 1], 1/6),
        ([1, 2], 1/6),
        ([1, 3], 1/6),
        ([1, 4], 1/6),
        ([1, 5], 1/6),
        ([1, 6], 1/6),
    ])

    assert( model.transition( [1, 5], ["roll"] ) == [
        ([0, 1], 1/6),
        ([0, 2], 1/6),
        ([0, 3], 1/6),
        ([0, 4], 1/6),
        ([0, 5], 1/6),
        ([0, 6], 1/6),
    ])

def test_BbMmModel_construction_reward():
    pass
