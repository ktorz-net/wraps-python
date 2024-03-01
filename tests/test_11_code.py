import sys
sys.path.insert( 1, __file__.split('tests')[0] )
# ------------------------------------------------------------------------ #
#                 T E S T   p y B b M m  : :  C O D E                      #
# ------------------------------------------------------------------------ #
import pyBbMm.core as bm

def test_BbMmCode_init():
    code= bm.Code()
    assert str(code) == "code[]"
    assert code.dimention() == 0

def test_BbMmCode_init2():
    code= bm.Code([1, 2, 3])
    assert code.dimention() == 3
    assert code.digit(1) == 1
    assert code.digit(2) == 2
    assert code.digit(3) == 3
    assert str(code) == "code[1, 2, 3]"
    assert code.asList() == [1, 2, 3]

def test_BbMmCode_copy():
    code= bm.Code([1, 2, 3])
    cpy= code.copy()
    assert cpy.dimention() == 3
    assert cpy.digit(1) == 1
    assert cpy.digit(2) == 2
    assert cpy.digit(3) == 3
    assert cpy.asList() == [1, 2, 3]
    code.initialize([3, 2])
    assert code.asList() == [3, 2]
    assert cpy.asList() == [1, 2, 3]

def test_BbMmCode_compare():
    code1= bm.Code([1, 42, 3])
    code2= bm.Code([1, 42, 3])
    assert code1 == code2
    assert code1 <= code2
    assert code1 >= code2
    code2.initialize( [1, 43, 3] )
    assert code1 < code2
    assert code1 <= code2
    assert code2 > code1
    assert code2 >= code1
    assert code1 != code2

def test_BbMmCode_modify():
    code= bm.Code([1, 2, 3])
    assert code.asList() == [1, 2, 3]
    code.resize(2)
    assert code.asList() == [1, 2]
    code.resize(4)
    assert code.asList() == [1, 2, 0, 0]
    code.at_set(1, 2)
    code.at_set(4, 6)
    code.at_set(2, 3)
    code.at_set(3, 1)
    assert code.asList() == [2, 3, 1, 6]

def test_BbMmCode_iterate():
    code= bm.Code([2, 3, 2])
    iCode= iter(code)
    assert next(iCode) == [1, 1, 1]
    assert next(iCode) == [2, 1, 1]
    assert next(iCode) == [1, 2, 1]
    assert next(iCode) == [2, 2, 1]
    assert next(iCode) == [1, 3, 1]
    assert next(iCode) == [2, 3, 1]
    assert next(iCode) == [1, 1, 2]
    assert next(iCode) == [2, 1, 2]
    assert next(iCode) == [1, 2, 2]
    assert next(iCode) == [2, 2, 2]
    assert next(iCode) == [1, 3, 2]
    assert next(iCode) == [2, 3, 2]
    count= 0
    for lst in iter(code) :
        count+= 1
    assert count == 2*3*2
    count= 0
    for lst in code :
        count+= 1
    assert count == 2*3*2

def test_BbMmCode_print():
    assert str( bm.Code([1, 2, 3]) ) == "code[1, 2, 3]"


def test_BbMmCode_dump():
    code= bm.Code([1, 2, 3])
    assert code.dump() == [1, 2, 3]

def test_BbMmCode_load():
    code= bm.Code().load( bm.Code([1, 2, 3]).dump() )
    assert code.dump() == [1, 2, 3]

def test_BbMmCode_print():
    assert str( bm.Code([1, 2, 3]) ) == "code[1, 2, 3]"

if __name__ == '__main__':
    test_BbMmCode_iterate()
