from .clib import core
from ctypes import c_int, c_uint, c_ulong, c_double, c_void_p

# ------------------------------------------------------------------------ #
#             P Y T H O N   W R A P E R   O F   l i b B b M m
#
# - generated with bin/c-to-py.py
# - c-header : bbmm.h
# 
#        /!\ ANY MODIFICATION IN THIS FILE WILL BE ERASED /!\
# ------------------------------------------------------------------------ #


# BmCode* newBmCode( uint size );
newBmCode= core.newBmCode
newBmCode.restype= c_void_p
newBmCode.argtypes= [c_uint]

# BmCode* newBmCode_numbers( uint size, uint* numbers );
newBmCode_numbers= core.newBmCode_numbers
newBmCode_numbers.restype= c_void_p
newBmCode_numbers.argtypes= [c_uint, c_void_p]

# BmCode* newBmCode_all( uint size, uint defaultValue );
newBmCode_all= core.newBmCode_all
newBmCode_all.restype= c_void_p
newBmCode_all.argtypes= [c_uint, c_uint]

# BmCode* newBmCodeAs( BmCode* model );
newBmCodeAs= core.newBmCodeAs
newBmCodeAs.restype= c_void_p
newBmCodeAs.argtypes= [c_void_p]

# BmCode* BmCode_create( BmCode* self, uint size );
BmCode_create= core.BmCode_create
BmCode_create.restype= c_void_p
BmCode_create.argtypes= [c_void_p, c_uint]

# BmCode* BmCode_create_numbers( BmCode* self, uint size, uint* numbers );
BmCode_create_numbers= core.BmCode_create_numbers
BmCode_create_numbers.restype= c_void_p
BmCode_create_numbers.argtypes= [c_void_p, c_uint, c_void_p]

# BmCode* BmCode_create_all( BmCode* self, uint size, uint defaultValue );
BmCode_create_all= core.BmCode_create_all
BmCode_create_all.restype= c_void_p
BmCode_create_all.argtypes= [c_void_p, c_uint, c_uint]

# BmCode* BmCode_createAs( BmCode* self, BmCode* model );
BmCode_createAs= core.BmCode_createAs
BmCode_createAs.restype= c_void_p
BmCode_createAs.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_createMerge( BmCode* self, uint numberOfCodes, BmCode ** codes );
BmCode_createMerge= core.BmCode_createMerge
BmCode_createMerge.restype= c_void_p
BmCode_createMerge.argtypes= [c_void_p, c_uint, c_void_p]

# void deleteBmCode( BmCode* instance );
deleteBmCode= core.deleteBmCode
deleteBmCode.restype= c_void_p
deleteBmCode.argtypes= [c_void_p]

# BmCode* BmCodedestroy( BmCode* self );
BmCodedestroy= core.BmCodedestroy
BmCodedestroy.restype= c_void_p
BmCodedestroy.argtypes= [c_void_p]

# uint BmCodeDimention( BmCode* self );
BmCodeDimention= core.BmCodeDimention
BmCodeDimention.restype= c_uint
BmCodeDimention.argtypes= [c_void_p]

# uint BmCode_digit( BmCode* self, uint index );
BmCode_digit= core.BmCode_digit
BmCode_digit.restype= c_uint
BmCode_digit.argtypes= [c_void_p, c_uint]

# uint BmCode_count( BmCode* self, uint value );
BmCode_count= core.BmCode_count
BmCode_count.restype= c_uint
BmCode_count.argtypes= [c_void_p, c_uint]

# ulong BmCodeSum( BmCode* self );
BmCodeSum= core.BmCodeSum
BmCodeSum.restype= c_ulong
BmCodeSum.argtypes= [c_void_p]

# ulong BmCodeProduct( BmCode* self );
BmCodeProduct= core.BmCodeProduct
BmCodeProduct.restype= c_ulong
BmCodeProduct.argtypes= [c_void_p]

# BmCode* BmCode_reinit( BmCode* self, uint newSize );
BmCode_reinit= core.BmCode_reinit
BmCode_reinit.restype= c_void_p
BmCode_reinit.argtypes= [c_void_p, c_uint]

# BmCode* BmCode_copy( BmCode* self, BmCode* model );
BmCode_copy= core.BmCode_copy
BmCode_copy.restype= c_void_p
BmCode_copy.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_copyNumbers( BmCode* self, BmCode* model );
BmCode_copyNumbers= core.BmCode_copyNumbers
BmCode_copyNumbers.restype= c_void_p
BmCode_copyNumbers.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_redimention( BmCode* self, uint newSize );
BmCode_redimention= core.BmCode_redimention
BmCode_redimention.restype= c_void_p
BmCode_redimention.argtypes= [c_void_p, c_uint]

# BmCode* BmCode_setAll( BmCode* self, uint value );
BmCode_setAll= core.BmCode_setAll
BmCode_setAll.restype= c_void_p
BmCode_setAll.argtypes= [c_void_p, c_uint]

# BmCode* BmCode_at_set( BmCode* self, uint index, uint value );
BmCode_at_set= core.BmCode_at_set
BmCode_at_set.restype= c_void_p
BmCode_at_set.argtypes= [c_void_p, c_uint, c_uint]

# BmCode* BmCode_at_increment( BmCode* self, uint index, uint value );
BmCode_at_increment= core.BmCode_at_increment
BmCode_at_increment.restype= c_void_p
BmCode_at_increment.argtypes= [c_void_p, c_uint, c_uint]

# BmCode* BmCode_at_decrement( BmCode* self, uint index, uint value );
BmCode_at_decrement= core.BmCode_at_decrement
BmCode_at_decrement.restype= c_void_p
BmCode_at_decrement.argtypes= [c_void_p, c_uint, c_uint]

# BmCode* BmCode_setNumbers( BmCode* self, uint* numbers );
BmCode_setNumbers= core.BmCode_setNumbers
BmCode_setNumbers.restype= c_void_p
BmCode_setNumbers.argtypes= [c_void_p, c_void_p]

# void BmCodeSort( BmCode* self );
BmCodeSort= core.BmCodeSort
BmCodeSort.restype= c_void_p
BmCodeSort.argtypes= [c_void_p]

# void BmCode_switch( BmCode* self, BmCode* anotherCode );
BmCode_switch= core.BmCode_switch
BmCode_switch.restype= c_void_p
BmCode_switch.argtypes= [c_void_p, c_void_p]

# uint BmCode_search( BmCode* self, uint value );
BmCode_search= core.BmCode_search
BmCode_search.restype= c_uint
BmCode_search.argtypes= [c_void_p, c_uint]

# bool BmCode_isEqualTo( BmCode* self, BmCode* another );
BmCode_isEqualTo= core.BmCode_isEqualTo
BmCode_isEqualTo.restype= c_int
BmCode_isEqualTo.argtypes= [c_void_p, c_void_p]

# bool BmCode_isGreaterThan( BmCode* self, BmCode* another );
BmCode_isGreaterThan= core.BmCode_isGreaterThan
BmCode_isGreaterThan.restype= c_int
BmCode_isGreaterThan.argtypes= [c_void_p, c_void_p]

# bool BmCode_isSmallerThan( BmCode* self, BmCode* another );
BmCode_isSmallerThan= core.BmCode_isSmallerThan
BmCode_isSmallerThan.restype= c_int
BmCode_isSmallerThan.argtypes= [c_void_p, c_void_p]

# ulong BmCode_keyOf( BmCode* self, BmCode* code );
BmCode_keyOf= core.BmCode_keyOf
BmCode_keyOf.restype= c_ulong
BmCode_keyOf.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_setCode_onKey( BmCode* self, BmCode* configuration, ulong key );
BmCode_setCode_onKey= core.BmCode_setCode_onKey
BmCode_setCode_onKey.restype= c_void_p
BmCode_setCode_onKey.argtypes= [c_void_p, c_void_p, c_ulong]

# BmCode* BmCode_setCodeFirst( BmCode* self, BmCode* configuration );
BmCode_setCodeFirst= core.BmCode_setCodeFirst
BmCode_setCodeFirst.restype= c_void_p
BmCode_setCodeFirst.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_setCodeLast( BmCode* self, BmCode* configuration );
BmCode_setCodeLast= core.BmCode_setCodeLast
BmCode_setCodeLast.restype= c_void_p
BmCode_setCodeLast.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_newBmCodeOnKey( BmCode* self, ulong key );
BmCode_newBmCodeOnKey= core.BmCode_newBmCodeOnKey
BmCode_newBmCodeOnKey.restype= c_void_p
BmCode_newBmCodeOnKey.argtypes= [c_void_p, c_ulong]

# BmCode* BmCodeNewBmCodeFirst( BmCode* self );
BmCodeNewBmCodeFirst= core.BmCodeNewBmCodeFirst
BmCodeNewBmCodeFirst.restype= c_void_p
BmCodeNewBmCodeFirst.argtypes= [c_void_p]

# BmCode* BmCodeNewBmCodeLast( BmCode* self );
BmCodeNewBmCodeLast= core.BmCodeNewBmCodeLast
BmCodeNewBmCodeLast.restype= c_void_p
BmCodeNewBmCodeLast.argtypes= [c_void_p]

# BmCode* BmCode_nextCode( BmCode* self, BmCode* configuration );
BmCode_nextCode= core.BmCode_nextCode
BmCode_nextCode.restype= c_void_p
BmCode_nextCode.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_previousCode( BmCode* self, BmCode* configuration );
BmCode_previousCode= core.BmCode_previousCode
BmCode_previousCode.restype= c_void_p
BmCode_previousCode.argtypes= [c_void_p, c_void_p]

# bool BmCode_isIncluding( BmCode* self, BmCode* configuration );
BmCode_isIncluding= core.BmCode_isIncluding
BmCode_isIncluding.restype= c_int
BmCode_isIncluding.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_newBmCodeMask( BmCode* self, BmCode* mask );
BmCode_newBmCodeMask= core.BmCode_newBmCodeMask
BmCode_newBmCodeMask.restype= c_void_p
BmCode_newBmCodeMask.argtypes= [c_void_p, c_void_p]

# char* BmCode_print( BmCode* self, char* buffer );
BmCode_print= core.BmCode_print
BmCode_print.restype= c_void_p
BmCode_print.argtypes= [c_void_p, c_void_p]

# BmVector* newBmVector( uint size );
newBmVector= core.newBmVector
newBmVector.restype= c_void_p
newBmVector.argtypes= [c_uint]

# BmVector* newBmVector_values( uint size, double* values );
newBmVector_values= core.newBmVector_values
newBmVector_values.restype= c_void_p
newBmVector_values.argtypes= [c_uint, c_void_p]

# BmVector* newBmVector_all( uint size, double value );
newBmVector_all= core.newBmVector_all
newBmVector_all.restype= c_void_p
newBmVector_all.argtypes= [c_uint, c_double]

# BmVector* BmVector_create( BmVector* self, uint size );
BmVector_create= core.BmVector_create
BmVector_create.restype= c_void_p
BmVector_create.argtypes= [c_void_p, c_uint]

# BmVector* BmVector_create_values( BmVector* self, uint size, double* values );
BmVector_create_values= core.BmVector_create_values
BmVector_create_values.restype= c_void_p
BmVector_create_values.argtypes= [c_void_p, c_uint, c_void_p]

# BmVector* BmVector_create_all( BmVector* self, uint size, double value );
BmVector_create_all= core.BmVector_create_all
BmVector_create_all.restype= c_void_p
BmVector_create_all.argtypes= [c_void_p, c_uint, c_double]

# BmVector* BmVectordestroy( BmVector* self );
BmVectordestroy= core.BmVectordestroy
BmVectordestroy.restype= c_void_p
BmVectordestroy.argtypes= [c_void_p]

# void deleteBmVector( BmVector* self );
deleteBmVector= core.deleteBmVector
deleteBmVector.restype= c_void_p
deleteBmVector.argtypes= [c_void_p]

# BmVector* BmVector_reinit( BmVector* self, uint newSize );
BmVector_reinit= core.BmVector_reinit
BmVector_reinit.restype= c_void_p
BmVector_reinit.argtypes= [c_void_p, c_uint]

# BmVector* BmVector_copy( BmVector* self, BmVector* model );
BmVector_copy= core.BmVector_copy
BmVector_copy.restype= c_void_p
BmVector_copy.argtypes= [c_void_p, c_void_p]

# uint BmVectorDimention( BmVector* self );
BmVectorDimention= core.BmVectorDimention
BmVectorDimention.restype= c_uint
BmVectorDimention.argtypes= [c_void_p]

# double BmVector_value( BmVector* self, uint i );
BmVector_value= core.BmVector_value
BmVector_value.restype= c_double
BmVector_value.argtypes= [c_void_p, c_uint]

# BmVector* BmVector_redimention( BmVector* self, uint size );
BmVector_redimention= core.BmVector_redimention
BmVector_redimention.restype= c_void_p
BmVector_redimention.argtypes= [c_void_p, c_uint]

# double BmVector_at_set( BmVector* self, uint i, double value );
BmVector_at_set= core.BmVector_at_set
BmVector_at_set.restype= c_double
BmVector_at_set.argtypes= [c_void_p, c_uint, c_double]

# BmVector* BmVector_setValues( BmVector* self, double* values );
BmVector_setValues= core.BmVector_setValues
BmVector_setValues.restype= c_void_p
BmVector_setValues.argtypes= [c_void_p, c_void_p]

# double BmVectorSum( BmVector* self );
BmVectorSum= core.BmVectorSum
BmVectorSum.restype= c_double
BmVectorSum.argtypes= [c_void_p]

# double BmVectorProduct( BmVector* self );
BmVectorProduct= core.BmVectorProduct
BmVectorProduct.restype= c_double
BmVectorProduct.argtypes= [c_void_p]

# bool BmVector_isEqualTo( BmVector* self, BmVector* another );
BmVector_isEqualTo= core.BmVector_isEqualTo
BmVector_isEqualTo.restype= c_int
BmVector_isEqualTo.argtypes= [c_void_p, c_void_p]

# bool BmVector_isGreaterThan( BmVector* self, BmVector* another );
BmVector_isGreaterThan= core.BmVector_isGreaterThan
BmVector_isGreaterThan.restype= c_int
BmVector_isGreaterThan.argtypes= [c_void_p, c_void_p]

# bool BmVector_isSmallerThan( BmVector* self, BmVector* another );
BmVector_isSmallerThan= core.BmVector_isSmallerThan
BmVector_isSmallerThan.restype= c_int
BmVector_isSmallerThan.argtypes= [c_void_p, c_void_p]

# char* BmVector_print( BmVector* self, char* output );
BmVector_print= core.BmVector_print
BmVector_print.restype= c_void_p
BmVector_print.argtypes= [c_void_p, c_void_p]

# char* BmVector_format_print( BmVector* self, char* format, char* buffer );
BmVector_format_print= core.BmVector_format_print
BmVector_format_print.restype= c_void_p
BmVector_format_print.argtypes= [c_void_p, c_void_p, c_void_p]

# BmBench* newBmBench( uint capacity );
newBmBench= core.newBmBench
newBmBench.restype= c_void_p
newBmBench.argtypes= [c_uint]

# BmBench* newBmBenchWith( uint capacity, BmCode* newFirstItem, double value );
newBmBenchWith= core.newBmBenchWith
newBmBenchWith.restype= c_void_p
newBmBenchWith.argtypes= [c_uint, c_void_p, c_double]

# BmBench* newBmBenchAs( BmBench* model );
newBmBenchAs= core.newBmBenchAs
newBmBenchAs.restype= c_void_p
newBmBenchAs.argtypes= [c_void_p]

# BmBench* BmBench_create( BmBench* self, uint capacity );
BmBench_create= core.BmBench_create
BmBench_create.restype= c_void_p
BmBench_create.argtypes= [c_void_p, c_uint]

# BmBench* BmBench_createWith( BmBench* self, uint capacity, BmCode* newFirstItems, double value );
BmBench_createWith= core.BmBench_createWith
BmBench_createWith.restype= c_void_p
BmBench_createWith.argtypes= [c_void_p, c_uint, c_void_p, c_double]

# BmBench* BmBench_createAs( BmBench* self, BmBench* model );
BmBench_createAs= core.BmBench_createAs
BmBench_createAs.restype= c_void_p
BmBench_createAs.argtypes= [c_void_p, c_void_p]

# BmBench* BmBenchdestroy( BmBench* self );
BmBenchdestroy= core.BmBenchdestroy
BmBenchdestroy.restype= c_void_p
BmBenchdestroy.argtypes= [c_void_p]

# void deleteBmBench( BmBench* self );
deleteBmBench= core.deleteBmBench
deleteBmBench.restype= c_void_p
deleteBmBench.argtypes= [c_void_p]

# BmBench* BmBench_reinit( BmBench* self, uint capacity );
BmBench_reinit= core.BmBench_reinit
BmBench_reinit.restype= c_void_p
BmBench_reinit.argtypes= [c_void_p, c_uint]

# uint BmBench_size( BmBench* self );
BmBench_size= core.BmBench_size
BmBench_size.restype= c_uint
BmBench_size.argtypes= [c_void_p]

# uint BmBench_capacity( BmBench* self );
BmBench_capacity= core.BmBench_capacity
BmBench_capacity.restype= c_uint
BmBench_capacity.argtypes= [c_void_p]

# BmCode* BmBench_at( BmBench* self, uint i );
BmBench_at= core.BmBench_at
BmBench_at.restype= c_void_p
BmBench_at.argtypes= [c_void_p, c_uint]

# double BmBench_valueAt( BmBench* self, uint i );
BmBench_valueAt= core.BmBench_valueAt
BmBench_valueAt.restype= c_double
BmBench_valueAt.argtypes= [c_void_p, c_uint]

# uint BmBenchDimention( BmBench* self );
BmBenchDimention= core.BmBenchDimention
BmBenchDimention.restype= c_uint
BmBenchDimention.argtypes= [c_void_p]

# void BmBench_resizeCapacity( BmBench* self, uint newCapacity );
BmBench_resizeCapacity= core.BmBench_resizeCapacity
BmBench_resizeCapacity.restype= c_void_p
BmBench_resizeCapacity.argtypes= [c_void_p, c_uint]

# uint BmBench_attach( BmBench* self, BmCode* newItem );
BmBench_attach= core.BmBench_attach
BmBench_attach.restype= c_uint
BmBench_attach.argtypes= [c_void_p, c_void_p]

# uint BmBench_attachLast( BmBench* self, BmCode* newItem, double value );
BmBench_attachLast= core.BmBench_attachLast
BmBench_attachLast.restype= c_uint
BmBench_attachLast.argtypes= [c_void_p, c_void_p, c_double]

# BmCode* BmBench_detachLast( BmBench* self );
BmBench_detachLast= core.BmBench_detachLast
BmBench_detachLast.restype= c_void_p
BmBench_detachLast.argtypes= [c_void_p]

# uint BmBench_attachFirst( BmBench* self, BmCode* newItem, double value );
BmBench_attachFirst= core.BmBench_attachFirst
BmBench_attachFirst.restype= c_uint
BmBench_attachFirst.argtypes= [c_void_p, c_void_p, c_double]

# BmCode* BmBench_detachFirst( BmBench* self );
BmBench_detachFirst= core.BmBench_detachFirst
BmBench_detachFirst.restype= c_void_p
BmBench_detachFirst.argtypes= [c_void_p]

# BmCode* BmBench_at_setValue( BmBench* self, uint i, double value );
BmBench_at_setValue= core.BmBench_at_setValue
BmBench_at_setValue.restype= c_void_p
BmBench_at_setValue.argtypes= [c_void_p, c_uint, c_double]

# void BmBench_switch( BmBench* self, BmBench* doppleganger );
BmBench_switch= core.BmBench_switch
BmBench_switch.restype= c_void_p
BmBench_switch.argtypes= [c_void_p, c_void_p]

# void BmBench_add_reducted( BmBench* self, BmBench* another, BmCode* mask );
BmBench_add_reducted= core.BmBench_add_reducted
BmBench_add_reducted.restype= c_void_p
BmBench_add_reducted.argtypes= [c_void_p, c_void_p, c_void_p]

# uint BmBench_sort( BmBench* self, fctptr_BmBench_compare compare );
BmBench_sort= core.BmBench_sort
BmBench_sort.restype= c_uint
BmBench_sort.argtypes= [c_void_p, c_void_p]

# uint BmBench_switchCodes( BmBench* self, uint id1, uint id2 );
BmBench_switchCodes= core.BmBench_switchCodes
BmBench_switchCodes.restype= c_uint
BmBench_switchCodes.argtypes= [c_void_p, c_uint, c_uint]

# bool BmBench_isGreater( BmBench* self, uint i1, uint i2 );
BmBench_isGreater= core.BmBench_isGreater
BmBench_isGreater.restype= c_int
BmBench_isGreater.argtypes= [c_void_p, c_uint, c_uint]

# bool BmBench_isSmaller( BmBench* self, uint i1, uint i2 );
BmBench_isSmaller= core.BmBench_isSmaller
BmBench_isSmaller.restype= c_int
BmBench_isSmaller.argtypes= [c_void_p, c_uint, c_uint]

# bool BmBench_isGreaterValue( BmBench* self, uint i1, uint i2 );
BmBench_isGreaterValue= core.BmBench_isGreaterValue
BmBench_isGreaterValue.restype= c_int
BmBench_isGreaterValue.argtypes= [c_void_p, c_uint, c_uint]

# bool BmBench_isSmallerValue( BmBench* self, uint i1, uint i2 );
BmBench_isSmallerValue= core.BmBench_isSmallerValue
BmBench_isSmallerValue.restype= c_int
BmBench_isSmallerValue.argtypes= [c_void_p, c_uint, c_uint]

# char* BmBench_print( BmBench* self, char* output );
BmBench_print= core.BmBench_print
BmBench_print.restype= c_void_p
BmBench_print.argtypes= [c_void_p, c_void_p]

# char* BmBench_printCodes( BmBench* self, char* output );
BmBench_printCodes= core.BmBench_printCodes
BmBench_printCodes.restype= c_void_p
BmBench_printCodes.argtypes= [c_void_p, c_void_p]

# char* BmBench_printNetwork( BmBench* self, char* output );
BmBench_printNetwork= core.BmBench_printNetwork
BmBench_printNetwork.restype= c_void_p
BmBench_printNetwork.argtypes= [c_void_p, c_void_p]

# BmTree* newBmTree( uint binarySpaceSize );
newBmTree= core.newBmTree
newBmTree.restype= c_void_p
newBmTree.argtypes= [c_uint]

# BmTree* newBmTreeWith( BmCode* newSpace );
newBmTreeWith= core.newBmTreeWith
newBmTreeWith.restype= c_void_p
newBmTreeWith.argtypes= [c_void_p]

# BmTree* BmTree_createWhith( BmTree* self, BmCode* input );
BmTree_createWhith= core.BmTree_createWhith
BmTree_createWhith.restype= c_void_p
BmTree_createWhith.argtypes= [c_void_p, c_void_p]

# BmTree* BmTreedestroy( BmTree* self );
BmTreedestroy= core.BmTreedestroy
BmTreedestroy.restype= c_void_p
BmTreedestroy.argtypes= [c_void_p]

# void deleteBmTree( BmTree* self );
deleteBmTree= core.deleteBmTree
deleteBmTree.restype= c_void_p
deleteBmTree.argtypes= [c_void_p]

# BmTree* BmTree_reinitWith( BmTree* self, BmCode* newSpace );
BmTree_reinitWith= core.BmTree_reinitWith
BmTree_reinitWith.restype= c_void_p
BmTree_reinitWith.argtypes= [c_void_p, c_void_p]

# BmTree* BmTree_clearWhith_on( BmTree* self, uint index, uint defaultOption );
BmTree_clearWhith_on= core.BmTree_clearWhith_on
BmTree_clearWhith_on.restype= c_void_p
BmTree_clearWhith_on.argtypes= [c_void_p, c_uint, c_uint]

# BmTree* BmTree_clearOn( BmTree* self, uint defaultOption );
BmTree_clearOn= core.BmTree_clearOn
BmTree_clearOn.restype= c_void_p
BmTree_clearOn.argtypes= [c_void_p, c_uint]

# uint BmTree_size( BmTree* self );
BmTree_size= core.BmTree_size
BmTree_size.restype= c_uint
BmTree_size.argtypes= [c_void_p]

# BmCode* BmTree_inputRanges( BmTree* self );
BmTree_inputRanges= core.BmTree_inputRanges
BmTree_inputRanges.restype= c_void_p
BmTree_inputRanges.argtypes= [c_void_p]

# uint BmTree_at( BmTree* self, BmCode* code );
BmTree_at= core.BmTree_at
BmTree_at.restype= c_uint
BmTree_at.argtypes= [c_void_p, c_void_p]

# uint BmTreeChild( uint key );
BmTreeChild= core.BmTreeChild
BmTreeChild.restype= c_uint
BmTreeChild.argtypes= [c_uint]

# uint BmTreeLeaf( uint key );
BmTreeLeaf= core.BmTreeLeaf
BmTreeLeaf.restype= c_uint
BmTreeLeaf.argtypes= [c_uint]

# void BmTree_reziseCapacity( BmTree* self, uint newCapacity );
BmTree_reziseCapacity= core.BmTree_reziseCapacity
BmTree_reziseCapacity.restype= c_void_p
BmTree_reziseCapacity.argtypes= [c_void_p, c_uint]

# void BmTree_reziseCompleteCapacity( BmTree* self );
BmTree_reziseCompleteCapacity= core.BmTree_reziseCompleteCapacity
BmTree_reziseCompleteCapacity.restype= c_void_p
BmTree_reziseCompleteCapacity.argtypes= [c_void_p]

# uint BmTree_at_set( BmTree* self, BmCode* code, uint output );
BmTree_at_set= core.BmTree_at_set
BmTree_at_set.restype= c_uint
BmTree_at_set.argtypes= [c_void_p, c_void_p, c_uint]

# uint BmTree_at_readOrder_set( BmTree* self, BmCode* code, BmCode* codeOrder, uint output );
BmTree_at_readOrder_set= core.BmTree_at_readOrder_set
BmTree_at_readOrder_set.restype= c_uint
BmTree_at_readOrder_set.argtypes= [c_void_p, c_void_p, c_void_p, c_uint]

# uint BmTree_branchSize( BmTree* self, uint iBranch );
BmTree_branchSize= core.BmTree_branchSize
BmTree_branchSize.restype= c_uint
BmTree_branchSize.argtypes= [c_void_p, c_uint]

# uint BmTree_branch_state( BmTree* self, uint iBranch, uint state );
BmTree_branch_state= core.BmTree_branch_state
BmTree_branch_state.restype= c_uint
BmTree_branch_state.argtypes= [c_void_p, c_uint, c_uint]

# uint BmTree_branchVariable( BmTree* self, uint iBranch );
BmTree_branchVariable= core.BmTree_branchVariable
BmTree_branchVariable.restype= c_uint
BmTree_branchVariable.argtypes= [c_void_p, c_uint]

# uint BmTree_branchNumberOfOutputs( BmTree* self, uint branch );
BmTree_branchNumberOfOutputs= core.BmTree_branchNumberOfOutputs
BmTree_branchNumberOfOutputs.restype= c_uint
BmTree_branchNumberOfOutputs.argtypes= [c_void_p, c_uint]

# uint BmTree_deepOf( BmTree* self, BmCode* code );
BmTree_deepOf= core.BmTree_deepOf
BmTree_deepOf.restype= c_uint
BmTree_deepOf.argtypes= [c_void_p, c_void_p]

# uint BmTree_newBranch( BmTree* self, uint iVariable, uint defaultOption );
BmTree_newBranch= core.BmTree_newBranch
BmTree_newBranch.restype= c_uint
BmTree_newBranch.argtypes= [c_void_p, c_uint, c_uint]

# void BmTree_branch_state_connect( BmTree* self, uint branchA, uint stateA, uint branchB );
BmTree_branch_state_connect= core.BmTree_branch_state_connect
BmTree_branch_state_connect.restype= c_void_p
BmTree_branch_state_connect.argtypes= [c_void_p, c_uint, c_uint, c_uint]

# void BmTree_branch_state_set( BmTree* self, uint branchA, uint iState, uint outbut );
BmTree_branch_state_set= core.BmTree_branch_state_set
BmTree_branch_state_set.restype= c_void_p
BmTree_branch_state_set.argtypes= [c_void_p, c_uint, c_uint, c_uint]

# uint BmTree_cleanDeadBranches( BmTree* self );
BmTree_cleanDeadBranches= core.BmTree_cleanDeadBranches
BmTree_cleanDeadBranches.restype= c_uint
BmTree_cleanDeadBranches.argtypes= [c_void_p]

# uint BmTree_removeBranch( BmTree* self, uint iBranch );
BmTree_removeBranch= core.BmTree_removeBranch
BmTree_removeBranch.restype= c_uint
BmTree_removeBranch.argtypes= [c_void_p, c_uint]

# BmBench* BmTree_asNewBench( BmTree* self );
BmTree_asNewBench= core.BmTree_asNewBench
BmTree_asNewBench.restype= c_void_p
BmTree_asNewBench.argtypes= [c_void_p]

# void BmTree_fromBench( BmTree* self, BmBench* model );
BmTree_fromBench= core.BmTree_fromBench
BmTree_fromBench.restype= c_void_p
BmTree_fromBench.argtypes= [c_void_p, c_void_p]

# char* BmTree_printBranch( BmTree* self, uint iBranch, char* output );
BmTree_printBranch= core.BmTree_printBranch
BmTree_printBranch.restype= c_void_p
BmTree_printBranch.argtypes= [c_void_p, c_uint, c_void_p]

# char* BmTree_print( BmTree* self, char* output );
BmTree_print= core.BmTree_print
BmTree_print.restype= c_void_p
BmTree_print.argtypes= [c_void_p, c_void_p]

# char* BmTree_print_sep( BmTree* self, char* output, char* separator );
BmTree_print_sep= core.BmTree_print_sep
BmTree_print_sep.restype= c_void_p
BmTree_print_sep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmTree_print( BmTree* self, char* output );
BmTree_print= core.BmTree_print
BmTree_print.restype= c_void_p
BmTree_print.argtypes= [c_void_p, c_void_p]

# char* BmTree_printInside( BmTree* self, char* output );
BmTree_printInside= core.BmTree_printInside
BmTree_printInside.restype= c_void_p
BmTree_printInside.argtypes= [c_void_p, c_void_p]

# BmCondition* newBmConditionBasic( uint domain );
newBmConditionBasic= core.newBmConditionBasic
newBmConditionBasic.restype= c_void_p
newBmConditionBasic.argtypes= [c_uint]

# BmCondition* newBmConditionWith( uint domain, BmCode* newInputRanges, BmBench* newDefaultDistrib );
newBmConditionWith= core.newBmConditionWith
newBmConditionWith.restype= c_void_p
newBmConditionWith.argtypes= [c_uint, c_void_p, c_void_p]

# BmCondition* BmCondition_createBasic( BmCondition* self, uint domain );
BmCondition_createBasic= core.BmCondition_createBasic
BmCondition_createBasic.restype= c_void_p
BmCondition_createBasic.argtypes= [c_void_p, c_uint]

# BmCondition* BmCondition_createWith( BmCondition* self, uint domain, BmCode* newInputRanges, BmBench* newDefaultDistrib );
BmCondition_createWith= core.BmCondition_createWith
BmCondition_createWith.restype= c_void_p
BmCondition_createWith.argtypes= [c_void_p, c_uint, c_void_p, c_void_p]

# BmCondition* BmConditiondestroy( BmCondition* self );
BmConditiondestroy= core.BmConditiondestroy
BmConditiondestroy.restype= c_void_p
BmConditiondestroy.argtypes= [c_void_p]

# void deleteBmCondition( BmCondition* instance );
deleteBmCondition= core.deleteBmCondition
deleteBmCondition.restype= c_void_p
deleteBmCondition.argtypes= [c_void_p]

# uint BmCondition_reinitWith( BmCondition* self, uint domain, BmCode* newInputRanges, BmBench* newDistrib );
BmCondition_reinitWith= core.BmCondition_reinitWith
BmCondition_reinitWith.restype= c_uint
BmCondition_reinitWith.argtypes= [c_void_p, c_uint, c_void_p, c_void_p]

# uint BmCondition_reinitDistributionsWith( BmCondition* self, BmBench* newDistrib );
BmCondition_reinitDistributionsWith= core.BmCondition_reinitDistributionsWith
BmCondition_reinitDistributionsWith.restype= c_uint
BmCondition_reinitDistributionsWith.argtypes= [c_void_p, c_void_p]

# uint BmCondition_range( BmCondition* self );
BmCondition_range= core.BmCondition_range
BmCondition_range.restype= c_uint
BmCondition_range.argtypes= [c_void_p]

# BmTree* BmCondition_selector( BmCondition* self );
BmCondition_selector= core.BmCondition_selector
BmCondition_selector.restype= c_void_p
BmCondition_selector.argtypes= [c_void_p]

# BmCode* BmCondition_parents( BmCondition* self );
BmCondition_parents= core.BmCondition_parents
BmCondition_parents.restype= c_void_p
BmCondition_parents.argtypes= [c_void_p]

# BmBench* BmCondition_from( BmCondition* self, BmCode* configuration );
BmCondition_from= core.BmCondition_from
BmCondition_from.restype= c_void_p
BmCondition_from.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_fromKey( BmCondition* self, uint configKey );
BmCondition_fromKey= core.BmCondition_fromKey
BmCondition_fromKey.restype= c_void_p
BmCondition_fromKey.argtypes= [c_void_p, c_uint]

# uint BmCondition_distributionSize( BmCondition* self );
BmCondition_distributionSize= core.BmCondition_distributionSize
BmCondition_distributionSize.restype= c_uint
BmCondition_distributionSize.argtypes= [c_void_p]

# BmBench* BmCondition_distributionAt( BmCondition* self, uint iDistrib );
BmCondition_distributionAt= core.BmCondition_distributionAt
BmCondition_distributionAt.restype= c_void_p
BmCondition_distributionAt.argtypes= [c_void_p, c_uint]

# uint BmCondition_attach( BmCondition* self, BmBench* distribution );
BmCondition_attach= core.BmCondition_attach
BmCondition_attach.restype= c_uint
BmCondition_attach.argtypes= [c_void_p, c_void_p]

# uint BmCondition_from_attach( BmCondition* self, BmCode* configuration, BmBench* distribution );
BmCondition_from_attach= core.BmCondition_from_attach
BmCondition_from_attach.restype= c_uint
BmCondition_from_attach.argtypes= [c_void_p, c_void_p, c_void_p]

# void BmCondition_switch( BmCondition* self, BmCondition* doppelganger );
BmCondition_switch= core.BmCondition_switch
BmCondition_switch.restype= c_void_p
BmCondition_switch.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_infer( BmCondition* self, BmBench* distribOverConfigurations );
BmCondition_infer= core.BmCondition_infer
BmCondition_infer.restype= c_void_p
BmCondition_infer.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_newDistributionByInfering( BmCondition* self, BmBench* distribOverConfigurations );
BmCondition_newDistributionByInfering= core.BmCondition_newDistributionByInfering
BmCondition_newDistributionByInfering.restype= c_void_p
BmCondition_newDistributionByInfering.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_newDistributionByInfering_mask( BmCondition* self, BmBench* longDistrib, BmCode* parentMask );
BmCondition_newDistributionByInfering_mask= core.BmCondition_newDistributionByInfering_mask
BmCondition_newDistributionByInfering_mask.restype= c_void_p
BmCondition_newDistributionByInfering_mask.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmCondition_print( BmCondition* self, char* output );
BmCondition_print= core.BmCondition_print
BmCondition_print.restype= c_void_p
BmCondition_print.argtypes= [c_void_p, c_void_p]

# char* BmCondition_printSep( BmCondition* self, char* output, char* separator );
BmCondition_printSep= core.BmCondition_printSep
BmCondition_printSep.restype= c_void_p
BmCondition_printSep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmCondition_printExtend( BmCondition* self, char* output );
BmCondition_printExtend= core.BmCondition_printExtend
BmCondition_printExtend.restype= c_void_p
BmCondition_printExtend.argtypes= [c_void_p, c_void_p]

# char* BmCondition_printExtendSep( BmCondition* self, char* output, char* separator );
BmCondition_printExtendSep= core.BmCondition_printExtendSep
BmCondition_printExtendSep.restype= c_void_p
BmCondition_printExtendSep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmCondition_printIdentity( BmCondition* self, char* output );
BmCondition_printIdentity= core.BmCondition_printIdentity
BmCondition_printIdentity.restype= c_void_p
BmCondition_printIdentity.argtypes= [c_void_p, c_void_p]

# BmInferer* newBmInferer( BmCode* variableSpace, uint inputDimention, uint outputDimention );
newBmInferer= core.newBmInferer
newBmInferer.restype= c_void_p
newBmInferer.argtypes= [c_void_p, c_uint, c_uint]

# BmInferer* newBmInfererStateAction( BmCode* stateSpace, BmCode* actionSpace );
newBmInfererStateAction= core.newBmInfererStateAction
newBmInfererStateAction.restype= c_void_p
newBmInfererStateAction.argtypes= [c_void_p, c_void_p]

# BmInferer* newBmInfererStateActionShift( BmCode* stateSpace, BmCode* actionSpace, BmCode* shiftSpace );
newBmInfererStateActionShift= core.newBmInfererStateActionShift
newBmInfererStateActionShift.restype= c_void_p
newBmInfererStateActionShift.argtypes= [c_void_p, c_void_p, c_void_p]

# BmInferer* BmInferer_create( BmInferer* self, BmCode* varDomains, uint inputDimention, uint outputDimention );
BmInferer_create= core.BmInferer_create
BmInferer_create.restype= c_void_p
BmInferer_create.argtypes= [c_void_p, c_void_p, c_uint, c_uint]

# BmInferer* BmInfererdestroy( BmInferer* self );
BmInfererdestroy= core.BmInfererdestroy
BmInfererdestroy.restype= c_void_p
BmInfererdestroy.argtypes= [c_void_p]

# void deleteBmInferer( BmInferer* self );
deleteBmInferer= core.deleteBmInferer
deleteBmInferer.restype= c_void_p
deleteBmInferer.argtypes= [c_void_p]

# BmBench* BmInferer_distribution( BmInferer* self );
BmInferer_distribution= core.BmInferer_distribution
BmInferer_distribution.restype= c_void_p
BmInferer_distribution.argtypes= [c_void_p]

# uint BmInferer_inputDimention( BmInferer* self );
BmInferer_inputDimention= core.BmInferer_inputDimention
BmInferer_inputDimention.restype= c_uint
BmInferer_inputDimention.argtypes= [c_void_p]

# uint BmInferer_outputDimention( BmInferer* self );
BmInferer_outputDimention= core.BmInferer_outputDimention
BmInferer_outputDimention.restype= c_uint
BmInferer_outputDimention.argtypes= [c_void_p]

# uint BmInferer_shiftDimention( BmInferer* self );
BmInferer_shiftDimention= core.BmInferer_shiftDimention
BmInferer_shiftDimention.restype= c_uint
BmInferer_shiftDimention.argtypes= [c_void_p]

# uint BmInferer_overallDimention( BmInferer* self );
BmInferer_overallDimention= core.BmInferer_overallDimention
BmInferer_overallDimention.restype= c_uint
BmInferer_overallDimention.argtypes= [c_void_p]

# BmCondition* BmInferer_node( BmInferer* self, uint iNode );
BmInferer_node= core.BmInferer_node
BmInferer_node.restype= c_void_p
BmInferer_node.argtypes= [c_void_p, c_uint]

# uint BmInferer_node_size( BmInferer* self, uint iVar );
BmInferer_node_size= core.BmInferer_node_size
BmInferer_node_size.restype= c_uint
BmInferer_node_size.argtypes= [c_void_p, c_uint]

# BmCode* BmInferer_node_parents( BmInferer* self, uint iVar );
BmInferer_node_parents= core.BmInferer_node_parents
BmInferer_node_parents.restype= c_void_p
BmInferer_node_parents.argtypes= [c_void_p, c_uint]

# BmCondition* BmInferer_node_reinitIndependant( BmInferer* self, uint index );
BmInferer_node_reinitIndependant= core.BmInferer_node_reinitIndependant
BmInferer_node_reinitIndependant.restype= c_void_p
BmInferer_node_reinitIndependant.argtypes= [c_void_p, c_uint]

# BmCondition* BmInferer_node_reinitWith( BmInferer* self, uint index, BmCode* newDependenceList, BmBench* newDefaultDistrib );
BmInferer_node_reinitWith= core.BmInferer_node_reinitWith
BmInferer_node_reinitWith.restype= c_void_p
BmInferer_node_reinitWith.argtypes= [c_void_p, c_uint, c_void_p, c_void_p]

# BmBench* BmInferer_process( BmInferer* self, BmBench* inputDistribution );
BmInferer_process= core.BmInferer_process
BmInferer_process.restype= c_void_p
BmInferer_process.argtypes= [c_void_p, c_void_p]

# BmBench* BmInferer_process_newOverallDistribution( BmInferer* self, BmBench* inputDistribution );
BmInferer_process_newOverallDistribution= core.BmInferer_process_newOverallDistribution
BmInferer_process_newOverallDistribution.restype= c_void_p
BmInferer_process_newOverallDistribution.argtypes= [c_void_p, c_void_p]

# BmBench* BmInferer_processState_Action( BmInferer* self, BmCode* state, BmCode* action );
BmInferer_processState_Action= core.BmInferer_processState_Action
BmInferer_processState_Action.restype= c_void_p
BmInferer_processState_Action.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmInferer_print( BmInferer* self, char* output );
BmInferer_print= core.BmInferer_print
BmInferer_print.restype= c_void_p
BmInferer_print.argtypes= [c_void_p, c_void_p]

# char* BmInferer_printStateActionSignature( BmInferer* self, char* output );
BmInferer_printStateActionSignature= core.BmInferer_printStateActionSignature
BmInferer_printStateActionSignature.restype= c_void_p
BmInferer_printStateActionSignature.argtypes= [c_void_p, c_void_p]

# char* BmInferer_printDependency( BmInferer* self, char* output );
BmInferer_printDependency= core.BmInferer_printDependency
BmInferer_printDependency.restype= c_void_p
BmInferer_printDependency.argtypes= [c_void_p, c_void_p]

# BmCriterion* newBmCriterionBasic( uint inputSize, uint outputSize );
newBmCriterionBasic= core.newBmCriterionBasic
newBmCriterionBasic.restype= c_void_p
newBmCriterionBasic.argtypes= [c_uint, c_uint]

# BmCriterion* newBmCriterionWith( BmCode* newInputRanges, BmVector* newOutputs );
newBmCriterionWith= core.newBmCriterionWith
newBmCriterionWith.restype= c_void_p
newBmCriterionWith.argtypes= [c_void_p, c_void_p]

# BmCriterion* BmCriterion_createWith( BmCriterion* self, BmCode* newInputRanges, BmVector* newOutputs );
BmCriterion_createWith= core.BmCriterion_createWith
BmCriterion_createWith.restype= c_void_p
BmCriterion_createWith.argtypes= [c_void_p, c_void_p, c_void_p]

# BmCriterion* BmCriteriondestroy( BmCriterion* self );
BmCriteriondestroy= core.BmCriteriondestroy
BmCriteriondestroy.restype= c_void_p
BmCriteriondestroy.argtypes= [c_void_p]

# void deleteBmCriterion( BmCriterion* instance );
deleteBmCriterion= core.deleteBmCriterion
deleteBmCriterion.restype= c_void_p
deleteBmCriterion.argtypes= [c_void_p]

# uint BmCriterion_reinitWith( BmCriterion* self, BmCode* newInputRanges, BmVector* newOutputs );
BmCriterion_reinitWith= core.BmCriterion_reinitWith
BmCriterion_reinitWith.restype= c_uint
BmCriterion_reinitWith.argtypes= [c_void_p, c_void_p, c_void_p]

# BmTree* BmCriterion_selector( BmCriterion* self );
BmCriterion_selector= core.BmCriterion_selector
BmCriterion_selector.restype= c_void_p
BmCriterion_selector.argtypes= [c_void_p]

# BmVector* BmCriterion_outputs( BmCriterion* self );
BmCriterion_outputs= core.BmCriterion_outputs
BmCriterion_outputs.restype= c_void_p
BmCriterion_outputs.argtypes= [c_void_p]

# double BmCriterion_from( BmCriterion* self, BmCode* input );
BmCriterion_from= core.BmCriterion_from
BmCriterion_from.restype= c_double
BmCriterion_from.argtypes= [c_void_p, c_void_p]

# uint BmCriterion_addValue( BmCriterion* self, double ouputValue );
BmCriterion_addValue= core.BmCriterion_addValue
BmCriterion_addValue.restype= c_uint
BmCriterion_addValue.argtypes= [c_void_p, c_double]

# uint BmCriterion_ouputId_setValue( BmCriterion* self, uint ouputId, double ouputValue );
BmCriterion_ouputId_setValue= core.BmCriterion_ouputId_setValue
BmCriterion_ouputId_setValue.restype= c_uint
BmCriterion_ouputId_setValue.argtypes= [c_void_p, c_uint, c_double]

# uint BmCriterion_from_set( BmCriterion* self, BmCode* input, uint ouputId );
BmCriterion_from_set= core.BmCriterion_from_set
BmCriterion_from_set.restype= c_uint
BmCriterion_from_set.argtypes= [c_void_p, c_void_p, c_uint]

# void BmCriterion_switch( BmCriterion* self, BmCriterion* doppelganger );
BmCriterion_switch= core.BmCriterion_switch
BmCriterion_switch.restype= c_void_p
BmCriterion_switch.argtypes= [c_void_p, c_void_p]

# BmBench* BmCriterion_asNewBench( BmCriterion* self );
BmCriterion_asNewBench= core.BmCriterion_asNewBench
BmCriterion_asNewBench.restype= c_void_p
BmCriterion_asNewBench.argtypes= [c_void_p]

# char* BmCriterion_print( BmCriterion* self, char* buffer );
BmCriterion_print= core.BmCriterion_print
BmCriterion_print.restype= c_void_p
BmCriterion_print.argtypes= [c_void_p, c_void_p]

# char* BmCriterion_printSep( BmCriterion* self, char* buffer, char* separator );
BmCriterion_printSep= core.BmCriterion_printSep
BmCriterion_printSep.restype= c_void_p
BmCriterion_printSep.argtypes= [c_void_p, c_void_p, c_void_p]

# BmEvaluator* newBmEvaluatorBasic( uint spaceDimention, uint numberOfCriteria );
newBmEvaluatorBasic= core.newBmEvaluatorBasic
newBmEvaluatorBasic.restype= c_void_p
newBmEvaluatorBasic.argtypes= [c_uint, c_uint]

# BmEvaluator* newBmEvaluatorWith( BmCode* newSpace, uint numberOfCriteria );
newBmEvaluatorWith= core.newBmEvaluatorWith
newBmEvaluatorWith.restype= c_void_p
newBmEvaluatorWith.argtypes= [c_void_p, c_uint]

# BmEvaluator* BmEvaluator_createWith( BmEvaluator* self, BmCode* newSpace, uint numberOfCriteria );
BmEvaluator_createWith= core.BmEvaluator_createWith
BmEvaluator_createWith.restype= c_void_p
BmEvaluator_createWith.argtypes= [c_void_p, c_void_p, c_uint]

# void deleteBmEvaluator( BmEvaluator* self );
deleteBmEvaluator= core.deleteBmEvaluator
deleteBmEvaluator.restype= c_void_p
deleteBmEvaluator.argtypes= [c_void_p]

# BmEvaluator* BmEvaluatordestroy( BmEvaluator* self );
BmEvaluatordestroy= core.BmEvaluatordestroy
BmEvaluatordestroy.restype= c_void_p
BmEvaluatordestroy.argtypes= [c_void_p]

# BmCode* BmEvaluator_space( BmEvaluator* self );
BmEvaluator_space= core.BmEvaluator_space
BmEvaluator_space.restype= c_void_p
BmEvaluator_space.argtypes= [c_void_p]

# uint BmEvaluator_numberOfCriteria( BmEvaluator* self );
BmEvaluator_numberOfCriteria= core.BmEvaluator_numberOfCriteria
BmEvaluator_numberOfCriteria.restype= c_uint
BmEvaluator_numberOfCriteria.argtypes= [c_void_p]

# BmCriterion* BmEvaluator_criterion( BmEvaluator* self, uint iCritirion );
BmEvaluator_criterion= core.BmEvaluator_criterion
BmEvaluator_criterion.restype= c_void_p
BmEvaluator_criterion.argtypes= [c_void_p, c_uint]

# BmVector* BmEvaluator_weights( BmEvaluator* self );
BmEvaluator_weights= core.BmEvaluator_weights
BmEvaluator_weights.restype= c_void_p
BmEvaluator_weights.argtypes= [c_void_p]

# double BmEvaluator_criterion_weight( BmEvaluator* self, uint iCritirion );
BmEvaluator_criterion_weight= core.BmEvaluator_criterion_weight
BmEvaluator_criterion_weight.restype= c_double
BmEvaluator_criterion_weight.argtypes= [c_void_p, c_uint]

# BmCode* BmEvaluator_criterion_mask( BmEvaluator* self, uint iCritirion );
BmEvaluator_criterion_mask= core.BmEvaluator_criterion_mask
BmEvaluator_criterion_mask.restype= c_void_p
BmEvaluator_criterion_mask.argtypes= [c_void_p, c_uint]

# double BmEvaluator_process( BmEvaluator* self, BmCode* input );
BmEvaluator_process= core.BmEvaluator_process
BmEvaluator_process.restype= c_double
BmEvaluator_process.argtypes= [c_void_p, c_void_p]

# double BmEvaluator_criterion_process( BmEvaluator* self, uint iCriterion, BmCode* input );
BmEvaluator_criterion_process= core.BmEvaluator_criterion_process
BmEvaluator_criterion_process.restype= c_double
BmEvaluator_criterion_process.argtypes= [c_void_p, c_uint, c_void_p]

# double BmEvaluator_processState_action( BmEvaluator* self, BmCode* state, BmCode* action );
BmEvaluator_processState_action= core.BmEvaluator_processState_action
BmEvaluator_processState_action.restype= c_double
BmEvaluator_processState_action.argtypes= [c_void_p, c_void_p, c_void_p]

# double BmEvaluator_processState_action_state( BmEvaluator* self, BmCode* state, BmCode* action, BmCode* statePrime );
BmEvaluator_processState_action_state= core.BmEvaluator_processState_action_state
BmEvaluator_processState_action_state.restype= c_double
BmEvaluator_processState_action_state.argtypes= [c_void_p, c_void_p, c_void_p, c_void_p]

# BmEvaluator* BmEvaluator_reinitCriterion( BmEvaluator* self, uint numberOfCriterion );
BmEvaluator_reinitCriterion= core.BmEvaluator_reinitCriterion
BmEvaluator_reinitCriterion.restype= c_void_p
BmEvaluator_reinitCriterion.argtypes= [c_void_p, c_uint]

# BmCriterion* BmEvaluator_criterion_reinitWith( BmEvaluator* self, uint iCrit, BmCode* newDependenceMask, BmVector* newValues );
BmEvaluator_criterion_reinitWith= core.BmEvaluator_criterion_reinitWith
BmEvaluator_criterion_reinitWith.restype= c_void_p
BmEvaluator_criterion_reinitWith.argtypes= [c_void_p, c_uint, c_void_p, c_void_p]

# void BmEvaluator_criterion_from_set( BmEvaluator* self, uint index, BmCode* option, uint output );
BmEvaluator_criterion_from_set= core.BmEvaluator_criterion_from_set
BmEvaluator_criterion_from_set.restype= c_void_p
BmEvaluator_criterion_from_set.argtypes= [c_void_p, c_uint, c_void_p, c_uint]

# void BmEvaluator_criterion_setWeight( BmEvaluator* self, uint iCritirion, double weight );
BmEvaluator_criterion_setWeight= core.BmEvaluator_criterion_setWeight
BmEvaluator_criterion_setWeight.restype= c_void_p
BmEvaluator_criterion_setWeight.argtypes= [c_void_p, c_uint, c_double]

# BmDecision* newBmDecisionBasic( uint inputSize );
newBmDecisionBasic= core.newBmDecisionBasic
newBmDecisionBasic.restype= c_void_p
newBmDecisionBasic.argtypes= [c_uint]

# BmDecision* newBmDecisionWith( BmCode* newInputRanges, BmBench* newOutputs );
newBmDecisionWith= core.newBmDecisionWith
newBmDecisionWith.restype= c_void_p
newBmDecisionWith.argtypes= [c_void_p, c_void_p]

# BmDecision* BmDecision_createWith( BmDecision* self, BmCode* newInputRanges, BmBench* newOutputs );
BmDecision_createWith= core.BmDecision_createWith
BmDecision_createWith.restype= c_void_p
BmDecision_createWith.argtypes= [c_void_p, c_void_p, c_void_p]

# BmDecision* BmDecisiondestroy( BmDecision* self );
BmDecisiondestroy= core.BmDecisiondestroy
BmDecisiondestroy.restype= c_void_p
BmDecisiondestroy.argtypes= [c_void_p]

# void deleteBmDecision( BmDecision* instance );
deleteBmDecision= core.deleteBmDecision
deleteBmDecision.restype= c_void_p
deleteBmDecision.argtypes= [c_void_p]

# BmDecision* BmDecision_reinitWith( BmDecision* self, BmCode* newInputRanges, BmBench* newOutputs );
BmDecision_reinitWith= core.BmDecision_reinitWith
BmDecision_reinitWith.restype= c_void_p
BmDecision_reinitWith.argtypes= [c_void_p, c_void_p, c_void_p]

# BmDecision* BmDecision_reinitWithDefault( BmDecision* self, BmCode* newInputRanges, BmCode* newDefaultOutput, double defaultValue );
BmDecision_reinitWithDefault= core.BmDecision_reinitWithDefault
BmDecision_reinitWithDefault.restype= c_void_p
BmDecision_reinitWithDefault.argtypes= [c_void_p, c_void_p, c_void_p, c_double]

# BmTree* BmDecision_selector( BmDecision* self );
BmDecision_selector= core.BmDecision_selector
BmDecision_selector.restype= c_void_p
BmDecision_selector.argtypes= [c_void_p]

# BmBench* BmDecision_outputs( BmDecision* self );
BmDecision_outputs= core.BmDecision_outputs
BmDecision_outputs.restype= c_void_p
BmDecision_outputs.argtypes= [c_void_p]

# uint BmDecision_from( BmDecision* self, BmCode* input );
BmDecision_from= core.BmDecision_from
BmDecision_from.restype= c_uint
BmDecision_from.argtypes= [c_void_p, c_void_p]

# BmCode* BmDecision_codeFrom( BmDecision* self, BmCode* input );
BmDecision_codeFrom= core.BmDecision_codeFrom
BmDecision_codeFrom.restype= c_void_p
BmDecision_codeFrom.argtypes= [c_void_p, c_void_p]

# double BmDecision_valueFrom( BmDecision* self, BmCode* input );
BmDecision_valueFrom= core.BmDecision_valueFrom
BmDecision_valueFrom.restype= c_double
BmDecision_valueFrom.argtypes= [c_void_p, c_void_p]

# uint BmDecision_attachOuput( BmDecision* self, BmCode* newOuputCode, double ouputValue );
BmDecision_attachOuput= core.BmDecision_attachOuput
BmDecision_attachOuput.restype= c_uint
BmDecision_attachOuput.argtypes= [c_void_p, c_void_p, c_double]

# uint BmDecision_from_set( BmDecision* self, BmCode* input, uint ouputId );
BmDecision_from_set= core.BmDecision_from_set
BmDecision_from_set.restype= c_uint
BmDecision_from_set.argtypes= [c_void_p, c_void_p, c_uint]

# void BmDecision_switch( BmDecision* self, BmDecision* doppelganger );
BmDecision_switch= core.BmDecision_switch
BmDecision_switch.restype= c_void_p
BmDecision_switch.argtypes= [c_void_p, c_void_p]

# char* BmDecision_print( BmDecision* self, char* output );
BmDecision_print= core.BmDecision_print
BmDecision_print.restype= c_void_p
BmDecision_print.argtypes= [c_void_p, c_void_p]

# char* BmDecision_printSep( BmDecision* self, char* output, char* separator );
BmDecision_printSep= core.BmDecision_printSep
BmDecision_printSep.restype= c_void_p
BmDecision_printSep.argtypes= [c_void_p, c_void_p, c_void_p]
