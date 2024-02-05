import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                 T E S T   p y B b M m  : :  V E C T O R                  #
# ------------------------------------------------------------------------ #

import pyBbMm as bm

def test_BbMmVector_init():
    vector= bm.Vector()
    assert vector.dimention() == 0

def test_BbMmVector_init2():
    vector= bm.Vector([1, 2, 3])
    assert vector.dimention() == 3
    assert vector.at(1) == 1
    assert vector.at(2) == 2
    assert vector.at(3) == 3
    assert vector.list() == [1, 2, 3]

def test_BbMmVector_copy():
    vector= bm.Vector([1, 2, 3])
    cpy= vector.copy()
    assert cpy.dimention() == 3
    assert cpy.at(1) == 1
    assert cpy.at(2) == 2
    assert cpy.at(3) == 3
    assert cpy.list() == [1, 2, 3]
    vector.initialize([3, 2])
    assert vector.list() == [3, 2]
    assert cpy.list() == [1, 2, 3]

def test_BbMmVector_compare():
    v1= bm.Vector([1.0, 42.0, 3.0])
    v2= bm.Vector([1.0, 42.0, 3.0])
    assert v1 == v2
    assert v1 <= v2
    assert v1 >= v2
    v2.initialize( [1.0, 43.0, 3.0] )
    assert v1 < v2
    assert v1 <= v2
    assert v2 > v1
    assert v2 >= v1
    assert v1 != v2

def test_BbMmVector_modify():
    vector= bm.Vector([1.0, 2.0, 3.0])
    assert vector.list() == [1.0, 2.0, 3.0]
    vector.resize(2)
    assert vector.list() == [1.0, 2.0]
    vector.resize(4)
    assert vector.list() == [1.0, 2.0, 0.0, 0.0]
    vector.at_set(1, 2.0)
    vector.at_set(4, 6.0)
    vector.at_set(2, 3.0)
    vector.at_set(3, 1.0)
    assert vector.list() == [2.0, 3.0, 1.0, 6.0]

def test_BbMmVector_dump():
    vect= bm.Vector([1.0, 2.1, 3.0])
    assert vect.dump() == [1.0, 2.1, 3.0]
    assert vect.dumpStr() == "[1.0, 2.1, 3.0]"

def test_BbMmVect_load():
    vect= bm.Vector().load( bm.Vector([1.0, 2.1, 3.0]).dump() )
    assert vect.dump() == [1.0, 2.1, 3.0]
    assert vect.dumpStr() == "[1.0, 2.1, 3.0]"

if __name__ == '__main__':
    test_BbMmVector_modify()
