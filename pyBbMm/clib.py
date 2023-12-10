import os
from ctypes import cdll, c_uint, cast, POINTER, c_double

# ctypes tools (uint): 

def uintArray( size, value=0 ):
    Array= c_uint * size
    cArray= Array()
    for i in range(size) :
        cArray[i]= (c_uint)( value )
    return cArray

def uintArrayAs( size, pythonLst ):
    Array= c_uint * size
    cArray= Array()
    for i in range(size) :
        cArray[i]= (c_uint)( pythonLst[i] )
    return cArray

def readUintLst( size, uintPointer ):
    pLst= cast(uintPointer, POINTER(c_uint))
    return [ (int)(pLst[i]) for i in range(size) ]


# ctypes tools (double): 

def doubleArray( size, value=0.0 ):
    Array= c_double * size
    cArray= Array()
    for i in range(size) :
        cArray[i]= (c_double)( value )
    return cArray

def doubleArrayAs( size, pythonLst ):
    Array= c_double * size
    cArray= Array()
    for i in range(size) :
        cArray[i]= (c_double)( pythonLst[i] )
    return cArray

def readDoubleLst( size, doublePointer ):
    pLst= cast(doublePointer, POINTER(c_double))
    return [ (float)(pLst[i]) for i in range(size) ]

# Load c-core BbMm librairy : 
bbmmDir= os.path.dirname(os.path.realpath(__file__))
print( f">>>> LOAD LIB: {bbmmDir} <<<" )
core = cdll.LoadLibrary( bbmmDir+"/libbbmm.so" )
