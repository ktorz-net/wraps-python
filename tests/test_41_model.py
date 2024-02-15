import sys
from pprint import pprint
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  M O D E L                     #
# ------------------------------------------------------------------------ #

from pyBbMm import Model, Node
import json

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
    
    assert list( buffer.keys() ) == [ 'H-0', 'D-0', 'A', 'H-1', 'D-1', 'rewards' ]

    assert buffer['H-0'] == {
      "domain": [0, 1, 2],
      "parents": [],
      "condition": {
        "range": 3,
        "selector": { "input": [1], "branches": [] },
        "distributions": [ [ ([1], 1.0) ] ]
      }
    }
    
    assert buffer['D-0'] == {
      "domain": [1, 2, 3, 4, 5, 6],
      "parents": [],
      "condition": {
        "range": 6,
        "selector": { "input": [1], "branches": [] },
        "distributions": [ [ ([1], 1.0) ] ]
      }
    }
    
    assert buffer['A'] == {
      "domain": ["keep", "roll"],
      "parents": [],
      "condition": {
        "range": 2,
        "selector": { "input": [1], "branches": [] },
        "distributions": [ [ ([1], 1.0) ] ]
      }
    }

    assert buffer['H-1'] == {
      'domain': [0, 1, 2],
      'parents': ['H-0'],
      'condition': {
        'distributions': [[([1], 1.0)], [([1], 1.0)], [([1], 1.0)], [([2], 1.0)]],
        'range': 3,
        'selector': {
          'input': [3],
          'branches': [
            {'child': 0, 'iInput': 1, 'states': [('leaf', 2), ('leaf', 3), ('leaf', 4)]}
          ]
        }
      }
    }

    pprint( buffer['D-1'] )
    
    assert buffer['D-1'] == {
      'domain': [1, 2, 3, 4, 5, 6],
      'parents': ["A", "D-0"],
      'condition': {
        'distributions': [
          [([1], 0.16666666666666666), ([2], 0.16666666666666666), ([3], 0.16666666666666666), ([4], 0.16666666666666666), ([5], 0.16666666666666666), ([6], 0.16666666666666666)],
          [([1], 1.0)],
          [([2], 1.0)],
          [([3], 1.0)],
          [([4], 1.0)],
          [([5], 1.0)],
          [([6], 1.0)]
        ],
        'range': 6,
        'selector': {
          'input': [2, 6],
          'branches': [
            { 'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 1)] },
            {'child': 1, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 3), ('leaf', 4), ('leaf', 5), ('leaf', 6), ('leaf', 7)]}
          ]
        }
      }
    }

def test_BbMmModel_construction_reward():
  pass

def test_BbMmModel_transition():
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

    print( "---" )
    print( model._trans.processFrom( [2, 5, 1] ) )
    print( "---" )
    print( model.digitTransition( [2, 5], [2] ) )
    print( "---" )

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

if __name__ == "__main__" :
    test_BbMmModel_init2()