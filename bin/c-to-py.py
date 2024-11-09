#!env python3
# ------------------------------------------------------------------------ #
#             C   T O   P Y  -  A   B b M m   T O O L 
#
# Generate python access primitive from a c-header file.
# Supose 'simple' c-header file: 
#     - functions return only classical type (cf. typeDico) our pointers
# ------------------------------------------------------------------------ #

import sys, re

reVoidLine= re.compile(r"^[ \t\n]*$")
reParameter= re.compile(r"([a-zA-Z-09_]+ *\**) ([a-zA-Z0-9_]+)")
typeDico= {
    "short": "c_short",
    "int": "c_int",
    "long": "c_long",
    "ushort": "c_ushort",
    "uint": "c_uint",
    "ulong": "c_ulong",
    "float": "c_float",
    "double": "c_double",
    "digit": "c_digit",
    "bool": "c_digit",
    "hash": "c_hash",
}

header= r"""import os, ctypes

# ------------------------------------------------------------------------ #
#             P Y T H O N   W R A P E R   O F   l i b B b M m
#
# - generated with bin/c-to-py.py
# - c-header : bbmm.h
# 
#        /!\ ANY MODIFICATION IN THIS FILE WILL BE ERASED /!\
# ------------------------------------------------------------------------ #

# Usefull ctype types:

c_ushort, c_ulong, c_double, c_void_p=  ctypes.c_ushort, ctypes.c_ulong, ctypes.c_double, ctypes.c_void_p

# Usefull BbMm basis types:

c_digit, c_hash= c_ushort, c_ulong

# CArray tools :

def makeCArray( c_type, size, value ):
    Array= c_type * size
    cArray= Array()
    for i in range(size) :
        cArray[i]= (c_type)( value )
    return cArray

def makeCArrayAs( c_type, size, pythonLst ):
    Array= c_type * size
    cArray= Array()
    for i in range(size) :
        cArray[i]= (c_type)( pythonLst[i] )
    return cArray

def readCArray( py_type, c_type, size, arrayPointer ):
    pLst= ctypes.cast(arrayPointer, ctypes.POINTER(c_type))
    return [ (py_type)(pLst[i]) for i in range(size) ]

# Load c-core BbMm librairy : 

bbmmDir= os.path.dirname(os.path.realpath(__file__))
print( f">>>> LOAD LIB: {bbmmDir} <<<" )
core = ctypes.cdll.LoadLibrary( bbmmDir+"/libbbmm.so" )

# bbmm.h wraps :

"""

def convert( cHeaderFile, pythonFile ):
    fch= open( cHeaderFile, 'r' )
    fpy= open( pythonFile, 'w' )

    fpy.write( header.replace("HEADER_FILE.h", cHeaderFile) )

    fctLine= re.compile(r"([a-zA-Z-09_]+ *\**) ([a-zA-Z0-9_]+)\(([\w\W]*)\);")

    for line in fch :
        fct= fctLine.match(line)
        if fct :
            convertFct( fpy, fct.group(2), fct.group(1), fct.group(3) )

    fch.close()
    fpy.close()

def convertFct( fpy, fctName, returnType, parameterStr ):
    parameterStr= parameterStr.strip()
    parameters= []
    pyParamType= []
    isOk= True
    if parameterStr != '' :
        parameters= [ p.strip() for p in parameterStr.split(',') ]
        for p in parameters :
            m= reParameter.match(p)
            if m :
                pyParamType.append( pythonType(m.group(1)) )
            else :
                print( f"ERROR: format on : {fctName}({parameterStr})")
                pyParamType.append( "ERROR" )
                isOk= False

    if isOk :
        fpy.write( f"\n# {returnType} {fctName}( {', '.join(parameters)} );\n")
        fpy.write( f"{fctName}= core.{fctName}\n")
        fpy.write( f"{fctName}.restype= {pythonType(returnType)}\n")
        fpy.write( f"{fctName}.argtypes= ["+ ", ".join(pyParamType) +"]\n")

def pythonType( cType ):
    pytype= "c_void_p"
    if cType in typeDico :
        pytype= typeDico[cType]
    return pytype

convert( sys.argv[1], sys.argv[2] )
