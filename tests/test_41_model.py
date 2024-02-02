import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  M O D E L                     #
# ------------------------------------------------------------------------ #

import pyBbMm as bbmm

def test_BbMmModel_init():
    model= bbmm.Model()
    assert type(model) == bbmm.Model
    assert( model.variables() == [] )
    assert( model.domains() == [] )

def test_BbMmModel_init2():
    model= bbmm.Model(
        { "H": range(0, 3), "D": range(1, 7) },
        { "A": ["keep", "roll"] }
    )
    
    assert( model.variables() == [ "t0-H", "t0-D", "A" , "t1-H", "t1-D" ] )
    for dModel, dRef in zip( model.domains(), [range(0, 3), range(1, 7), ["keep", "roll"], range(0, 3), range(1, 7)] ) :
        assert( dModel == dRef )
    
    aNode= model.node('t0-H')
    assert( type(aNode) == bbmm.Node )
    assert( aNode.id() == 1 )
    assert( aNode.name() == 't0-H' )
    assert( aNode.domain() == range(0, 3) )
    assert( aNode.parents() == [] )
    assert( aNode.distribution() == [(0, 1.0)] )
    assert( model.node('A').distribution() == [("keep", 1.0)] )

def test_BbMmModel_construction():
    model= bbmm.Model(
        { "H": range(0, 3), "D": range(1, 7) },
        { "A": ["keep", "roll"] }
    )

    nodeD= model.node("t1-D")
    nodeD.initialize( ["A", "t0-D"], [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] )
    
    assert( nodeD.parents() == [ "A", "t0-D" ] )
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

    model.node( "t1-H" ).create( ["t0-H"], lambda config: [(min( config[0], 3 ), 1.0)] )
